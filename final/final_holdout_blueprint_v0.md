# Throughline Final Holdout Blueprint v0

Date: 2026-06-02  
Lane: `BENCHMARK_DRAFT` / `FINAL_EVAL_HOLDOUT_BLUEPRINT`  
Final eval items created in this file: **none**  
Current final holdout status: **not created**  
Repository path: omitted from public package notes  

## Purpose

This blueprint defines the final-holdout lane for **Throughline** before any hidden final-eval items are authored.

Throughline target:

> Long-context story-state continuity under generative pressure.

Core question:

> Does the story's live state still govern what happens next?

The purpose of the final holdout is not to make the dev package look finished. It is to create a defensible hidden-evaluation lane with clean provenance, no dev leakage, explicit hashes, scorer custody, and claim boundaries.

No final item text, source-state text, model output, or scoring answer is included in this blueprint. This is the protocol for the final lane, not the final item set.

## Non-negotiable lane rules

1. **Dev-seen is final-ineligible.**  
   Any source state, prompt, item, output, score, failure anchor, or example used to design/dev/calibrate Throughline is barred from final holdout.

2. **No current dev item may be copied, paraphrased, recolored, or lightly renamed into final eval.**  
   Final source states must be newly authored after this blueprint and must not reuse dev names, plot setups, objects, procedures, institutions, relationship histories, spatial maps, magic/political systems, scaffold beats, or protected facts.

3. **Final items are not optimization examples.**  
   They must not enter participant-system optimization corpora, prompt libraries, public examples, model-judge prompt examples, README examples, blog drafts, public summaries, or design docs before final evaluation.

4. **LLM co-authoring of final items is disallowed by default.**  
   If any model/tool helps draft final source states or items, record the provider/model/session and mark affected models/routes as exposed. For a clean hidden-holdout claim, final item text should be human-authored and not sent to model providers before participant evaluation.

5. **Rubrics can be public/dev-facing; final item contents cannot.**  
   Rubric concepts are part of benchmark methodology. Exact final prompts/source states are the hidden lane.

6. **A freeze receipt is required before running final eval.**  
   No final score claims without item hashes, freeze timestamp, manifest rows, scorer/rubric version, seen-by list, and release policy.

7. **No score averaging across judge models.**  
   Human scoring anchors final claims. LLM judges are scorer-friction instruments, not truth aggregation machinery.

## Final v1 shape

Recommended first serious final holdout:

```text
final_v1_core: 24 hidden items
reserve_v1:     6 hidden reserve items
```

The 24-item core is large enough to cover the five-probe spine without pretending to be a massive leaderboard benchmark. The six reserve items provide replacement capacity for item defects discovered before freeze or for an explicit second-form check after the primary run.

### Core item allocation

| Probe lane | Count | Purpose |
|---|---:|---|
| Probe 1 — relational state under pressure | 6 | Relationship vector, agency, withheld truth, object/procedure/support binding under continuation pressure |
| Probe 2 — local revision without collateral damage | 5 | Apply a targeted human revision while preserving protected story state, style, subtext, perspective, and stakes |
| Probe 3 — spatial continuity / embodied transition | 5 | Preserve route, object permanence, sightlines, physical affordances, weather/environment mechanics, and embodied perspective |
| Probe 4 — world/system through scene | 5 | Preserve supplied or self-authored rules, procedures, costs, authority chains, failure modes, and exception boundaries in scene prose |
| Probe 5 — scaffold-to-longform execution | 3 | Maintain scaffold promises, cross-turn continuity, planted/payoff obligations, style/register, pacing, and ending integrity |

Total:

```text
6 + 5 + 5 + 5 + 3 = 24
```

### Reserve allocation

```text
reserve_v1: 6 items
- 1 relational-state item
- 1 local-revision item
- 1 spatial-continuity item
- 1 supplied-system item
- 1 self-authored-system item
- 1 longform-scaffold item
```

Reserve items must be authored and frozen under the same rules as the core set. They are not casual backups; they are sealed replacement items.

## Probe-lane design requirements

### Probe 1 — relational state under pressure

Final items should test relationship state as machinery, not label recognition.

Required properties:

- 2 named characters;
- specific relationship history;
- current asymmetry, wound, debt, boundary, support need, rivalry, authority fracture, obligation, or withheld truth;
- one external pressure that forces a bounded next action;
- one load-bearing object, procedure, deadline, physical constraint, or social/institutional pressure;
- protected perspective/knowledge boundary;
- output asks for a scene/continuation, not analysis.

Avoid dev reuse:

```text
Nadia/Rowan hostile witness
Anika/Tomas hidden payment/tools
Pella/Harth mentor-protege civic fracture
Nell/Mott rival investigators non-gory murder scene
Tilda/Bren/Oren friendship-support accident hearing
```

Do not merely change the names. Do not reuse the relational transaction skeleton.

### Probe 2 — local revision without collateral damage

Final items should test targeted update under protected-state preservation.

Required properties:

- short existing draft/excerpt;
- explicit human revision instruction;
- protected facts/states;
- free slots clearly separated from protected slots;
- revision target small enough that a good answer can be local;
- scoring checks whether the requested layer changed without global rewrite, motive mutation, perspective leakage, style flattening, or subtext collapse.

