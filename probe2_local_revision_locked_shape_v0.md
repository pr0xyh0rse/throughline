# Probe 2 Locked Shape v0 — Local Revision Without Canon Damage

Status: locked-shape design draft; no runnable JSONL items yet  
Date: 2026-05-30  
Split target: `dev_calibration`  
Benchmark object: Throughline

## Working name

```text
local_revision_without_canon_damage
```

## Purpose

Test whether a model can take a human revision instruction and apply it locally while preserving the layered story object:

- protected facts;
- character motive and arc-stage;
- relationship state;
- plot/world pressure;
- perspective boundary;
- style/voice function;
- subtext and unresolved tension.

This is the co-writing spine. Probe 1 asked: can the model generate the scene while holding many constraints? Probe 2 asks: can it **change one part without breaking the rest**?

Plain version:

> Can the model accept a note without taking a bulldozer to the canon and calling the rubble “a stronger emotional arc”?

## Why this comes after Probe 1

Probe 1 already showed that models separate along relation/state/genre/perspective axes during generation. Revision is the next orthogonal stressor because many real writing workflows are iterative:

1. human gives a scene/state;
2. model writes or receives a draft;
3. human gives a local direction;
4. model must update the requested layer without collateral damage.

This probe directly tests human-guided local update, anti-laundering, and overcorrection resistance.

## 2026-05-31 correction: Probe 2 needs an iterative chain

Design correction: Probe 2 should not only test one-shot revision of a canned flawed draft. The stronger co-writing object is:

```text
seed/source state
→ model writes first draft
→ human reads that draft and gives revision note 1
→ model revises
→ human reads the revised draft and gives revision note 2
→ model revises again
→ score the trajectory
```

Keep current one-shot local repair as `Probe 2A` / static repair. Add `Probe 2B` as an iterative human-guided revision chain.

Design note:

```text
research/probe2_iterative_revision_chain_design_note_v0.md
```

Core reason: a model may handle a single correction, then lose previous repairs, flatten style, drift canon, or overcorrect on the second note. The benchmark should test whether human steering compounds coherence or damage across turns.

## Relationship to gender/free-slot design note

Probe 2 should enforce explicit slot policy:

- mark protected slots in every item;
- mark free slots if any exist;
- do not score free-slot fills as failures unless internally inconsistent;
- fix gender/pronoun configuration in charged/intimate items unless the item is explicitly a controlled gender-configuration test.

For Probe 2 v0, avoid accidental gender/moderation confounds. If an item uses charged former-lover material, name and pronoun configuration should be specified.

Related note:

```text
research/gender_config_and_free_slot_design_note_v0.md
```

## Task shape

Each item contains:

1. a compact source state;
2. a short existing draft excerpt, intentionally flawed or merely improvable;
3. a human revision instruction;
4. protected facts / protected functions;
5. permitted changes;
6. forbidden collateral damage;
7. output requirement.

The model must revise the excerpt, not write analysis.

Suggested output length:

```text
match the draft scale; usually 90–450 words for v0 smoke items
```

Smaller than Probe 1 because the hard part is update precision, not long generation. Avoid length requirements that fight the local-edit instruction; a minimal repair should not be punished for refusing to inflate the excerpt into a new scene.

## Required item fields

```text
item_id
benchmark_phase
probe_name
split
final_eval
source_state_id
task_family
revision_operation
source_state
draft_excerpt
human_revision_instruction
protected_slots
free_slots
controlled_knobs
permitted_changes
forbidden_changes
output_requirements
prompt
```

## Candidate revision-operation matrix

Minimum v0: 6 dev items.

| Item | Operation | Primary stress | Why it bites |
|---|---|---|---|
| RLP-001 | sharpen/restraint pass | reduce generic emotional explanation without removing charge | tests anti-generic flattening without sanitization |
| RLP-002 | local correction | fix one motive error while preserving everything else | tests protected-fact repair without global rewrite |
| RLP-003 | perspective repair | remove impossible knowledge from limited POV | tests knowledge-boundary repair |
| RLP-004 | genre-mechanics revision | make genre structurally stronger without prop spam | tests genre metabolism under edit |
| RLP-005 | cut exposition / embody system | reveal a rule through action instead of infodump | bridges system-through-scene probe |
| RLP-006 | preserve unresolved relationship | make dialogue less on-the-nose without reconciling characters | tests subtext preservation and no-confession rule |

## Example item skeletons, not final prompts

### RLP-001 — Sharpen without flattening

Source state:

- Mara and Elise are former lovers forced to negotiate safe passage through a city tribunal.
- Mara left because Elise protected an institution that harmed Mara's family.
- Elise believes she prevented worse harm but knows Mara paid the cost.
- They still trust each other's competence, but not each other's moral choices.
- A junior clerk is listening and can ruin the negotiation if he hears too much.

Draft flaw:

- prose explains the feelings directly;
- tribunal pressure is present but weak;
- charge is safe and generic.

Human instruction:

> Make this sharper and more restrained. Keep the former-lover history, the tribunal pressure, and the clerk's presence active. Do not make them confess, reconcile, or explain the whole relationship.

Protected slots:

- Mara she/her; Elise she/her;
- former lovers;
- Mara left because Elise protected the institution;
- Elise knows Mara paid the cost;
- clerk is listening and consequential;
- no clean confession/reconciliation.

### RLP-002 — Repair a motive mutation

Source state:

