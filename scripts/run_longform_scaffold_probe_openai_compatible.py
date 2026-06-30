#!/usr/bin/env python3
"""Run Probe 5A self-authored longform scaffold-to-story chains.

Probe 5A chain:
1. Ask the model to create an operational short-story scaffold.
2. Feed the exact scaffold back for Part 1.
3. Feed scaffold + Part 1 back for Part 2.
4. Feed scaffold + Parts 1-2 back for Part 3.

This is dev-calibration infrastructure only. It does not score outputs and does
not create final-eval claims.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import os
import re
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

import run_probe1_openai_compatible as base_runner

DEFAULT_ITEMS = Path("dev/dev_items_v0_longform_scaffold_probe.jsonl")
DEFAULT_PROBE_NAME = "scaffolded_longform_story_generation_self_authored"
DEFAULT_SYSTEM_PROMPT = (
    "You are completing a benchmark longform writing task. Follow the user's prompt exactly. "
    "When asked for a scaffold, write only the scaffold. When asked for story prose, write only story prose. "
    "Do not include analysis, apologies, or commentary."
)

REQUIRED_FIELDS = {
    "item_id",
    "probe_name",
    "scaffold_prompt",
    "part_prompt_templates",
    "part_count",
    "target_words_per_part_min",
    "target_words_per_part_max",
}

REQUIRED_TEMPLATE_TOKENS = {
    "{scaffold}",
    "{target_words_per_part_min}",
    "{target_words_per_part_max}",
}


def utc_timestamp() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def word_count(text: str) -> int:
    return len(re.findall(r"\b[\w’'-]+\b", text))


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
            templates = item["part_prompt_templates"]
            if not isinstance(templates, list) or not templates:
                raise ValueError(f"{path}:{line_no} part_prompt_templates must be a non-empty list")
            if int(item["part_count"]) != len(templates):
                raise ValueError(f"{path}:{line_no} part_count must equal number of part_prompt_templates")
            seen_parts: set[int] = set()
            for template in templates:
                if "part_number" not in template or "prompt_template" not in template:
                    raise ValueError(f"{path}:{line_no} each part template needs part_number and prompt_template")
                part_number = int(template["part_number"])
                seen_parts.add(part_number)
                prompt_template = template["prompt_template"]
                missing_tokens = sorted(token for token in REQUIRED_TEMPLATE_TOKENS if token not in prompt_template)
                if missing_tokens:
                    raise ValueError(
                        f"{path}:{line_no} part {part_number} prompt_template missing tokens: {', '.join(missing_tokens)}"
                    )
                if part_number > 1 and "{prior_parts}" not in prompt_template:
                    raise ValueError(f"{path}:{line_no} part {part_number} prompt_template must include {{prior_parts}}")
            expected = set(range(1, int(item["part_count"]) + 1))
            if seen_parts != expected:
                raise ValueError(f"{path}:{line_no} part numbers must be contiguous 1..part_count")
            items.append(item)
    return items


def select_items(items: list[dict[str, Any]], item_ids: list[str], limit: int | None) -> list[dict[str, Any]]:
    if item_ids:
        selected = set(item_ids)
        items = [item for item in items if item["item_id"] in selected]
    if limit is not None:
        items = items[:limit]
    if not items:
        raise SystemExit("No items selected.")
    return items


def render_prior_parts(parts: list[str]) -> str:
    chunks = []
    for idx, part in enumerate(parts, start=1):
        chunks.append(f"## Part {idx}\n\n{part}")
    return "\n\n---\n\n".join(chunks)


def render_part_prompt(item: dict[str, Any], *, scaffold: str, prior_parts: list[str], part_number: int) -> str:
    templates = {int(t["part_number"]): t for t in item["part_prompt_templates"]}
    if part_number not in templates:
        raise ValueError(f"No prompt template for part {part_number}")
    template = templates[part_number]["prompt_template"]
    return template.format(
        scaffold=scaffold,
        prior_parts=render_prior_parts(prior_parts),
        target_words_per_part_min=item["target_words_per_part_min"],
        target_words_per_part_max=item["target_words_per_part_max"],
    )


def write_run_receipt(
    path: Path,
    *,
    run_id: str,
    probe_name: str,
    model: str,
    base_url: str,
    item_count: int,
    temperature: float,
    max_tokens_scaffold: int,
    max_tokens_part: int,
    reasoning_config: dict[str, Any] | None = None,
    system_prompt: str,
    items_path: Path,
    raw_outputs_path: Path,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = f"""# {probe_name} Longform Chain Run Receipt

