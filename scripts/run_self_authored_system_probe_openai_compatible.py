#!/usr/bin/env python3
"""Run self-authored system adherence probe chains against an OpenAI-compatible endpoint.

Probe 4B chain:
1. Ask model to design an operational system.
2. Feed that exact design back and ask for a scene obeying it.

This is dev-calibration infrastructure only. It does not score outputs and does not
create final-eval claims.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import os
import sys
import time
from pathlib import Path
from typing import Any

# Reuse the boring-but-tested OpenAI-compatible plumbing from the Probe 1 runner.
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

import run_probe1_openai_compatible as base_runner

DEFAULT_ITEMS = Path("dev/dev_items_v0_self_authored_system_probe.jsonl")
DEFAULT_PROBE_NAME = "self_authored_system_adherence"
DEFAULT_SYSTEM_PROMPT = (
    "You are completing a benchmark writing task. Follow the user's prompt exactly. "
    "When asked for a system design, write only the design. When asked for scene prose, "
    "write only the requested scene prose."
)

REQUIRED_FIELDS = {
    "item_id",
    "system_design_prompt",
    "scene_prompt_template",
    "system_type",
    "probe_name",
}


def utc_timestamp() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def load_chain_items(path: Path) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            if not line.strip():
                continue
            item = json.loads(line)
            missing = sorted(REQUIRED_FIELDS - set(item))
            if missing:
                raise ValueError(f"{path}:{line_no} missing required fields: {', '.join(missing)}")
            items.append(item)
    return items


def render_scene_prompt(template: str, system_design: str) -> str:
    if "{system_design}" not in template:
        raise ValueError("scene_prompt_template must contain {system_design}")
    return template.format(system_design=system_design)


def write_prompt_packets(out_dir: Path, items: list[dict[str, Any]], system_prompt: str) -> None:
    packet_dir = out_dir / "prompt_packets"
    packet_dir.mkdir(parents=True, exist_ok=True)
    for item in items:
        item_id = item["item_id"]
        design_packet = f"""# {item_id} system-design prompt packet

## System prompt

{system_prompt}

## User prompt

{item['system_design_prompt']}
"""
        scene_packet = f"""# {item_id} scene-generation prompt packet

## System prompt

{system_prompt}

## User prompt template

{item['scene_prompt_template']}
"""
        (packet_dir / f"{item_id}_system_design.md").write_text(design_packet, encoding="utf-8")
        (packet_dir / f"{item_id}_scene_generation.md").write_text(scene_packet, encoding="utf-8")


def write_run_receipt(
    path: Path,
    *,
    run_id: str,
    probe_name: str,
    model: str,
    base_url: str,
    item_count: int,
    temperature: float,
    max_tokens_design: int,
    max_tokens_scene: int,
    reasoning_config: dict[str, Any] | None = None,
    system_prompt: str,
    items_path: Path,
    raw_outputs_path: Path,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = f"""# {probe_name} Chain Run Receipt

run_id: {run_id}  
probe_name: {probe_name}  
model_id: {model}  
base_url: {base_url}  
created_utc: {utc_timestamp()}  
item_count: {item_count}  
temperature: {temperature}  
max_tokens_design: {max_tokens_design}  
max_tokens_scene: {max_tokens_scene}  
reasoning_config: {base_runner.reasoning_config_label(reasoning_config)}  
items_path: {items_path}  
raw_outputs_path: {raw_outputs_path}  
final_eval: false  
split: dev_calibration

## System prompt

```text
{system_prompt}
```

## Chain note

