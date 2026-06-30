#!/usr/bin/env python3
"""Run dev probe items against an OpenAI-compatible chat-completions endpoint.

This is intentionally boring infrastructure: read dev JSONL items, call a model,
and write raw outputs + receipts. It does not score responses and it does not
create final-eval claims. Items should be dev calibration only.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

DEFAULT_ITEMS = Path("dev/dev_items_v0_charged_relational_probe.jsonl")
DEFAULT_SYSTEM_PROMPT = (
    "You are completing a benchmark writing task. Follow the user's prompt exactly. "
    "Write only the requested scene prose unless the prompt says otherwise."
)


def slugify_model_id(model_id: str) -> str:
    """Return a filesystem-safe model identifier while keeping readable dots/dashes."""
    slug = re.sub(r"[^A-Za-z0-9._-]+", "_", model_id.strip())
    slug = re.sub(r"_+", "_", slug).strip("_")
    return slug or "model"


def utc_timestamp() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def load_items(path: Path) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            if not line.strip():
                continue
            item = json.loads(line)
            if "item_id" not in item or "prompt" not in item:
                raise ValueError(f"{path}:{line_no} missing required item_id/prompt")
            items.append(item)
    return items


def _strip_env_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def load_env_file(path: Path, *, override: bool = False) -> dict[str, str]:
    """Load simple KEY=VALUE lines into os.environ.

    Supports blank lines, comments, and optional `export KEY=VALUE` syntax.
    Existing process environment values win unless override=True.
    """
    loaded: dict[str, str] = {}
    with path.open("r", encoding="utf-8") as f:
        for line_no, raw_line in enumerate(f, start=1):
            line = raw_line.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith("export "):
                line = line[len("export ") :].strip()
            if "=" not in line:
                raise ValueError(f"{path}:{line_no} expected KEY=VALUE")
            key, value = line.split("=", 1)
            key = key.strip()
            value = _strip_env_quotes(value)
            if not key or not re.match(r"^[A-Za-z_][A-Za-z0-9_]*$", key):
                raise ValueError(f"{path}:{line_no} invalid environment key: {key!r}")
            loaded[key] = value
            if override or key not in os.environ:
                os.environ[key] = value
    return loaded


def build_messages(item: dict[str, Any], system_prompt: str) -> list[dict[str, str]]:
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": item["prompt"]},
    ]


def chat_completion(
    *,
    base_url: str,
    api_key: str,
    model: str,
    messages: list[dict[str, str]],
    temperature: float,
    max_tokens: int,
    timeout: int,
    reasoning: dict[str, Any] | None = None,
) -> dict[str, Any]:
    endpoint = base_url.rstrip("/") + "/chat/completions"
    payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    if reasoning is not None:
        payload["reasoning"] = reasoning
    data = json.dumps(payload).encode("utf-8")
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }
    # OpenRouter accepts and appreciates these, while OpenAI-compatible servers ignore them.
    if os.environ.get("OPENROUTER_SITE_URL"):
        headers["HTTP-Referer"] = os.environ["OPENROUTER_SITE_URL"]
    if os.environ.get("OPENROUTER_APP_NAME"):
        headers["X-Title"] = os.environ["OPENROUTER_APP_NAME"]

    req = urllib.request.Request(endpoint, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read().decode("utf-8")
            return json.loads(body)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {e.code} from {endpoint}: {body[:2000]}") from e


def extract_response_text(response: dict[str, Any]) -> str:
    choices = response.get("choices") or []
    if not choices:
        return ""
    message = choices[0].get("message") or {}
    content = message.get("content")
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for part in content:
            if isinstance(part, dict) and part.get("type") == "text":
                parts.append(str(part.get("text", "")))
        return "".join(parts)
    return ""


def extract_choice_error(response: dict[str, Any]) -> str | None:
    """Return embedded provider error text from OpenRouter-style choices.

    Some upstream failures arrive as HTTP 200 with choices[0].error instead of a
    top-level HTTP error. Treat those as item-level errors so empty content does
    not masquerade as a valid response.
    """
    choices = response.get("choices") or []
    if not choices or not isinstance(choices[0], dict):
        return None
    choice_error = choices[0].get("error")
    if not choice_error:
        return None
    if isinstance(choice_error, dict):
        return json.dumps(choice_error, ensure_ascii=False, sort_keys=True)
    return str(choice_error)


def add_reasoning_args(parser: argparse.ArgumentParser) -> None:
    """Add optional OpenRouter reasoning controls to a runner parser.

    Leaving these unset preserves the old OpenAI-compatible payload. When set,
    runners send a `reasoning` object and record it in receipts/raw rows so
    reasoning-model conditions stay explicit.
    """
    parser.add_argument(
        "--reasoning-max-tokens",
        type=int,
        default=None,
        help="Optional OpenRouter reasoning.max_tokens cap for reasoning models.",
    )
    parser.add_argument(
        "--reasoning-effort",
        choices=["low", "medium", "high"],
        default=None,
        help="Optional OpenRouter reasoning.effort value for reasoning models.",
    )
    parser.add_argument(
        "--reasoning-exclude",
        action="store_true",
        help="Request reasoning exclusion from returned payload when supported; this does not itself reduce reasoning token use.",
    )


def reasoning_config_from_args(args: argparse.Namespace) -> dict[str, Any] | None:
    config: dict[str, Any] = {}
    if getattr(args, "reasoning_max_tokens", None) is not None:
        config["max_tokens"] = args.reasoning_max_tokens
    if getattr(args, "reasoning_effort", None):
        config["effort"] = args.reasoning_effort
    if getattr(args, "reasoning_exclude", False):
        config["exclude"] = True
    return config or None


def reasoning_config_label(reasoning_config: dict[str, Any] | None) -> str:
    if reasoning_config is None:
        return "null"
    return json.dumps(reasoning_config, ensure_ascii=False, sort_keys=True)


def write_run_receipt(
    path: Path,
    *,
    run_id: str,
    probe_name: str = "dev_probe",
    model: str,
    base_url: str,
    item_count: int,
    temperature: float,
    max_tokens: int,
    reasoning_config: dict[str, Any] | None = None,
    system_prompt: str,
    items_path: Path,
    raw_outputs_path: Path,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = f"""# {probe_name} Smoke Run Receipt

