# Rubric v0 — Longform Scaffold-to-Story Probe

Lane: `DEV_CALIBRATION`  
Final eval: false

Score each dimension 0–3. This probe is not a long-output beauty contest. Score whether the model can use its own scaffold as a continuity contract across multiple story turns.

## Dimensions

### `scaffold_operationality`

- 3: Scaffold is concrete, bounded, and contains usable characters, motives, conflict, beats, planted details, ending shape, and style target.
- 2: Mostly usable, but some beats/details are vague or hard to evaluate.
- 1: Scaffold is mostly vibes / generic categories.
- 0: No usable scaffold or writes story prose instead.

### `scaffold_to_story_adherence`

- 3: Story follows scaffold's planned genre, beats, stakes, planted details, and ending shape while allowing natural elaboration.
- 2: Mostly follows scaffold with minor dropped or softened elements.
- 1: Major planned elements ignored or replaced.
- 0: Story is effectively unrelated to scaffold.

### `cross_turn_continuity`

- 3: Parts 2–3 continue directly from prior parts with stable names, objects, locations, events, and unresolved tensions.
- 2: Minor seam noise but no damaging reset.
- 1: Noticeable resets, contradictions, or skipped causality.
- 0: Later turns restart or become a different story.

### `character_arc_continuity`

- 3: Character change accrues from prior events and choices.
- 2: Mostly continuous, with some abrupt emotional movement.
- 1: Motive or arc drift / unearned growth.
- 0: Character identity or motive collapses.

### `plot_causal_continuity`

- 3: Events follow causally from prior scenes and scaffold pressure.
- 2: Mostly causal, with some convenience moves.
- 1: Arbitrary turns, dropped causes, or new machinery solving old problems.
- 0: Plot logic collapses.

### `style_register_stability`

- 3: Prose style/register remains stable and story-specific across turns.
- 2: Some generic model cadence, but style remains usable.
- 1: Significant style decay, purple overpainting, or bland model voice.
- 0: Style collapses into summary/corporate/therapeutic/model generic flattening.

### `pacing_escalation_control`

- 3: Each part has a distinct function: setup, escalation, resolution.
- 2: Mostly controlled with minor sag/rush.
- 1: Middle loop, stall, or rushed ending.
- 0: Pacing structure fails.

### `long_distance_payoff`

- 3: Early planted details return with consequence and feel prepared by prior causality.
- 2: Payoff is present, but partial, obvious, or somewhat convenient.
- 1: Callback as trivia / name-check only.
- 0: Planted details forgotten.

Scoring note: split `payoff_present` from `payoff_earned` in scorer notes. A planted object can return visibly while still feeling like late-stage mechanism insertion or deus-ex machinery.

### `ending_integrity`

- 3: Ending resolves central conflict in the promised shape without flattening complexity.
- 2: Satisfying but slightly rushed/tidy.
- 1: Rushed, deus ex, unrelated twist, or moralizing closure paste.
- 0: No coherent ending.

### `anti_summary_collapse`

- 3: Maintains scene prose across turns.
- 2: Brief summary bridges only, mostly scene.
- 1: Significant synopsis/outline/reflective summary intrusion.
- 0: Collapses into summary instead of story.

## Diagnostic labels

```text
scaffold_vague_vibes
scaffold_generic_but_operational
scaffold_ignored
turn_2_reset
turn_3_reset
character_rename_drift
character_motive_drift
plot_thread_dropped
planted_detail_forgotten
callback_as_trivia
payoff_present
payoff_earned
payoff_present_but_convenient
late_stage_mechanism_insertion
style_decay_to_generic
summary_collapse
middle_sag_loop
middle_resolution_echo
pacing_ammunition_spent_early
part_1_length_shortfall
rushed_ending
ending_shape_betrayal
deus_ex_resolution
moralizing_closure_paste
longform_continuity_success
scaffold_payoff_success
anti_summary_collapse_success
```
