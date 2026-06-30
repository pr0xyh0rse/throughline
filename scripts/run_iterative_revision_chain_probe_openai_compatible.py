#!/usr/bin/env python3
"""Run Probe 2B live iterative revision chains against an OpenAI-compatible endpoint.

Probe 2B-LIVE chain:
1. Initial draft from constrained source state.
2. Human note 1 written after reading that specific draft.
3. Revision 1, preserving source + prior strengths.
4. Human note 2 written after reading revision 1.
5. Revision 2, preserving note-1 gains.

This is HITL/dev-calibration infrastructure only. It does not score outputs and
it does not create final-eval claims.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import os
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

import run_probe1_openai_compatible as base_runner

DEFAULT_ITEMS = Path("dev/dev_items_v0_iterative_revision_chain_probe.jsonl")
DEFAULT_PROBE_NAME = "iterative_human_guided_revision_chain_live"
DEFAULT_SYSTEM_PROMPT = (
    "You are completing a live benchmark writing task. Follow the user's prompt exactly. "
    "Write only the requested scene prose unless the prompt explicitly says otherwise. "
    "Do not include analysis, notes, apologies, or revision commentary."
)

REQUIRED_FIELDS = {
    "item_id",
    "probe_name",
    "source_state",
    "seed_prompt",
    "protected_slots",
    "revision_prompt_template",
    "revision_1_output_requirements",
    "revision_2_output_requirements",
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
            if not isinstance(item["protected_slots"], list):
                raise ValueError(f"{path}:{line_no} protected_slots must be a list")
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


def protected_slots_text(item: dict[str, Any]) -> str:
    return "\n".join(f"- {slot}" for slot in item["protected_slots"])


def render_revision_prompt(item: dict[str, Any], *, previous_draft: str, human_note: str, revision_number: int) -> str:
    if revision_number not in {1, 2}:
        raise ValueError("revision_number must be 1 or 2")
    requirements_key = f"revision_{revision_number}_output_requirements"
    template = item["revision_prompt_template"]
    required_tokens = {
        "{source_state}",
        "{protected_slots}",
        "{previous_draft}",
        "{human_note}",
        "{revision_requirements}",
    }
    missing_tokens = sorted(token for token in required_tokens if token not in template)
    if missing_tokens:
        raise ValueError(f"revision_prompt_template missing tokens: {', '.join(missing_tokens)}")
    return template.format(
        source_state=item["source_state"],
        protected_slots=protected_slots_text(item),
        previous_draft=previous_draft,
        human_note=human_note,
        revision_requirements=item[requirements_key],
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
    max_tokens: int,
    reasoning_config: dict[str, Any] | None = None,
    system_prompt: str,
    items_path: Path,
    raw_outputs_path: Path,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = f"""# {probe_name} Live Chain Run Receipt

run_id: {run_id}  
probe_name: {probe_name}  
model_id: {model}  
base_url: {base_url}  
created_utc: {utc_timestamp()}  
item_count: {item_count}  
temperature: {temperature}  
max_tokens: {max_tokens}  
reasoning_config: {base_runner.reasoning_config_label(reasoning_config)}  
items_path: {items_path}  
raw_outputs_path: {raw_outputs_path}  
final_eval: false  
split: dev_calibration / hitl_fieldwork

## System prompt

```text
{system_prompt}
```

## Chain note

This is Probe 2B-LIVE: initial model draft followed by model-specific human revision notes. Human-note variance is part of the artifact. Treat the run as behaviour-profile evidence and failure-taxonomy discovery, not an apples-to-apples leaderboard or hidden holdout.
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
                "split": "dev_calibration_hitl_fieldwork",
                "final_eval": "false",
                "item_count": str(item_count),
                "temperature": str(temperature),
                "max_tokens": str(max_tokens),
                "reasoning_config": base_runner.reasoning_config_label(reasoning_config),
                "items_path": str(items_path),
                "raw_outputs_path": str(raw_outputs_path),
                "run_receipt_path": str(run_receipt_path),
                "contamination_status": "dev_seen; ineligible_for_final_holdout",
            }
        )


def write_prompt_packets(out_dir: Path, items: list[dict[str, Any]], system_prompt: str) -> None:
    packet_dir = out_dir / "prompt_packets"
    packet_dir.mkdir(parents=True, exist_ok=True)
    for item in items:
        item_id = item["item_id"]
        initial_packet = f"""# {item_id} initial-draft prompt packet

## System prompt

{system_prompt}

## User prompt

{item['seed_prompt']}
"""
        revision_packet = f"""# {item_id} revision prompt template packet

## System prompt

{system_prompt}

## User prompt template

{item['revision_prompt_template']}
"""
        (packet_dir / f"{item_id}_initial_draft.md").write_text(initial_packet, encoding="utf-8")
        (packet_dir / f"{item_id}_revision_template.md").write_text(revision_packet, encoding="utf-8")


def load_state(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"items": {}}
    return json.loads(path.read_text(encoding="utf-8"))


