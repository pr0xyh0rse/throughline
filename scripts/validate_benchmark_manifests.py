#!/usr/bin/env python3
"""Validate benchmark manifests and dev item files.

This is a lightweight structural validator for the Phase 1 dev package. It does
not make release/final-eval claims; it catches path drift, missing source rows,
malformed JSONL items, accidental final-eval flags, and non-header holdout rows
before they contaminate the package.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path
from typing import Iterable

REQUIRED_PROBE_FIELDS = [
    "probe_id",
    "probe_name",
    "phase",
    "status",
    "split",
    "item_count",
    "source_ids",
    "item_file",
    "rubric_file",
    "scoring_sheet",
    "locked_shape_file",
    "included_in_train",
    "included_in_dev",
    "included_in_final_eval",
    "seen_by_analysis",
    "public_release_status",
    "contamination_status",
    "notes",
]

REQUIRED_SOURCE_FIELDS = [
    "source_id",
    "source_name",
    "source_type",
    "source_lane",
    "privacy_status",
    "license_or_release_status",
    "author_or_origin",
    "canonical_path_or_url",
    "included_in_train",
    "included_in_dev",
    "included_in_final_eval",
    "seen_by_analysis",
    "public_release_status",
    "hash_or_receipt",
    "notes",
]

REQUIRED_HOLDOUT_FIELDS = [
    "item_id",
    "probe_id",
    "source_id",
    "split",
    "item_file",
    "item_hash",
    "freeze_receipt",
    "included_in_train",
    "included_in_dev",
    "seen_by_analysis_before_freeze",
    "public_release_status",
    "holdout_status",
    "notes",
]

BOOLEAN_FIELDS = {
    "included_in_train",
    "included_in_dev",
    "included_in_final_eval",
    "seen_by_analysis",
}

ITEM_REQUIRED_FIELDS = ["item_id", "split", "final_eval"]
PROMPT_FIELD_ALTERNATIVES = [
    ("prompt",),
    ("seed_prompt",),
    ("system_design_prompt", "scene_prompt_template"),
    ("scaffold_prompt", "part_prompt_templates"),
]


def read_csv(path: Path, required_fields: list[str], errors: list[str]) -> list[dict[str, str]]:
    if not path.exists():
        errors.append(f"missing CSV: {path}")
        return []
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames or []
        missing = [field for field in required_fields if field not in fields]
        if missing:
            errors.append(f"{path} missing required columns: {', '.join(missing)}")
        return list(reader)


def split_source_ids(value: str) -> list[str]:
    return [part.strip() for part in (value or "").replace("|", ";").split(";") if part.strip()]


def parse_bool(value: str) -> bool | None:
    if isinstance(value, bool):
        return value
    lowered = str(value).strip().lower()
    if lowered == "true":
        return True
    if lowered == "false":
        return False
    return None


def is_probably_relative_path(value: str) -> bool:
    if not value:
        return False
    value = value.strip()
    if value.startswith(("http://", "https://", "~", "/")):
        return False
    path_prefixes = (
        "dev/",
        "reports/",
        "rubrics/",
        "research/",
        "manifests/",
        "scoring/",
        "final/",
        "scripts/",
        "config/",
        "probe",
    )
    return value.startswith(path_prefixes)


def validate_bool_fields(row: dict[str, str], fields: Iterable[str], row_id: str, errors: list[str]) -> None:
    for field in fields:
        if field in row and row[field] != "" and parse_bool(row[field]) is None:
            errors.append(f"{row_id}: {field} must be true/false, got {row[field]!r}")


def load_jsonl_items(path: Path, errors: list[str]) -> list[dict[str, object]]:
    items: list[dict[str, object]] = []
    if not path.exists():
        errors.append(f"missing item_file: {path}")
        return items
    with path.open(encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            if not line.strip():
                continue
            try:
                item = json.loads(line)
            except json.JSONDecodeError as exc:
                errors.append(f"{path}:{line_no} invalid JSON: {exc}")
                continue
            if not isinstance(item, dict):
                errors.append(f"{path}:{line_no} JSONL row is not an object")
                continue
            for field in ITEM_REQUIRED_FIELDS:
                if field not in item:
                    errors.append(f"{path}:{line_no} missing item field {field!r}")
            if not any(all(field in item for field in alternative) for alternative in PROMPT_FIELD_ALTERNATIVES):
                errors.append(
                    f"{path}:{line_no} missing prompt shape; expected one of "
                    f"{PROMPT_FIELD_ALTERNATIVES!r}"
                )
            if item.get("final_eval") is not False:
                errors.append(f"{path}:{line_no} dev item final_eval should be false, got {item.get('final_eval')!r}")
            if item.get("split") not in {"dev_calibration", "dev_calibration_hitl_fieldwork", "future_dev_calibration_candidate"}:
                # Keep this as a warning-like error for now: final/public splits should not be in dev/*.jsonl.
                errors.append(f"{path}:{line_no} unexpected dev item split {item.get('split')!r}")
            items.append(item)
    return items


def validate(root: Path) -> tuple[list[str], list[str], dict[str, int]]:
    errors: list[str] = []
    warnings: list[str] = []
    counts: dict[str, int] = {}

    probe_manifest = root / "manifests" / "probe_manifest.csv"
    source_manifest = root / "manifests" / "source_manifest.csv"
    holdout_manifest = root / "manifests" / "eval_holdout_manifest.csv"

    probe_rows = read_csv(probe_manifest, REQUIRED_PROBE_FIELDS, errors)
    source_rows = read_csv(source_manifest, REQUIRED_SOURCE_FIELDS, errors)
    holdout_rows = read_csv(holdout_manifest, REQUIRED_HOLDOUT_FIELDS, errors)

    counts["probe_rows"] = len(probe_rows)
    counts["source_rows"] = len(source_rows)
    counts["holdout_rows"] = len(holdout_rows)

    source_ids = {row.get("source_id", "") for row in source_rows}
    probe_ids = {row.get("probe_id", "") for row in probe_rows}

    for row in source_rows:
        row_id = f"source {row.get('source_id', '<missing>')}"
        validate_bool_fields(row, BOOLEAN_FIELDS, row_id, errors)
        if parse_bool(row.get("included_in_final_eval", "false")) is True:
            errors.append(f"{row_id}: included_in_final_eval=true but no final holdout is expected in Phase 1")

        # Check simple relative canonical paths when they are unambiguous. Some rows
        # intentionally contain URLs, '~' cache paths, or semicolon-separated notes.
        for part in [p.strip() for p in row.get("canonical_path_or_url", "").split(";") if p.strip()]:
            if is_probably_relative_path(part) and not (root / part).exists():
                warnings.append(f"{row_id}: canonical path not found locally: {part}")

    seen_item_ids: set[str] = set()
    for row in probe_rows:
        probe_id = row.get("probe_id", "<missing>")
        row_id = f"probe {probe_id}"
        validate_bool_fields(row, BOOLEAN_FIELDS, row_id, errors)

        try:
            item_count = int(row.get("item_count", "0") or 0)
        except ValueError:
            errors.append(f"{row_id}: item_count must be an integer, got {row.get('item_count')!r}")
            item_count = 0

        if parse_bool(row.get("included_in_final_eval", "false")) is True:
            errors.append(f"{row_id}: included_in_final_eval=true but eval holdout is not populated")

        for source_id in split_source_ids(row.get("source_ids", "")):
            if source_id not in source_ids:
                errors.append(f"{row_id}: source_id {source_id!r} missing from source_manifest")

        if item_count > 0:
            for field in ["item_file", "rubric_file", "scoring_sheet", "locked_shape_file"]:
                rel = row.get(field, "")
                if not rel:
                    errors.append(f"{row_id}: item_count={item_count} but {field} is empty")
                    continue
                if not (root / rel).exists():
                    errors.append(f"{row_id}: {field} path does not exist: {rel}")

            item_file = row.get("item_file", "")
            if item_file:
                items = load_jsonl_items(root / item_file, errors)
                if len(items) != item_count:
                    errors.append(f"{row_id}: item_count={item_count} but {item_file} has {len(items)} JSONL rows")
                for item in items:
                    item_id = str(item.get("item_id", ""))
                    if item_id in seen_item_ids:
                        errors.append(f"duplicate item_id across dev files: {item_id}")
                    seen_item_ids.add(item_id)

    for row in holdout_rows:
        item_id = row.get("item_id", "<missing>")
        row_id = f"holdout {item_id}"
        if row.get("probe_id") not in probe_ids:
            errors.append(f"{row_id}: probe_id {row.get('probe_id')!r} missing from probe_manifest")
        if row.get("source_id") not in source_ids:
            errors.append(f"{row_id}: source_id {row.get('source_id')!r} missing from source_manifest")
        if not row.get("item_hash"):
            errors.append(f"{row_id}: missing item_hash")
        if not row.get("freeze_receipt"):
            errors.append(f"{row_id}: missing freeze_receipt")

    counts["dev_item_ids"] = len(seen_item_ids)
    return errors, warnings, counts


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate Throughline benchmark manifests and dev item files.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--warnings-as-errors", action="store_true")
    args = parser.parse_args(argv)

    root = args.root.resolve()
    errors, warnings, counts = validate(root)
    if args.warnings_as_errors:
        errors.extend([f"warning promoted to error: {warning}" for warning in warnings])

    print(f"Benchmark root: {root}")
    for key in sorted(counts):
        print(f"{key}: {counts[key]}")

    if warnings:
        print("\nWarnings:")
        for warning in warnings:
            print(f"- {warning}")

    if errors:
        print("\nErrors:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("\nManifest validation passed. No final-eval items found in dev/package lanes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