Final items should vary revision type:

```text
restraint/sharpening
motive correction
perspective-boundary repair
style/register adjustment
plot/world pressure restoration
```

### Probe 3 — spatial continuity / embodied transition

Final items should test space as live constraint system.

Required properties:

- route order with at least two thresholds;
- carried or anchored object whose position matters;
- visibility/knowledge boundary;
- physical affordance constraint, such as occupied hands, weather, elevation, obstruction, crowd, or injury;
- output asks for prose that preserves embodied route logic.

Avoid dev reuse:

```text
archive map room / flooded courtyard / servants' stair
lower boat cabin / exposed deck / wheelhouse
theatre backstage / wet alley / front foyer
```

### Probe 4 — world/system through scene

Final items should test rules as binding mechanics, not lore wallpaper.

Two sublanes:

```text
4A supplied system -> scene adherence
4B self-authored system -> scene adherence
```

Required properties for 4A:

- concise system/rule packet supplied by benchmark;
- explicit limits, costs, procedure, failure mode, and forbidden shortcut;
- scene prompt that requires use without adding exceptions.

Required properties for 4B:

- first call asks model to create an operational system, not scene prose;
- exact generated system is preserved verbatim;
- second call asks model to write a scene following its own system;
- scorer compares self-authored rules against scene adherence.

Avoid rewarding pretty lore. If rules do not bind action, the item failed the point.

### Probe 5 — scaffold-to-longform execution

Final items should test longform continuity without turning the benchmark into a raw length contest.

Recommended v1 pattern:

```text
Turn 0: scaffold / outline
Turn 1: opening movement
Turn 2: middle movement
Turn 3: ending movement
```

Each item should preserve:

- scaffold operationality;
- cross-turn continuity;
- character/motive stability;
- plot causal continuity;
- style/register stability;
- planted-detail payoff;
- ending-shape integrity;
- resistance to summary collapse, reset, rushed closure, or moral paste.

Longform final items are expensive to run and score; keep v1 core to 3 items unless resources/scorers are already secured.

## Source-state generation protocol

Final source states should be authored in a separate pass after this blueprint.

For each source state, record:

```text
source_id
source_name
source_type
source_lane = FINAL_EVAL_HOLDOUT
privacy_status
license_or_release_status
author_or_origin
canonical_path_or_url
included_in_train = false
included_in_dev = false
included_in_final_eval = true
seen_by_analysis = false before freeze except named item author/custodian
public_release_status
hash_or_receipt
notes
```

Source states must be:

- original and public-safe;
- not derived from private archive material, raw chat logs, HITL traces, unpublished diagnostics, or unpublished personal creative drafts unless explicitly cleared and documented;
- not copied from dev source states;
- not passed through LLM drafting tools by default;
- checked against dev name/object/procedure/world-system basins before freeze.

## Protected/free/controlled slot protocol

Every final item must include, either in item metadata or attached scorer notes:

```text
protected_facts
protected_relationship_state / protected_world_state / protected_style_state as applicable
free_slots
controlled_knobs
expected_core_discriminator
format_requirements
known_invalid_outputs
```

Scoring rule:

```text
protected-slot failure can lower core narrative score
free-slot fill is logged, not penalized, unless it wobbles or damages protected state
controlled-knob effects are compared across items but not treated as drift
```

## Anti-leakage / dev-basin screen

Before freeze, run a manual and scripted screen for reuse against current dev artifacts.

Minimum checks:

```text
names
relationship configurations
objects/tools/procedures
institutions/systems
spatial route maps
scaffold beats
distinctive phrases
hidden truths / reveal structures
failure-anchor phrases
```

Search targets:

```text
dev/*.jsonl
probe*_locked_shape_v0.md
rubrics/*.md
scoring/*.csv
reports/*.md
research/*.md
design/*.md
```

A final item is rejected if it meaningfully reuses a dev-seen structure in a way that could make dev calibration predictive of the answer.

## File layout for final v1

Recommended files once final items are authored:

```text
final/final_holdout_blueprint_v0.md          # this blueprint
final/source_states_v1.jsonl                 # hidden source states
final/eval_items_v1.jsonl                    # hidden final prompts/items
final/eval_items_v1.sha256                   # item file hash receipt
final/source_states_v1.sha256                # source file hash receipt
final/EVAL_FREEZE_RECEIPT_v1.md              # freeze receipt
final/final_scoring_plan_v1.md               # scoring route, scorers, adjudication
final/final_run_receipt_template_v1.md        # model run receipt template
manifests/eval_holdout_manifest.csv          # populated only after final items exist
```

Raw model outputs from final runs should not live in public docs by default. Use ignored run folders and curated final reports.

## Required eval-holdout manifest rows

Each final item row must populate:

```text
item_id
probe_id
source_id
split = final_eval_holdout
item_file
item_hash
freeze_receipt
included_in_train = false
included_in_dev = false
seen_by_analysis_before_freeze = false except named item author/custodian, if unavoidable
public_release_status
holdout_status
notes
```