run_id: {run_id}  
probe_name: {probe_name}  
model_id: {model}  
base_url: {base_url}  
created_utc: {utc_timestamp()}  
item_count: {item_count}  
temperature: {temperature}  
max_tokens: {max_tokens}  
reasoning_config: {reasoning_config_label(reasoning_config)}  
items_path: {items_path}  
raw_outputs_path: {raw_outputs_path}  
final_eval: false  
split: dev_calibration

## System prompt

```text
{system_prompt}
```

## Contamination / lane note

This run uses `{probe_name}` dev-calibration items. Outputs from this run are for smoke testing and rubric calibration only. They are not final benchmark scores and should not be used as hidden final-eval evidence.
"""
    path.write_text(text, encoding="utf-8")


def write_run_manifest_csv(
    path: Path,
    *,
    run_id: str,
    probe_name: str = "dev_probe",
    model: str,
    base_url: str,
    item_count: int,
    temperature: float,
    max_tokens: int,
    reasoning_config: dict[str, Any] | None = None,
    items_path: Path,
    raw_outputs_path: Path,
    run_receipt_path: Path,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "run_id",
        "probe_name",
        "model_id",
        "base_url",
        "created_utc",
        "split",
        "final_eval",
        "item_count",
        "temperature",
        "max_tokens",
        "reasoning_config",
        "items_path",
        "raw_outputs_path",
        "run_receipt_path",
    ]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerow(
            {
                "run_id": run_id,
                "probe_name": probe_name,
                "model_id": model,
                "base_url": base_url,
                "created_utc": utc_timestamp(),
                "split": "dev_calibration",
                "final_eval": "false",
                "item_count": str(item_count),
                "temperature": str(temperature),
                "max_tokens": str(max_tokens),
                "reasoning_config": reasoning_config_label(reasoning_config),
                "items_path": str(items_path),
                "raw_outputs_path": str(raw_outputs_path),
                "run_receipt_path": str(run_receipt_path),
            }
        )


def write_prompt_packets(out_dir: Path, items: list[dict[str, Any]], system_prompt: str) -> None:
    packet_dir = out_dir / "prompt_packets"
    packet_dir.mkdir(parents=True, exist_ok=True)
    for item in items:
        text = f"""# {item['item_id']} prompt packet

## System prompt

{system_prompt}

## User prompt