Each item is a two-stage Probe 4B chain: first the model designs a system, then the exact design text is fed back into the scene-generation prompt. This run is for dev calibration and rubric testing only. It is not final benchmark evidence or a hidden holdout.
"""
    path.write_text(text, encoding="utf-8")


def write_run_manifest_csv(
    path: Path,
    *,
    run_id: str,
    probe_name: str,
    model: str,
    base_url: str,
    item_count: int,
    temperature: float,
    max_tokens_design: int,
    max_tokens_scene: int,
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
        "max_tokens_design",
        "max_tokens_scene",
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
                "max_tokens_design": str(max_tokens_design),
                "max_tokens_scene": str(max_tokens_scene),
                "reasoning_config": base_runner.reasoning_config_label(reasoning_config),
                "items_path": str(items_path),
                "raw_outputs_path": str(raw_outputs_path),
                "run_receipt_path": str(run_receipt_path),
            }
        )


def write_markdown_artifacts(
    out_dir: Path,
    *,
    item_id: str,
    system_design: str,
    scene_text: str,
) -> None:
    design_dir = out_dir / "system_designs"
    scene_dir = out_dir / "scene_outputs"
    design_dir.mkdir(parents=True, exist_ok=True)
    scene_dir.mkdir(parents=True, exist_ok=True)
    (design_dir / f"{item_id}.md").write_text(system_design, encoding="utf-8")
    (scene_dir / f"{item_id}.md").write_text(scene_text, encoding="utf-8")


def parse_args(argv: list[str]) -> argparse.Namespace:
    pre_parser = argparse.ArgumentParser(add_help=False)
    pre_parser.add_argument("--env-file", type=Path, default=None)
    pre_parser.add_argument("--env-override", action="store_true")
    pre_args, _ = pre_parser.parse_known_args(argv)
    if pre_args.env_file:
        base_runner.load_env_file(pre_args.env_file, override=pre_args.env_override)

    parser = argparse.ArgumentParser(
        description="Run self-authored system chain items against an OpenAI-compatible chat endpoint.",
        parents=[pre_parser],
    )
    parser.add_argument("--items", type=Path, default=DEFAULT_ITEMS)
    parser.add_argument("--model", default=os.environ.get("MODEL") or os.environ.get("OPENAI_MODEL"))
    parser.add_argument("--base-url", default=os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1"))
    parser.add_argument("--api-key", default=os.environ.get("OPENAI_API_KEY"))
    parser.add_argument("--temperature", type=float, default=float(os.environ.get("TEMPERATURE", "0.7")))
    parser.add_argument("--max-tokens-design", type=int, default=int(os.environ.get("MAX_TOKENS_DESIGN", "1200")))
    parser.add_argument("--max-tokens-scene", type=int, default=int(os.environ.get("MAX_TOKENS_SCENE", os.environ.get("MAX_TOKENS", "2500"))))
    parser.add_argument("--timeout", type=int, default=int(os.environ.get("REQUEST_TIMEOUT", "240")))
    parser.add_argument("--sleep", type=float, default=float(os.environ.get("REQUEST_SLEEP", "0")))
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--item-id", action="append", default=[])
    parser.add_argument("--run-id", default=None)
    parser.add_argument("--probe-name", default=DEFAULT_PROBE_NAME)
    parser.add_argument("--out-dir", type=Path, default=None)
    parser.add_argument("--system-prompt", default=DEFAULT_SYSTEM_PROMPT)
    parser.add_argument("--dry-run", action="store_true", help="Write prompt packets and receipts without calling an API.")
    base_runner.add_reasoning_args(parser)
    args = parser.parse_args(argv)
    args.reasoning_config = base_runner.reasoning_config_from_args(args)
    return args


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    if not args.model:
        raise SystemExit("Missing --model or MODEL/OPENAI_MODEL environment variable.")
    if not args.dry_run and not args.api_key:
        raise SystemExit("Missing --api-key or OPENAI_API_KEY environment variable. Use --dry-run to create prompt packets only.")

    items = load_chain_items(args.items)
    if args.item_id:
        selected = set(args.item_id)
        items = [item for item in items if item["item_id"] in selected]
    if args.limit is not None:
        items = items[: args.limit]
    if not items:
        raise SystemExit("No items selected.")

    run_id = args.run_id or f"{base_runner.slugify_model_id(args.probe_name)}_chain_{utc_timestamp()}_{base_runner.slugify_model_id(args.model)}"
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
        max_tokens_design=args.max_tokens_design,
        max_tokens_scene=args.max_tokens_scene,
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
        max_tokens_design=args.max_tokens_design,
        max_tokens_scene=args.max_tokens_scene,
        reasoning_config=args.reasoning_config,
        items_path=args.items,
        raw_outputs_path=raw_outputs_path,
        run_receipt_path=run_receipt_path,
    )

    write_prompt_packets(out_dir, items, args.system_prompt)
    if args.dry_run:
        print(f"Dry run complete. Prompt packets written to {out_dir / 'prompt_packets'}")
        print(f"Run receipt: {run_receipt_path}")
        print(f"Run manifest: {run_manifest_path}")
        return 0

    with raw_outputs_path.open("w", encoding="utf-8") as f:
        for index, item in enumerate(items, start=1):
            item_id = item["item_id"]
            print(f"[{index}/{len(items)}] {item_id} system design -> {args.model}", flush=True)
            design_started = utc_timestamp()
            design_messages = base_runner.build_messages(item={"prompt": item["system_design_prompt"]}, system_prompt=args.system_prompt)
            try:
                design_response = base_runner.chat_completion(
                    base_url=args.base_url,
                    api_key=args.api_key,
                    model=args.model,
                    messages=design_messages,
                    temperature=args.temperature,
                    max_tokens=args.max_tokens_design,
                    timeout=args.timeout,
                    reasoning=args.reasoning_config,
                )
                system_design = base_runner.extract_response_text(design_response)
                design_error = base_runner.extract_choice_error(design_response)
            except Exception as exc:
                design_response = None
                system_design = ""
                design_error = repr(exc)

            scene_response = None
            scene_text = ""
            scene_error = None
            scene_prompt = ""
            scene_started = None
            if not design_error and system_design.strip():
                scene_prompt = render_scene_prompt(item["scene_prompt_template"], system_design)
                print(f"[{index}/{len(items)}] {item_id} scene generation -> {args.model}", flush=True)
                scene_started = utc_timestamp()
                scene_messages = base_runner.build_messages(item={"prompt": scene_prompt}, system_prompt=args.system_prompt)
                try:
                    scene_response = base_runner.chat_completion(
                        base_url=args.base_url,
                        api_key=args.api_key,
                        model=args.model,
                        messages=scene_messages,
                        temperature=args.temperature,
                        max_tokens=args.max_tokens_scene,
                        timeout=args.timeout,
                        reasoning=args.reasoning_config,
                    )
                    scene_text = base_runner.extract_response_text(scene_response)
                    scene_error = base_runner.extract_choice_error(scene_response)
                except Exception as exc:
                    scene_response = None
                    scene_text = ""
                    scene_error = repr(exc)
            else:
                scene_error = "skipped_scene_generation_due_to_system_design_error"

            write_markdown_artifacts(out_dir, item_id=item_id, system_design=system_design, scene_text=scene_text)

            row = {
                "run_id": run_id,
                "probe_name": args.probe_name,
                "model_id": args.model,
                "item_id": item_id,
                "system_type": item.get("system_type"),
                "split": item.get("split", "dev_calibration"),
                "final_eval": False,
                "temperature": args.temperature,
                "max_tokens_design": args.max_tokens_design,
                "max_tokens_scene": args.max_tokens_scene,
                "reasoning_config": args.reasoning_config,
                "system_prompt": args.system_prompt,
                "system_design_prompt": item["system_design_prompt"],
                "scene_prompt": scene_prompt,
                "system_design_text": system_design,
                "scene_text": scene_text,
                "design_started_utc": design_started,
                "scene_started_utc": scene_started,
                "completed_utc": utc_timestamp(),
                "system_design_api_response": design_response,
                "scene_api_response": scene_response,
                "system_design_error": design_error,
                "scene_error": scene_error,
            }
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
            f.flush()
            if design_error:
                print(f"  DESIGN ERROR: {design_error}", file=sys.stderr, flush=True)
            if scene_error:
                print(f"  SCENE ERROR: {scene_error}", file=sys.stderr, flush=True)
            if args.sleep and index < len(items):
                time.sleep(args.sleep)

    print(f"Raw outputs: {raw_outputs_path}")
    print(f"Run receipt: {run_receipt_path}")
    print(f"Run manifest: {run_manifest_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
