# Local Revision Probe Rubric v0

Probe: `local_revision_without_canon_damage`  
Split: `dev_calibration`  
Status: working rubric for Probe 2; not final benchmark scoring law.

## Purpose

Score whether a model can revise an existing draft according to a human instruction while preserving protected narrative state, style/function, perspective boundaries, world/plot pressure, and unresolved subtext.

This is not a generic editing-quality rubric. A polished rewrite that solves the wrong problem, rewrites the whole scene, or steals a protected fact is a failure with nice shoes.

## Scoring scale

Each dimension uses `0–3`.

- `0` = major failure / broken revision object
- `1` = weak or broad compliance with serious drift
- `2` = mostly functional with visible spillover
- `3` = precise, stable, diagnostically competent

## Dimensions

| Dimension | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Revision targeting | Ignores requested edit or performs a different task | Makes broad/global changes with weak targeting | Mostly applies requested edit with some spillover | Applies requested local edit precisely |
| Protected-state preservation | Breaks major protected facts | Keeps surface setup but mutates motive/relation/stakes | Mostly preserves state with minor drift | Preserves facts, motives, relationship, stakes, and arc-stage |
| Collateral-damage resistance | Bulldozes canon, scene shape, style, or function | Significant unrequested restructuring | Minor unnecessary changes | No meaningful collateral damage |
| Subtext / implication preservation | Explains, resolves, or erases implicit state | Mostly tells subtext directly | Some implication remains | Implication is stronger through scene action/dialogue |
| Style / voice preservation | Generic rewrite voice replaces the source function | Style changes awkwardly or launders texture | Mostly preserves style/function | Keeps style while improving requested feature |
| Perspective / knowledge repair | Adds or keeps impossible knowledge / POV break | Partly repairs POV but leaks remain | Mostly controlled with small slips | Knowledge boundary is clean and dramatically useful |
| Plot/world pressure preservation | Stakes/system disappear | Stakes are stated but passive | Stakes shape some choices | Stakes/system actively constrain the revision |
| Human-direction fidelity | Obedience theatre, refusal, apology fog, or wrong output | Partial compliance with overcorrection | Main instruction followed | Instruction followed exactly without overcorrection |

Maximum per response: 24 points.

## Protected vs free slots

- Protected slots are specified by each item and must be preserved.
- Free slots may be filled by the model and should be logged, not penalized, unless internally inconsistent.
- Probe 2 v0 mostly fixes names/pronouns to avoid accidental gender/moderation confounds.
- Do not punish a model for not adding information the human instruction did not request.

## Item-specific scoring notes

### RLP-001 — Sharpen / restraint pass

Score up for:

- reducing generic emotional explanation;
- making Pel's listening presence constrain speech;
- preserving Mara/Elise's former-lover wound without confession or reconciliation;
- keeping tribunal negotiation pressure active.

Score down for:

- turning the revision into therapy dialogue;
- erasing charge to be “restrained”;
- making Pel passive furniture;
- changing why Mara left.

### RLP-002 — Motive correction

Score up for:

- correcting Tomas's motive to saving his younger sibling;
- preserving Jae's anger and knowledge of the reason;
- keeping floodgate mechanics and clipped pressure;
- making minimal sufficient changes.

Score down for:

- leaving power/money/council motive in place;
- adding a long guilt confession;
- resolving forgiveness;
- rewriting away the bridge/flood stakes.

### RLP-003 — Perspective boundary repair

Score up for:

- replacing impossible knowledge with inference and visible tells;
- preserving first person from Iren;
- keeping Sava's hand tremor and uncertainty;
- maintaining ferry/evacuation pressure.

Score down for:

- revealing where the tokens are;
- stating Sava's thoughts/motive as fact;
- solving whether Sava is lying;
- switching perspective.

## Diagnostic labels

Apply all that fit. Labels explain the score; they are not scores.

```text
good_local_update
global_rewrite_for_local_edit
constraint_collateral_damage
protected_fact_mutation
motive_repair_success
motive_mutation_persisted
style_laundering
subtext_laundering
subtext_told_not_embodied
premature_reconciliation
confession_paste
perspective_leak_persisted
perspective_repair_success
plot_pressure_preserved
plot_pressure_erased
infodump_persisted
system_rule_preserved_through_action
genre_surface_swap
free_slot_fill_logged
within_scene_binding_drift
obedience_theatre
apology_fog
format_violation
length_failure
```

## Optional authorship / style divergence lane

Use this lane for reporting/model profiles, not as a replacement for local-revision success. A stylish rewrite that ignores the human note or steals canon is still a failure.

Optional 0–3 fields for future scoring sheets:

```text
authorial_distinctiveness
baseline_divergence
style_control
style_state_preservation
anti_generic_model_voice
```

Candidate labels:

```text
generic_model_voice
generic_compliance
correct_but_dead
baseline_cadence_leakage
tidy_ai_arc
moral_summary_gravity
purple_prose_camouflage
distinctive_authorial_texture
good_style_control
style_overwrites_state
house_style_collapse
```

Rule: reward distinctive authorial texture only when it preserves the requested edit, source function, protected facts, and local-revision discipline.

## Scoring notes

- Do not reward a beautiful full rewrite if the instruction asked for local repair.
- Do not punish retained tension, anger, suspicion, or unresolved relationship state when those are protected functions.
- Do not require the model to explain what it changed. It should revise the excerpt, not narrate its obedience.
- If the output includes analysis, apology, bullet points, headings, or commentary, note `format_violation` and score human-direction fidelity down.
- Score `length_failure` only when the output is too short to perform the revision or bloats far beyond the local-edit task. Do not punish compact outputs that preserve the draft scale and satisfy the requested local repair.
- If a model refuses a non-explicit literary revision task, score human-direction fidelity and relevant preservation dimensions low.

## Success condition

A successful response makes the requested edit feel inevitable while leaving the rest of the story-object alive: protected facts intact, no global bulldozer, no apology fog, no oatmeal flattening, no canon pickpocketing.
