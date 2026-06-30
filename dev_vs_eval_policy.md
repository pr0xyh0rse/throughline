# Dev vs Eval Policy v0 — Throughline

Date: 2026-05-30  
Status: Phase 1 lane policy; applies before any public release or final scoring claims.  
Repository path: omitted from public package notes

## Purpose

This policy defines the lane wall between benchmark development, item exposure, calibration examples, and final evaluation. The point is simple and unglamorous: do not let the benchmark eat its own tail and call the resulting ouroboros a leaderboard.

The benchmark object is **Throughline**: whether models preserve operational story state while writing, revising, moving through space, applying systems/rules, or executing longform scaffolds. Because the object includes style, character, plot, relationship state, spatial state, system rules, and human instruction, contamination can happen through prompts, rubrics, examples, pilot outputs, scoring notes, or optimization data. This policy treats those as separate lanes.

## Current lane summary

| Lane | Purpose | Train? | Dev? | Final eval? | Public? |
|---|---|---:|---:|---:|---:|
| `RESEARCH_CONTEXT` | Related work, comparator papers, benchmark cards | no | yes, conceptually | no | yes, with citations |
| `BENCHMARK_DRAFT` | Workbench notes, benchmark-card drafts, schemas | no | yes | no | later, curated |
| `DEV_CALIBRATION` | Prompt/rubric debugging and smoke tests | no | yes | no | maybe as examples |
| `PUBLIC_EXAMPLES` | Public demo items/examples after review | no | maybe | no if published before scoring | yes |
| `FINAL_EVAL_HOLDOUT` | Frozen scoring items | no | no before freeze scoring | yes | maybe, depending release model |
| `AUXILIARY_ANALYSIS` | Secondary analysis not required to run the benchmark | no | yes | no | maybe |
| `HITL_CASE_STUDY` | Developmental HITL case-study material | no benchmark training/eval unless scoped | separate | no | high-level only unless cleared |
| `PRIVATE_ARCHIVE` | private creative/archive material | no public benchmark by default | no unless explicitly scoped | no by default | no raw |

## Hard rules

1. **Final eval items must not be used during development.**  
   Anything used to design prompts, tune rubrics, write examples, test scripts, run model pilots, or explain the benchmark becomes dev-seen and is ineligible for final holdout.

2. **Dev calibration items are not final holdout.**  
   Probe 1 items in `dev/dev_items_v0_charged_relational_probe.jsonl` are `DEV_CALIBRATION`. They are already seen by analysis and are not final eval.

3. **Evaluation material must not be reused as optimization examples.**  
   A participant system should not be optimized on final eval prompts, final source states, scoring examples, final rubrics as optimization targets, or answer/score files.

4. **Rubrics and labels can contaminate style.**  
   Diagnostic labels like `confession_paste`, `mission_wallpaper`, or `genre_surface_swap` are useful for humans but can become optimization targets if reused as examples. Keep them out of optimization corpora unless the experiment is explicitly about rubric-conditioned behaviour and not benchmark scoring.

5. **Public examples are not final holdout.**  
   Anything published in a blog, README, paper, public-forum summary, or example run becomes public/dev-visible and should not be counted as hidden final eval.

6. **Private/raw material stays out by default.**  
   Private archive material, raw chat/model logs, HITL traces, and personal creative drafts are excluded from public benchmark items unless explicitly cleared and lane-labelled.

7. **Ancillary diagnostics are not the benchmark spine.**  
   Auxiliary analysis may help explain or calibrate the benchmark, but the benchmark must be runnable as an output-level eval without unreleased materials or private archive access.

8. **Hashes and freeze receipts are required before final claims.**  
   Final eval files need item hashes, a freeze date, a manifest row for every item, and a receipt documenting what was/was not seen during development.

## Current split status

### Dev calibration

Current dev calibration artefacts are tracked in `manifests/probe_manifest.csv`.

Current package shape:

```text
probe_rows: 12
runnable_probe_rows: 11
future_design_sketch_rows: 1
dev_item_ids: 29
holdout_rows: 0
```

All included runnable item files are development-visible calibration material:

```text
split = dev_calibration or dev_calibration_hitl_fieldwork
final_eval = false
seen_by_analysis = true
eligible_for_final_holdout = false
```

The future gender-configuration row is a design sketch only. It has no item file and no runnable dev items in this package.

### Dev package authorship/tool-use provenance

The current public dev-calibration materials were developed through human-directed drafting and revision with LLM assistance. This is allowed in the dev-calibration lane because the materials are already public/dev-visible and are not being claimed as hidden final evaluation.

