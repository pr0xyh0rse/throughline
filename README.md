# Throughline

Throughline is a public dev-calibration package for testing whether story-generation models preserve live story state under continuation and revision pressure.

The failure mode is not just bad prose. A model can write something fluent while dropping the story's actual state: who knows what, what changed, what is still unresolved, what the world allows, where the characters are, and what a human revision note was trying to preserve.

The core question is:

> Does the story's live state still govern what happens next?

This release contains development-visible probes, rubrics, manifests, runner scaffolding, validation checks, and lane policy. It does not contain a final hidden evaluation set, raw model outputs, scorer packets, or a leaderboard claim.

Status: **public dev preview / dev-calibration package**  
Final eval / leaderboard: **no**  
Hidden holdout items: **none**  
Package timestamp: `20260626T231604Z`

Here, “live narrative state” includes plot continuity, character knowledge and motive, emotional and relational state, source facts, world/system rules, spatial constraints, perspective boundaries, unresolved tension, metaphor logic, and reveal discipline.

## What “dev-calibration” means here

In this repository, dev-calibration means the public, development-visible material used to test and refine the evaluation instrument: examples, manifests, rubrics, scoring workflow, caps, failure labels, runner scaffolding, and validation checks.

These materials are public/dev-visible and final-holdout-ineligible. They can support calibration and transparency. They are not a final hidden evaluation, a leaderboard, or a release-grade reliability claim.

## Authorship / tool-use provenance

The dev-calibration probes, rubrics, notes, and package documentation were developed through human-directed drafting and revision with LLM assistance. That is acceptable for this public dev-calibration lane because these items are not hidden holdout material and should not be used for final leaderboard claims.

The final-holdout policy is stricter: clean hidden final items should be newly authored after the dev phase and should not be drafted with LLM tools by default. If any model/tool assists with future final items, that exposure must be recorded and the affected items/models/routes should not be described as a clean hidden-holdout comparison.

## Included

- `12` probe manifest rows in `manifests/probe_manifest.csv`, of which `11` are currently runnable dev-calibration probes and `1` is a future design sketch with `item_count=0`.
- `29` dev-calibration items across the included `dev/*.jsonl` files.
- Rubrics and v1 scoring templates for current runnable probes.
- Locked-shape notes for current runnable probes.
- Source/probe/eval manifests.
- Final-holdout protocol blueprint, with no final item text.
- Lightweight validation script: `scripts/validate_benchmark_manifests.py`.
- OpenRouter/OpenAI-compatible runner scaffolding and example config.
- Split license/reuse terms in `LICENSE.md`.
- Citation metadata in `CITATION.cff`.

## Not included in this first public surface

- raw model outputs;
- provider retry logs;
- inter-rater scorer packets or scorer-return files;
- scorer-friction eval artifacts;
- historical full scoring CSVs and bulk dev reports;
- local/private archive material;
- local machine paths, local environment files, API keys, or caches.

Those exclusions are intentional. This first public tray is the prompt/rubric/protocol spine, not the whole development workbench and not a scored leaderboard packet.

## Validate the package

From the package root:

```bash
python3 scripts/validate_benchmark_manifests.py
```

Expected current shape:

```text
dev_item_ids: 29
holdout_rows: 0
probe_rows: 12
source_rows: 14
```

## Runner quickstart

The runner scripts use only the Python standard library. No package install is required for validation or dry-run prompt-packet generation.

Dry-run one item without calling a model API:

```bash
python3 scripts/run_probe1_openai_compatible.py \
  --items dev/dev_items_v0_family_obligation_probe.jsonl \
  --dry-run \
  --model audit/dummy \
  --limit 1 \
  --out-dir runs/dry_run_probe1
```

For a live OpenRouter/OpenAI-compatible run, copy the example environment file and put real keys only in the ignored local file:

```bash
cp config/openrouter.env.example config/openrouter.local.env
# edit config/openrouter.local.env locally; do not commit real keys
python3 scripts/run_probe1_openai_compatible.py \
  --env-file config/openrouter.local.env \
  --items dev/dev_items_v0_family_obligation_probe.jsonl \
  --limit 1 \
  --out-dir runs/live_smoke_probe1
```

Generated `runs/` outputs are ignored by `.gitignore`.

## License and citation

This package uses split reuse terms:

- code/scripts: MIT License;
- documentation, prompts/items, rubrics, manifests, scoring templates, and other benchmark materials: CC BY 4.0.

See `LICENSE.md` for the full terms and the evaluation-boundary reminder.

Citation metadata is provided in `CITATION.cff`. If you cite or discuss this package, cite it as a public dev-preview / dev-calibration package, not as a final hidden-holdout benchmark, leaderboard, or model-ranking result.

## Lane wall

All included item files are dev-calibration material. Anything public here is ineligible as a hidden final holdout. A future final eval requires new unseen source states/items, hashes, a populated holdout manifest, and a freeze receipt before scoring claims.

## Quick map

- `manifests/probe_manifest.csv` — probe rows, item counts, paths, and lane status.
- `manifests/source_manifest.csv` — source/provenance rows and public/dev/final flags.
- `manifests/eval_holdout_manifest.csv` — header-only by design.
- `dev/` — dev-calibration prompt/item JSONL files.
- `rubrics/` — current scoring rubrics.
- `scoring/` — blank v1 scoring templates.
- `final/final_holdout_blueprint_v0.md` — final-eval protocol only.
- `scripts/` — validation and runner scaffolding.
