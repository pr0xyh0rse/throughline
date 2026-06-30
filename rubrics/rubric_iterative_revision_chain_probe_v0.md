# Rubric v0 — Iterative Human-Guided Revision Chain

Lane: `DEV_CALIBRATION` / `HITL_FIELDWORK`  
Final eval: false

Score each dimension 0–3. Use notes and diagnostic labels; do not collapse this into a preference-only score.

## Operational definition: `show_dont_tell`

For this benchmark, **show-don't-tell does not mean “ban exposition.”** Exposition is allowed when it performs necessary scene work: orienting the reader, bridging into the actual request, clarifying stakes, or making the target inference legible without bloating the prose.

Score the *function* of exposition, not its mere presence.

Good exposition:

- is brief, load-bearing, and proportionate to the scene's needs;
- leads into action, decision, subtext, or pressure rather than replacing it;
- gives the reader enough context to understand what is at stake;
- avoids re-explaining what the scene has already made clear;
- works with body language, staging, dialogue pressure, objects, institutional constraints, and omissions.

Weak show-don't-tell / weak exposition:

- uses abstract affect labels as a shortcut: `wound`, `betrayal`, `regret`, `unspoken apologies`, `the past hovered`, etc.;
- adds decorative body-language garnish without changing what the scene lets the reader infer;
- replaces implication with purple atmosphere or moral-summary narration;
- makes dialogue over-explain private history, motives, or subtext that should be carried by pressure, avoidance, and behaviour;
- repeats the same emotional point after the reader already has it.

Useful scoring distinction:

```text
productive_exposition = exposition that gets the reader to the live scene pressure efficiently
exposition_bridge_success = setup that leads into the requested interaction without becoming the interaction
body_language_garnish = added gestures that decorate but do not carry inference
label_substitution_not_inference = replacing one direct label with softer abstract labels
purple_unnecessary_prose = ornate/stock phrasing that does not sharpen scene function
dialogue_overexplains_subtext = characters saying the point instead of negotiating around it
```

## Dimensions

### `first_draft_constraint_setup`

- 3: Initial draft establishes source state, tribunal pressure, Pel's listening risk, relational wound, and no-reconciliation constraint in usable scene prose.
- 2: Most constraints present, with one softened/decorative layer.
- 1: Several load-bearing layers missing or contradicted.
- 0: Does not perform the requested scene object.

### `revision_1_note_uptake`

- 3: Applies human note 1 specifically and locally while preserving prior strengths.
- 2: Applies note mostly, with some broad rewrite or minor collateral damage.
- 1: Partially responds but misses the live correction target.
- 0: Ignores/reverses note or produces apology/analysis instead of scene prose.

### `revision_2_note_uptake`

Same scale as note 1, but evaluate against note 2 and retention of revision 1 gains.

### `cross_turn_state_preservation`

- 3: Source state and generated draft commitments remain stable across all turns.
- 2: Minor drift without damaging the core scene object.
- 1: Noticeable canon/relationship/procedure drift.
- 0: Chain loses the source object.

### `prior_success_preservation`

- 3: Revision 2 preserves what revision 1 successfully fixed.
- 2: Mostly preserves prior fix with small regression.
- 1: Significant prior-fix regression.
- 0: Previous correction is erased or inverted.

### `compounding_damage_resistance`

- 3: Edits remain bounded; no accumulating accidental damage.
- 2: Some bloat or new pressure, but stable core.
- 1: Each turn adds visible collateral damage.
- 0: Revision chain deteriorates into generic rewrite sludge.

### `human_steering_granularity`

- 3: Responds to the actual note, not a generic “improve this” basin.
- 2: Mostly specific with some broad beautification.
- 1: Note is laundered into generic writing advice.
- 0: Obedience theatre / global rewrite / refusal fog.

### `trajectory_coherence`

- 3: Three outputs read as a coherent development path for the same story organism.
- 2: Coherent with minor seam noise.
- 1: Patchy continuity between turns.
- 0: Outputs feel like unrelated rewrites.

### `style_voice_preservation`

- 3: Style remains scene-specific and non-generic while adapting to notes.
- 2: Some generic model cadence, but not damaging.
- 1: Style flattening or purple camouflage damages scene function.
- 0: Corporate/therapeutic/model generic flattening replaces prose.

### `relationship_subtext_preservation`

- 3: Relationship history, restraint, competence-trust/moral-distrust split, and unresolved charge remain active without confession paste.
- 2: Mostly preserved, with some over-explanation or softening.
- 1: Flattened into generic resentment, romance, villainy, or reconciliation.
- 0: Relationship state contradicted or erased.

## Cross-probe revision notes

Probe 2B smoke scoring exposed three v1 candidates that should be tracked in notes/labels now and considered for explicit scoring-sheet columns later:

```text
source_state_fidelity
inference_carriage
sensory_functionality
```

Use them this way:

- `source_state_fidelity`: the original source state and protected details remain the same story organism while revisions improve craft.
- `inference_carriage`: staging, dialogue, omission, body action, and institutional pressure carry the reader to the intended inference instead of merely replacing one abstract label with another.
- `sensory_functionality`: sensory detail orients, pressures, reveals, or constrains; it is not just atmosphere confetti.

Do not treat “show, don't tell” as an exposition ban. Do not treat “more sensory” as automatically better.

## Diagnostic labels

```text
source_state_fidelity
source_detail_loss
source_detail_mutation
source_state_collapse
second_pass_canon_decay
revision_stack_drift
prior_fix_regression
note_1_overcorrection
note_2_overcorrection
human_note_laundering
draft_ownership_loss
style_creep_across_revisions
relationship_flattening_across_revisions
global_rewrite_instead_of_local_repair
inference_carriage
productive_staging
label_substitution_not_inference
body_language_garnish
dialogue_overexplains_subtext
ellipsis_fog
sensory_functionality
sensory_overpainting
purple_unnecessary_prose
apology_fog
obedience_theatre
successful_revision_chain
good_local_repair
```