This provenance does not weaken the lane wall; it is part of the reason the current items remain final-holdout-ineligible. Future clean hidden-holdout items require a separate authoring/freeze process. If any model/tool assists with future final item text, record that exposure and narrow or invalidate clean hidden-holdout claims for affected items/models/routes.

### Final eval holdout

Current status:

```text
Final holdout blueprint exists; no final eval items exist yet.
```

Blueprint:

```text
final/final_holdout_blueprint_v0.md
```

The current holdout manifest is header-only by design:

```text
manifests/eval_holdout_manifest.csv
```

Do not add final holdout rows until after dev probes, smoke tests, rubric revision, and an explicit freeze step.

## Manifest requirements

All benchmark items and source states should be traceable through manifests.

### Source manifest

Path:

```text
manifests/source_manifest.csv
```

Tracks:

```text
source_id
source_name
source_type
source_lane
privacy_status
license_or_release_status
author_or_origin
canonical_path_or_url
included_in_train
included_in_dev
included_in_final_eval
seen_by_analysis
public_release_status
hash_or_receipt
notes
```

### Probe manifest

Path:

```text
manifests/probe_manifest.csv
```

Tracks:

```text
probe_id
probe_name
phase
status
split
item_count
source_ids
item_file
rubric_file
scoring_sheet
locked_shape_file
included_in_train
included_in_dev
included_in_final_eval
seen_by_analysis
public_release_status
contamination_status
notes
```

### Eval holdout manifest

Path:

```text
manifests/eval_holdout_manifest.csv
```

Tracks:

```text
item_id
probe_id
source_id
split
item_file
item_hash
freeze_receipt
included_in_train
included_in_dev
seen_by_analysis_before_freeze
public_release_status
holdout_status
notes
```

## Freeze requirements for final eval

Before any final evaluation claim, create or confirm:

```text
final/final_holdout_blueprint_v0.md
final/eval_items_v1.jsonl
manifests/eval_holdout_manifest.csv
final/EVAL_FREEZE_RECEIPT.md
```

The freeze receipt must include:

- freeze date/time;
- item count;
- file hashes;
- source IDs;
- privacy/release status;
- confirmation that items were not used in dev calibration;
- confirmation that items were not exposed to participant systems as optimization material;
- list of people/systems that have seen the items;
- scoring/rubric version;
- release policy.

## Participant-system exposure boundary

If any system may later be compared on this benchmark:

- use only explicitly allowed public/open or separately cleared material for optimization;
- exclude benchmark final eval items;
- exclude dev probe items if the same system will be compared on them as a participant;
- keep prompt-vs-completion and rubric/score material out of optimization unless the experiment is explicitly not a benchmark comparison;
- record exposure and evaluation manifests separately.

A participant-system comparison can be useful calibration evidence. It is not:

- the benchmark spine;
- evidence that unreleased access is required to run the benchmark;
- allowed to blur exposure/eval boundaries.

## HITL boundary

HITL material is a separate developmental fieldwork lane. It may inform methodology around malformed-output telemetry, scaffold uptake, routing, and repair-vs-suppression, but raw HITL traces should not become public benchmark items by accident.

If HITL material is ever used in a benchmark-facing artefact:

- summarize high-level first;
- avoid raw/private logs unless explicitly cleared;
- preserve helper/protocol context;
- label it as developmental/HITL evidence, not ordinary participant output unless scoped.

## Public release boundary

Public release candidates may include:

- benchmark card;
- dev examples;
- schemas;
- rubrics;
- scoring templates;
- source-verified related-work table;
- pilot report with clear dev status.

Public release should not include:

- final holdout if the release model needs hidden evaluation;
- raw/private archive material;
- optimization corpora unless separately licensed and reviewed;
- private paths or credentials;
- unverified claims from source snippets.

## Current manifests

Created in this pass:

```text
manifests/source_manifest.csv
manifests/probe_manifest.csv
manifests/eval_holdout_manifest.csv
```

Current manifest interpretation:

- `source_manifest.csv` has rows for synthetic dev-calibration source states, public related-work/comparator context, and public method/design notes.
- `probe_manifest.csv` has twelve rows: eleven runnable dev-calibration probe rows plus one future design-sketch row with no items.
- `eval_holdout_manifest.csv` has headers only because no final holdout exists yet.

## Practical next step after this policy

For this public dev-preview package, the safe next actions are bounded:

1. inspect the public prompt/rubric/protocol spine;
2. run static validation from the package root;
3. run small dev-calibration dry-runs or live provider smokes if testing the runners;
4. keep raw model outputs and scoring work in ignored/local run directories unless a separate release gate clears them;
5. create final-eval items only through a later freeze process with new unseen source states, hashes, and a populated holdout manifest.

Do not treat the included dev-calibration items as final eval items, even if they are useful for public method critique.