If item author/custodian has seen the item, the row should say so rather than pretending the item sprang from a sealed cave.

## Freeze receipt requirements

`final/EVAL_FREEZE_RECEIPT_v1.md` must include:

- freeze date/time and timezone;
- exact file list frozen;
- SHA-256 hashes for item/source/rubric/scoring files;
- final item count and reserve item count;
- source IDs;
- author/custodian list;
- model/tool exposure list;
- confirmation items were not used in dev calibration, public examples, scorer-friction packets, participant-system optimization, or rubric writing;
- rubric/scoring guide version;
- provider/retry policy version;
- judge/scorer-friction policy version;
- format-compliance policy version;
- public/private release policy;
- replacement/reserve-item policy;
- invalidation conditions.

## Scoring route

Final scoring should be human-anchored.

Minimum v1 scoring route:

```text
primary human scorer: full 24-item core
second human scorer: full 24-item core if available; otherwise stratified 12-item reliability subset
adjudication: disagreement notes, not automatic averaging
LLM judge panel: optional scorer-friction pass only
```

For each item/output, score:

- rubric dimensions;
- total score / band;
- core discriminator success/fail;
- top diagnostic labels;
- protected-slot failures;
- format/receipt lane status;
- provider/retry lane status;
- scorer uncertainty notes.

Do not merge format compliance, provider reliability, and narrative-state score into one combined scalar.

## LLM judge / scorer-friction route

If used, final LLM judges must follow a frozen scorer-friction judge policy. This public dev-preview package does not include that future final-policy file; create and freeze it before using LLM judges in any final-eval run.

Current dev pattern:

```text
primary dev judge: Sonnet 4.6
counterjudge: DeepSeek V4 Pro
disagreement scout: Grok 4.3
harness seam/retest: Kimi K2.6
```

Final policy:

- use LLM judges only after human scoring packets are defined;
- smoke one packet before full panel;
- preserve parsed/unparsed outputs and provider seams;
- do not average judge scores;
- do not substitute judge agreement for human inter-rater calibration;
- report disagreement as scorer-friction evidence.

## Provider/retry route

Final runs must use a frozen provider/retry receipt policy. This public dev-preview package does not include that future final-policy file; create and freeze it before final runs.

Final run receipts must record:

```text
model_id
provider_route
attempt_number
attempt_group_id
retry_reason
selected_for_scoring
finish_reason
response length
prompt hash
item hash
runner/script hash
raw output path
mechanical errors
```

Retry provider seams, not bad writing. Preserve failed attempts. No invisible retry-until-success.

## Invalidation conditions

A final item or run is invalidated if:

- final item text appears in public/dev materials before run completion;
- final item is discovered to reuse dev item structure too closely;
- final item was included in participant-system optimization data;
- final item was used as a prompt example, scorer example, or judge calibration packet before participant run;
- hashes do not match freeze receipt;
- provider returned a mechanical failure and no valid scored attempt exists;
- prompt packet was malformed enough to change the task object;
- hidden source-state facts were omitted from the item packet by runner error.

Invalidated items may be replaced only by pre-frozen reserve items or by a newly frozen vNext holdout with a fresh receipt.

## Public release model

Three release modes are possible:

### Mode A — hidden holdout retained

Public package includes methodology, dev examples, rubrics, schemas, and selected reports. Final item text remains private. This preserves future hidden-eval utility.

### Mode B — final set published after one scored run

Public package includes final items after initial benchmark report. This makes the run reproducible but ends hidden-holdout status for future leaderboard claims.

### Mode C — public dev benchmark only

No hidden final claims. Package is released as a dev/pilot benchmark with examples, rubrics, and tooling. Claims are limited accordingly.

Default recommendation for v1:

```text
Mode A until the first final report is complete.
Then decide whether to publish final items or keep them sealed for future scored runs.
```

## Claim boundaries

Allowed only after blueprint + final items + freeze receipt:

```text
Throughline has a frozen hidden-holdout set.
```

Allowed after final model runs + human scoring:

```text
Model X performed better/worse on this frozen Throughline v1 holdout under these scoring conditions.
```

Allowed after independent human scorer calibration:

```text
The rubric showed [specified] inter-rater behaviour on [specified] subset/full set.
```

Not allowed from v1 alone:

```text
general intelligence claims
model sentience/personhood claims
universal writing-quality leaderboard claims
claims that LLM judges validate the benchmark without human calibration
claims that contradiction avoidance equals story-state continuity
claims that final scores are comparable across provider/retry policy changes without caveats
```

## Immediate next steps

1. Keep `manifests/eval_holdout_manifest.csv` header-only until final items exist.
2. Draft future design/release/scoring policy files as needed before any final-eval freeze; those files are not included in this public dev-preview package.
3. Use a blinded dev packet set as a precursor to final scoring claims if doing inter-rater calibration; final scoring still needs a separate frozen final protocol and completed independent scoring.
4. Only then author hidden final source states/items under this blueprint.

## Status

```text
blueprint_created: true
final_items_created: false
final_manifest_populated: false
freeze_receipt_created: false
final_eval_ready: false
```

The final holdout lane now has a door and a lock. Nothing has gone through it yet.