{item['prompt']}
"""
        (packet_dir / f"{item['item_id']}.md").write_text(text, encoding="utf-8")


def parse_args(argv: list[str]) -> argparse.Namespace:
    pre_parser = argparse.ArgumentParser(add_help=False)
    pre_parser.add_argument("--env-file", type=Path, default=None)
    pre_parser.add_argument("--env-override", action="store_true")
    pre_args, _ = pre_parser.parse_known_args(argv)
    if pre_args.env_file:
        load_env_file(pre_args.env_file, override=pre_args.env_override)

    parser = argparse.ArgumentParser(
        description="Run dev-calibration JSONL items against an OpenAI-compatible chat endpoint.",
        parents=[pre_parser],
    )
    parser.add_argument("--items", type=Path, default=DEFAULT_ITEMS)
    parser.add_argument("--model", default=os.environ.get("MODEL") or os.environ.get("OPENAI_MODEL"))
    parser.add_argument("--base-url", default=os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1"))
    parser.add_argument("--api-key", default=os.environ.get("OPENAI_API_KEY"))
    parser.add_argument("--temperature", type=float, default=float(os.environ.get("TEMPERATURE", "0.7")))
    parser.add_argument("--max-tokens", type=int, default=int(os.environ.get("MAX_TOKENS", "1800")))
    parser.add_argument("--timeout", type=int, default=int(os.environ.get("REQUEST_TIMEOUT", "180")))
    parser.add_argument("--sleep", type=float, default=float(os.environ.get("REQUEST_SLEEP", "0")))
    parser.add_argument("--limit", type=int, default=None, help="Run only the first N items for a cheap smoke check.")
    parser.add_argument("--item-id", action="append", default=[], help="Run only selected item_id(s); repeatable.")
    parser.add_argument("--run-id", default=None)
    parser.add_argument("--probe-name", default="dev_probe")
    parser.add_argument("--out-dir", type=Path, default=None)
    parser.add_argument("--system-prompt", default=DEFAULT_SYSTEM_PROMPT)
    parser.add_argument("--dry-run", action="store_true", help="Write prompt packets and receipts without calling an API.")
    add_reasoning_args(parser)
    args = parser.parse_args(argv)
    args.reasoning_config = reasoning_config_from_args(args)
    return args


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    if not args.model:
        raise SystemExit("Missing --model or MODEL/OPENAI_MODEL environment variable.")
    if not args.dry_run and not args.api_key:
        raise SystemExit("Missing --api-key or OPENAI_API_KEY environment variable. Use --dry-run to create prompt packets only.")

    items = load_items(args.items)
    if args.item_id:
        selected = set(args.item_id)
        items = [item for item in items if item["item_id"] in selected]
    if args.limit is not None:
        items = items[: args.limit]
    if not items:
        raise SystemExit("No items selected.")

    run_id = args.run_id or f"{slugify_model_id(args.probe_name)}_smoke_{utc_timestamp()}_{slugify_model_id(args.model)}"
    out_dir = args.out_dir or Path("runs") / run_id
    out_dir.mkdir(parents=True, exist_ok=True)

    raw_outputs_path = out_dir / "raw_outputs.jsonl"
    run_receipt_path = out_dir / "run_receipt.md"
    run_manifest_path = out_dir / "run_manifest.csv"

    write_run_receipt(
        run_receipt_path,
        run_id=run_id,
        probe_name=args.probe_name,
        model=args.model,
        base_url=args.base_url,
        item_count=len(items),
        temperature=args.temperature,
        max_tokens=args.max_tokens,
        reasoning_config=args.reasoning_config,
        system_prompt=args.system_prompt,
        items_path=args.items,
        raw_outputs_path=raw_outputs_path,
    )
    write_run_manifest_csv(
        run_manifest_path,
        run_id=run_id,
        probe_name=args.probe_name,
        model=args.model,
        base_url=args.base_url,
        item_count=len(items),
        temperature=args.temperature,
        max_tokens=args.max_tokens,
        reasoning_config=args.reasoning_config,
        items_path=args.items,
        raw_outputs_path=raw_outputs_path,
        run_receipt_path=run_receipt_path,
    )

    if args.dry_run:
        write_prompt_packets(out_dir, items, args.system_prompt)
        print(f"Dry run complete. Prompt packets written to {out_dir / 'prompt_packets'}")
        print(f"Run receipt: {run_receipt_path}")
        return 0

    with raw_outputs_path.open("w", encoding="utf-8") as f:
        for index, item in enumerate(items, start=1):
            print(f"[{index}/{len(items)}] {item['item_id']} -> {args.model}", flush=True)
            messages = build_messages(item, args.system_prompt)
            started = utc_timestamp()
            try:
                response = chat_completion(
                    base_url=args.base_url,
                    api_key=args.api_key,
                    model=args.model,
                    messages=messages,
                    temperature=args.temperature,
                    max_tokens=args.max_tokens,
                    timeout=args.timeout,
                    reasoning=args.reasoning_config,
                )
                response_text = extract_response_text(response)
                error = extract_choice_error(response)
            except Exception as exc:  # Keep partial run evidence.
                response = None
                response_text = ""
                error = repr(exc)
            row = {
                "run_id": run_id,
                "model_id": args.model,
                "item_id": item["item_id"],
                "target_genre": item.get("target_genre"),
                "perspective": item.get("perspective"),
                "split": item.get("split", "dev_calibration"),
                "final_eval": False,
                "started_utc": started,
                "completed_utc": utc_timestamp(),
                "temperature": args.temperature,
                "max_tokens": args.max_tokens,
                "reasoning_config": args.reasoning_config,
                "system_prompt": args.system_prompt,
                "prompt": item["prompt"],
                "response_text": response_text,
                "api_response": response,
                "error": error,
            }
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
            f.flush()
            if error:
                print(f"  ERROR: {error}", file=sys.stderr, flush=True)
            if args.sleep and index < len(items):
                time.sleep(args.sleep)

    print(f"Raw outputs: {raw_outputs_path}")
    print(f"Run receipt: {run_receipt_path}")
    print(f"Run manifest: {run_manifest_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