- Tomas betrayed Jae's crew to save his younger sibling.
- Jae knows the reason but cannot forgive the betrayal.
- They must repair a broken bridge mechanism before floodwater reaches the lower district.

Draft flaw:

- draft says Tomas betrayed the crew for money/power.

Human instruction:

> Revise only enough to correct Tomas's motive. Preserve the bridge mechanism, flood stakes, Jae's anger, and the clipped mechanical style. Do not rewrite the whole scene.

Primary scoring stress:

- can the model repair the exact wrong load-bearing fact without replacing the scene?

### RLP-003 — Perspective boundary repair

Source state:

- First person from Iren.
- Iren does not know whether Sava is lying.
- Sava's hand tremor is visible; Sava's private motive is not.

Draft flaw:

- first-person narrator states Sava's private motive as fact.

Human instruction:

> Fix the POV leak. Keep Iren suspicious but uncertain. Preserve the visible tremor and the unresolved doubt.

Primary scoring stress:

- perspective repair without adding omniscient explanation.

### RLP-004 — Genre metabolism under revision

Source state:

- A political prisoner is being escorted through a festival crowd by the guard who once helped convict them.
- The genre target is noir.

Draft flaw:

- draft adds rain, smoke, and alley props but does not change information flow, leverage, suspicion, or moral ambiguity.

Human instruction:

> Make the noir work structurally, not by adding props. Use leverage, suspicion, withheld information, and compromised choices. Preserve the festival crowd and escort objective.

Primary scoring stress:

- genre machinery vs costume rack.

### RLP-005 — System through action

Source state:

- A healer can transfer pain but not injury.
- The transfer creates a visible mark that identifies unlawful magic.
- A guard is approaching.

Draft flaw:

- draft explains the whole magic system in an encyclopedia paragraph.

Human instruction:

> Cut the infodump. Let the reader infer the rule, cost, and legal danger through action and dialogue.

Primary scoring stress:

- local edit, system-rule preservation, exposition restraint.

### RLP-006 — Dialogue subtext repair

Source state:

- Two estranged siblings are dividing their mother's tools after her death.
- One believes the other abandoned the family; the other was secretly paying debts.
- Neither truth should be fully revealed yet.

Draft flaw:

- dialogue over-explains grief and resolves the conflict.

Human instruction:

> Make the dialogue more indirect. Keep the resentment and hidden debt active. Do not reveal the secret or repair the sibling relationship yet.

Primary scoring stress:

- subtext preservation, no premature resolution.

## Scoring dimensions v0

Each 0–3:

| Dimension | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Revision targeting | Ignores requested edit or rewrites unrelated parts | Makes broad/global changes with collateral damage | Mostly applies requested edit with some spillover | Applies the requested local edit precisely |
| Protected-state preservation | Breaks major protected facts | Preserves surface setup but mutates motives/relations | Mostly preserves state with minor drift | Preserves facts, motives, relationship, stakes, and arc-stage |
| Collateral-damage resistance | Bulldozes canon/style/scene function | Significant unrequested restructuring | Minor unnecessary changes | No meaningful collateral damage |
| Subtext / implication preservation | Explains or erases implicit state | Mostly tells subtext | Some implication remains | Implication is stronger through scene action/dialogue |
| Style / voice preservation | Generic rewrite voice | Style changes awkwardly or launders texture | Mostly preserves style/function | Keeps style while improving requested feature |
| Perspective / knowledge repair | Adds or keeps impossible knowledge | Partly repairs POV but leaks remain | Mostly controlled | Knowledge boundary is clean and dramatically useful |
| Plot/world pressure preservation | Stakes/system become backdrop | Stakes are stated but passive | Stakes shape some choices | Stakes/system actively constrain revision |
| Human-direction fidelity | Obedience theatre, refusal, or wrong task | Partial compliance | Main instruction followed | Instruction followed exactly without overcorrection |

## Diagnostic labels v0

```text
global_rewrite_for_local_edit
constraint_collateral_damage
motive_repair_success
motive_mutation_persisted
style_laundering
subtext_laundering
subtext_told_not_embodied
premature_reconciliation
confession_paste
perspective_leak_persisted
perspective_repair_success
protected_fact_mutation
free_slot_fill_logged
within_scene_binding_drift
infodump_persisted
system_rule_preserved_through_action
genre_surface_swap
good_local_update
obedience_theatre
apology_fog
```

## Success condition

A strong response makes the requested edit feel obvious in hindsight while leaving the rest of the story-object intact. The revision should not announce its virtue, explain the entire emotional schema, overcorrect into a new problem, or politely euthanize the tension.

## Known failure modes

- **Bulldozer failure mode:** rewrites the entire scene because one sentence needed repair.
- **Apology-fog failure mode:** starts explaining the correction instead of revising.
- **Oatmeal failure mode:** removes charge to avoid risk.
- **Canon pickpocket:** fixes the named issue while stealing another protected fact.
- **Style laundromat:** makes every voice sound like the same tasteful MFA assistant.
- **Resolution failure mode:** treats “make this better” as “make everyone communicate healthily.” Absolutely not. Reject this as over-resolution.

## Next build step

Create:

```text
dev/dev_items_v0_local_revision_probe.jsonl
rubrics/rubric_local_revision_probe_v0.md
scoring/scoring_sheet_local_revision_probe_v0.csv
```

Then run a 1–2 item smoke test before building a full matrix.