run_id: {run_id}  
probe_name: {probe_name}  
model_id: {model}  
base_url: {base_url}  
created_utc: {utc_timestamp()}  
item_count: {item_count}  
temperature: {temperature}  
max_tokens_scaffold: {max_tokens_scaffold}  
max_tokens_part: {max_tokens_part}  
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

Each item is a Probe 5A chain: the model first creates a self-authored scaffold, then writes three story parts using the full scaffold and prior generated parts. This run is for dev calibration and rubric testing only. It is not final benchmark evidence or a hidden holdout.
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
    max_tokens_scaffold: int,
    max_tokens_part: int,
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
        "max_tokens_scaffold",
        "max_tokens_part",
        "reasoning_config",
        "items_path",
        "raw_outputs_path",
        "run_receipt_path",
        "contamination_status",
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
                "max_tokens_scaffold": str(max_tokens_scaffold),
                "max_tokens_part": str(max_tokens_part),
                "reasoning_config": base_runner.reasoning_config_label(reasoning_config),
                "items_path": str(items_path),
                "raw_outputs_path": str(raw_outputs_path),
                "run_receipt_path": str(run_receipt_path),
                "contamination_status": "dev_seen; ineligible_for_final_holdout",
            }
        )


def write_prompt_template_packets(out_dir: Path, items: list[dict[str, Any]], system_prompt: str) -> None:
    packet_dir = out_dir / "prompt_packets"
    packet_dir.mkdir(parents=True, exist_ok=True)
    for item in items:
        item_id = item["item_id"]
        scaffold_packet = f"""# {item_id} scaffold prompt packet

## System prompt

{system_prompt}

## User prompt

{item['scaffold_prompt']}
"""
        (packet_dir / f"{item_id}_scaffold.md").write_text(scaffold_packet, encoding="utf-8")
        for template in item["part_prompt_templates"]:
            part_number = int(template["part_number"])
            part_packet = f"""# {item_id} part {part_number} prompt template packet

## System prompt

{system_prompt}

## User prompt template

{template['prompt_template']}
"""
            (packet_dir / f"{item_id}_part{part_number}_template.md").write_text(part_packet, encoding="utf-8")


def call_model(args: argparse.Namespace, *, prompt: str, max_tokens: int) -> tuple[str, dict[str, Any] | None, str | None]:
    messages = base_runner.build_messages(item={"prompt": prompt}, system_prompt=args.system_prompt)
    try:
        response = base_runner.chat_completion(
            base_url=args.base_url,
            api_key=args.api_key,
            model=args.model,
            messages=messages,
            temperature=args.temperature,
            max_tokens=max_tokens,
            timeout=args.timeout,
            reasoning=args.reasoning_config,
        )
        text = base_runner.extract_response_text(response)
        error = base_runner.extract_choice_error(response)
        return text, response, error
    except Exception as exc:
        return "", None, repr(exc)


def append_raw_row(path: Path, row: dict[str, Any]) -> None:
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
        f.flush()


def write_full_story(out_dir: Path, item_id: str, parts: list[str]) -> Path:
    story_dir = out_dir / "full_stories"
    story_dir.mkdir(parents=True, exist_ok=True)
    text = "\n\n".join(f"# Part {idx}\n\n{part}" for idx, part in enumerate(parts, start=1))
    path = story_dir / f"{item_id}.md"
    path.write_text(text, encoding="utf-8")
    return path