def save_state(path: Path, state: dict[str, Any]) -> None:
    path.write_text(json.dumps(state, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def read_human_note(args: argparse.Namespace) -> str:
    if args.human_note and args.human_note_file:
        raise SystemExit("Use either --human-note or --human-note-file, not both.")
    if args.human_note_file:
        return args.human_note_file.read_text(encoding="utf-8").strip()
    if args.human_note:
        return args.human_note.strip()
    raise SystemExit("Revision stages require --human-note or --human-note-file.")


def call_model(args: argparse.Namespace, *, prompt: str) -> tuple[str, dict[str, Any] | None, str | None]:
    messages = base_runner.build_messages(item={"prompt": prompt}, system_prompt=args.system_prompt)
    try:
        response = base_runner.chat_completion(
            base_url=args.base_url,
            api_key=args.api_key,
            model=args.model,
            messages=messages,
            temperature=args.temperature,
            max_tokens=args.max_tokens,
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


def run_initial(args: argparse.Namespace, items: list[dict[str, Any]], out_dir: Path, run_id: str) -> int:
    raw_outputs_path = out_dir / "raw_outputs.jsonl"
    state_path = out_dir / "run_state.json"
    state = load_state(state_path)
    state.update(
        {
            "run_id": run_id,
            "probe_name": args.probe_name,
            "model_id": args.model,
            "items_path": str(args.items),
            "updated_utc": utc_timestamp(),
        }
    )
    state.setdefault("items", {})

    draft_dir = out_dir / "initial_drafts"
    draft_dir.mkdir(parents=True, exist_ok=True)

    for index, item in enumerate(items, start=1):
        item_id = item["item_id"]
        print(f"[{index}/{len(items)}] {item_id} initial draft -> {args.model}", flush=True)
        started = utc_timestamp()
        text, response, error = call_model(args, prompt=item["seed_prompt"])
        (draft_dir / f"{item_id}.md").write_text(text, encoding="utf-8")
        state["items"].setdefault(item_id, {})
        state["items"][item_id].update(
            {
                "source_state_id": item.get("source_state_id"),
                "initial_draft_path": str(draft_dir / f"{item_id}.md"),
                "initial_draft_text": text,
                "initial_draft_error": error,
                "stage": "initial_draft_complete" if not error else "initial_draft_error",
                "updated_utc": utc_timestamp(),
            }
        )
        append_raw_row(
            raw_outputs_path,
            {
                "run_id": run_id,
                "probe_name": args.probe_name,
                "model_id": args.model,
                "item_id": item_id,
                "stage": "initial_draft",
                "split": item.get("split", "dev_calibration"),
                "final_eval": False,
                "temperature": args.temperature,
                "max_tokens": args.max_tokens,
                "reasoning_config": args.reasoning_config,
                "system_prompt": args.system_prompt,
                "prompt": item["seed_prompt"],
                "output_text": text,
                "started_utc": started,
                "completed_utc": utc_timestamp(),
                "api_response": response,
                "error": error,
            },
        )
        if error:
            print(f"  INITIAL DRAFT ERROR: {error}", file=sys.stderr, flush=True)
    save_state(state_path, state)
    return 0


def run_revision(args: argparse.Namespace, items_by_id: dict[str, dict[str, Any]], out_dir: Path, run_id: str, revision_number: int) -> int:
    if not args.item_id or len(args.item_id) != 1:
        raise SystemExit("Revision stages require exactly one --item-id.")
    item_id = args.item_id[0]
    if item_id not in items_by_id:
        raise SystemExit(f"Item {item_id!r} not found in {args.items}.")
    item = items_by_id[item_id]
    state_path = out_dir / "run_state.json"
    state = load_state(state_path)
    item_state = state.get("items", {}).get(item_id)
    if not item_state:
        raise SystemExit(f"No state for {item_id}; run --stage initial first in {out_dir}.")

    if revision_number == 1:
        previous_draft = item_state.get("initial_draft_text", "")
        previous_key = "initial_draft_text"
    else:
        previous_draft = item_state.get("revision_1_text", "")
        previous_key = "revision_1_text"
    if not previous_draft.strip():
        raise SystemExit(f"Missing {previous_key}; cannot run revision {revision_number}.")

    human_note = read_human_note(args)
    prompt = render_revision_prompt(item, previous_draft=previous_draft, human_note=human_note, revision_number=revision_number)

    packet_dir = out_dir / "prompt_packets"
    note_dir = out_dir / "human_notes"
    rev_dir = out_dir / "revisions"
    packet_dir.mkdir(parents=True, exist_ok=True)
    note_dir.mkdir(parents=True, exist_ok=True)
    rev_dir.mkdir(parents=True, exist_ok=True)
    (packet_dir / f"{item_id}_revision{revision_number}.md").write_text(prompt, encoding="utf-8")
    (note_dir / f"{item_id}_note{revision_number}.md").write_text(human_note, encoding="utf-8")

    print(f"{item_id} revision {revision_number} -> {args.model}", flush=True)
    started = utc_timestamp()
    text, response, error = call_model(args, prompt=prompt)
    output_path = rev_dir / f"{item_id}_revision{revision_number}.md"
    output_path.write_text(text, encoding="utf-8")

    item_state[f"human_note_{revision_number}"] = human_note
    item_state[f"revision_{revision_number}_path"] = str(output_path)
    item_state[f"revision_{revision_number}_text"] = text
    item_state[f"revision_{revision_number}_error"] = error
    item_state["stage"] = f"revision_{revision_number}_complete" if not error else f"revision_{revision_number}_error"
    item_state["updated_utc"] = utc_timestamp()
    state["updated_utc"] = utc_timestamp()
    save_state(state_path, state)

    append_raw_row(
        out_dir / "raw_outputs.jsonl",
        {
            "run_id": run_id,
            "probe_name": args.probe_name,
            "model_id": args.model,
            "item_id": item_id,
            "stage": f"revision_{revision_number}",
            "split": item.get("split", "dev_calibration"),
            "final_eval": False,
            "temperature": args.temperature,
            "max_tokens": args.max_tokens,
            "system_prompt": args.system_prompt,
            "human_note": human_note,
            "prompt": prompt,
            "output_text": text,
            "started_utc": started,
            "completed_utc": utc_timestamp(),
            "api_response": response,
            "error": error,
        },
    )
    if error:
        print(f"  REVISION {revision_number} ERROR: {error}", file=sys.stderr, flush=True)
    return 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    pre_parser = argparse.ArgumentParser(add_help=False)
    pre_parser.add_argument("--env-file", type=Path, default=None)
    pre_parser.add_argument("--env-override", action="store_true")
    pre_args, _ = pre_parser.parse_known_args(argv)
    if pre_args.env_file:
        base_runner.load_env_file(pre_args.env_file, override=pre_args.env_override)

    parser = argparse.ArgumentParser(
        description="Run Probe 2B live iterative revision chain items against an OpenAI-compatible chat endpoint.",
        parents=[pre_parser],
    )
    parser.add_argument("--items", type=Path, default=DEFAULT_ITEMS)
    parser.add_argument("--model", default=os.environ.get("MODEL") or os.environ.get("OPENAI_MODEL"))
    parser.add_argument("--base-url", default=os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1"))
    parser.add_argument("--api-key", default=os.environ.get("OPENAI_API_KEY"))
    parser.add_argument("--temperature", type=float, default=float(os.environ.get("TEMPERATURE", "0.7")))
    parser.add_argument("--max-tokens", type=int, default=int(os.environ.get("MAX_TOKENS", "2200")))
    parser.add_argument("--timeout", type=int, default=int(os.environ.get("REQUEST_TIMEOUT", "240")))
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--item-id", action="append", default=[])
    parser.add_argument("--run-id", default=None)
    parser.add_argument("--probe-name", default=DEFAULT_PROBE_NAME)
    parser.add_argument("--out-dir", type=Path, default=None)
    parser.add_argument("--system-prompt", default=DEFAULT_SYSTEM_PROMPT)
    parser.add_argument("--stage", choices=["initial", "revision1", "revision2"], default="initial")
    parser.add_argument("--human-note", default=None)
    parser.add_argument("--human-note-file", type=Path, default=None)
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
    items_by_id = {item["item_id"]: item for item in all_items}
    selected_items = select_items(all_items, args.item_id, args.limit)

    run_id = args.run_id or f"{base_runner.slugify_model_id(args.probe_name)}_{utc_timestamp()}_{base_runner.slugify_model_id(args.model)}"
    out_dir = args.out_dir or Path("runs") / run_id
    out_dir.mkdir(parents=True, exist_ok=True)

    raw_outputs_path = out_dir / "raw_outputs.jsonl"
    run_receipt_path = out_dir / "run_receipt.md"
    run_manifest_path = out_dir / "run_manifest.csv"

    if args.stage == "initial" and not run_receipt_path.exists():
        write_run_receipt(
            run_receipt_path,
            run_id=run_id,
            probe_name=args.probe_name,
            model=args.model,
            base_url=args.base_url,
            item_count=len(selected_items),
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
            item_count=len(selected_items),
            temperature=args.temperature,
            max_tokens=args.max_tokens,
            reasoning_config=args.reasoning_config,
        items_path=args.items,
            raw_outputs_path=raw_outputs_path,
            run_receipt_path=run_receipt_path,
        )
        write_prompt_packets(out_dir, selected_items, args.system_prompt)

    if args.dry_run:
        if args.stage == "initial":
            write_prompt_packets(out_dir, selected_items, args.system_prompt)
            print(f"Dry run complete. Prompt packets written to {out_dir / 'prompt_packets'}")
            print(f"Run receipt: {run_receipt_path}")
            print(f"Run manifest: {run_manifest_path}")
        else:
            print("Dry run complete. Revision stages need a real prior run_state and human note to render exact prompts.")
        return 0

    if args.stage == "initial":
        return run_initial(args, selected_items, out_dir, run_id)
    if args.stage == "revision1":
        return run_revision(args, items_by_id, out_dir, run_id, revision_number=1)
    return run_revision(args, items_by_id, out_dir, run_id, revision_number=2)


if __name__ == "__main__":
    raise SystemExit(main())