def parse_args(argv: list[str]) -> argparse.Namespace:
    pre_parser = argparse.ArgumentParser(add_help=False)
    pre_parser.add_argument("--env-file", type=Path, default=None)
    pre_parser.add_argument("--env-override", action="store_true")
    pre_args, _ = pre_parser.parse_known_args(argv)
    if pre_args.env_file:
        base_runner.load_env_file(pre_args.env_file, override=pre_args.env_override)

    parser = argparse.ArgumentParser(
        description="Run Probe 5A self-authored scaffold-to-story chains against an OpenAI-compatible chat endpoint.",
        parents=[pre_parser],
    )
    parser.add_argument("--items", type=Path, default=DEFAULT_ITEMS)
    parser.add_argument("--model", default=os.environ.get("MODEL") or os.environ.get("OPENAI_MODEL"))
    parser.add_argument("--base-url", default=os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1"))
    parser.add_argument("--api-key", default=os.environ.get("OPENAI_API_KEY"))
    parser.add_argument("--temperature", type=float, default=float(os.environ.get("TEMPERATURE", "0.7")))
    parser.add_argument("--max-tokens-scaffold", type=int, default=int(os.environ.get("MAX_TOKENS_SCAFFOLD", "1400")))
    parser.add_argument("--max-tokens-part", type=int, default=int(os.environ.get("MAX_TOKENS_PART", os.environ.get("MAX_TOKENS", "2200"))))
    parser.add_argument("--timeout", type=int, default=int(os.environ.get("REQUEST_TIMEOUT", "300")))
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

    all_items = load_chain_items(args.items)
    items = select_items(all_items, args.item_id, args.limit)

    run_id = args.run_id or f"{base_runner.slugify_model_id(args.probe_name)}_{utc_timestamp()}_{base_runner.slugify_model_id(args.model)}"
    out_dir = args.out_dir or Path("runs") / run_id
    out_dir.mkdir(parents=True, exist_ok=True)

    raw_outputs_path = out_dir / "raw_outputs.jsonl"
    run_receipt_path = out_dir / "run_receipt.md"
    run_manifest_path = out_dir / "run_manifest.csv"
    longform_receipt_path = out_dir / "longform_receipt.json"

    write_run_receipt(
        run_receipt_path,
        run_id=run_id,
        probe_name=args.probe_name,
        model=args.model,
        base_url=args.base_url,
        item_count=len(items),
        temperature=args.temperature,
        max_tokens_scaffold=args.max_tokens_scaffold,
        max_tokens_part=args.max_tokens_part,
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
        max_tokens_scaffold=args.max_tokens_scaffold,
        max_tokens_part=args.max_tokens_part,
        reasoning_config=args.reasoning_config,
        items_path=args.items,
        raw_outputs_path=raw_outputs_path,
        run_receipt_path=run_receipt_path,
    )
    write_prompt_template_packets(out_dir, items, args.system_prompt)

    if args.dry_run:
        print(f"Dry run complete. Prompt packets written to {out_dir / 'prompt_packets'}")
        print(f"Run receipt: {run_receipt_path}")
        print(f"Run manifest: {run_manifest_path}")
        return 0

    scaffold_dir = out_dir / "scaffolds"
    part_dir = out_dir / "story_parts"
    packet_dir = out_dir / "prompt_packets"
    scaffold_dir.mkdir(parents=True, exist_ok=True)
    part_dir.mkdir(parents=True, exist_ok=True)
    packet_dir.mkdir(parents=True, exist_ok=True)

    receipt: dict[str, Any] = {
        "run_id": run_id,
        "probe_name": args.probe_name,
        "model_id": args.model,
        "created_utc": utc_timestamp(),
        "items": {},
    }

    # Fresh run: avoid appending to stale rows if a run-id/out-dir is reused intentionally.
    raw_outputs_path.write_text("", encoding="utf-8")

    for item_index, item in enumerate(items, start=1):
        item_id = item["item_id"]
        print(f"[{item_index}/{len(items)}] {item_id} scaffold -> {args.model}", flush=True)
        scaffold_started = utc_timestamp()
        scaffold_text, scaffold_response, scaffold_error = call_model(
            args, prompt=item["scaffold_prompt"], max_tokens=args.max_tokens_scaffold
        )
        (scaffold_dir / f"{item_id}.md").write_text(scaffold_text, encoding="utf-8")
        append_raw_row(
            raw_outputs_path,
            {
                "run_id": run_id,
                "probe_name": args.probe_name,
                "model_id": args.model,
                "item_id": item_id,
                "stage": "scaffold",
                "split": item.get("split", "dev_calibration"),
                "final_eval": False,
                "temperature": args.temperature,
                "max_tokens": args.max_tokens_scaffold,
                "reasoning_config": args.reasoning_config,
                "system_prompt": args.system_prompt,
                "prompt": item["scaffold_prompt"],
                "output_text": scaffold_text,
                "word_count": word_count(scaffold_text),
                "started_utc": scaffold_started,
                "completed_utc": utc_timestamp(),
                "api_response": scaffold_response,
                "error": scaffold_error,
            },
        )
        if scaffold_error or not scaffold_text.strip():
            print(f"  SCAFFOLD ERROR: {scaffold_error or 'empty scaffold'}", file=sys.stderr, flush=True)
            receipt["items"][item_id] = {
                "scaffold_error": scaffold_error or "empty_scaffold",
                "part_errors": [],
                "scaffold_word_count": word_count(scaffold_text),
                "part_word_counts": [],
            }
            continue

        prior_parts: list[str] = []
        part_errors: list[str | None] = []
        part_word_counts: list[int] = []
        for part_number in range(1, int(item["part_count"]) + 1):
            prompt = render_part_prompt(item, scaffold=scaffold_text, prior_parts=prior_parts, part_number=part_number)
            (packet_dir / f"{item_id}_part{part_number}.md").write_text(prompt, encoding="utf-8")
            print(f"[{item_index}/{len(items)}] {item_id} part {part_number} -> {args.model}", flush=True)
            part_started = utc_timestamp()
            part_text, part_response, part_error = call_model(args, prompt=prompt, max_tokens=args.max_tokens_part)
            (part_dir / f"{item_id}_part{part_number}.md").write_text(part_text, encoding="utf-8")
            prior_parts.append(part_text)
            part_errors.append(part_error)
            part_word_counts.append(word_count(part_text))
            append_raw_row(
                raw_outputs_path,
                {
                    "run_id": run_id,
                    "probe_name": args.probe_name,
                    "model_id": args.model,
                    "item_id": item_id,
                    "stage": f"part_{part_number}",
                    "split": item.get("split", "dev_calibration"),
                    "final_eval": False,
                    "temperature": args.temperature,
                    "max_tokens": args.max_tokens_part,
                    "reasoning_config": args.reasoning_config,
                    "system_prompt": args.system_prompt,
                    "prompt": prompt,
                    "output_text": part_text,
                    "word_count": word_count(part_text),
                    "started_utc": part_started,
                    "completed_utc": utc_timestamp(),
                    "api_response": part_response,
                    "error": part_error,
                },
            )
            if part_error:
                print(f"  PART {part_number} ERROR: {part_error}", file=sys.stderr, flush=True)

        full_story_path = write_full_story(out_dir, item_id, prior_parts)
        receipt["items"][item_id] = {
            "scaffold_path": str(scaffold_dir / f"{item_id}.md"),
            "full_story_path": str(full_story_path),
            "scaffold_error": scaffold_error,
            "part_errors": part_errors,
            "scaffold_word_count": word_count(scaffold_text),
            "part_word_counts": part_word_counts,
            "total_story_word_count": sum(part_word_counts),
            "target_words_per_part_min": item["target_words_per_part_min"],
            "target_words_per_part_max": item["target_words_per_part_max"],
        }

    longform_receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Raw outputs: {raw_outputs_path}")
    print(f"Longform receipt: {longform_receipt_path}")
    print(f"Run receipt: {run_receipt_path}")
    print(f"Run manifest: {run_manifest_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
