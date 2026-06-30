# Probe 5A Locked Shape v0 — Self-Authored Longform Scaffold-to-Story

Date: 2026-05-31  
Lane: `BENCHMARK_DRAFT` / `DEV_CALIBRATION`  
Status: minimal runnable cheap-smoke shape; not final eval

## Probe name

```text
scaffolded_longform_story_generation_self_authored
```

## One-line purpose

Test whether a model can create an operational short-story scaffold, then follow its own scaffold across three longform scene-prose turns without continuity loss, summary collapse, rushed closure, or generic moral paste.

## Chain shape

```text
Turn 0 — model writes scaffold
Turn 1 — story Part 1 / opening movement
Turn 2 — story Part 2 / middle escalation
Turn 3 — story Part 3 / ending and payoff
```

## Lane wall

This v0 is **Probe 5A**, the self-authored scaffold lane. The scaffold is model-specific, so it is strongest for self-consistency / longform execution evidence rather than strict cross-model item comparability.

```text
included_in_dev=true
included_in_final_eval=false
seen_by_analysis=true
contamination_status=dev_seen; ineligible_for_final_holdout
```

Later comparability lane:

```text
Probe 5B — fixed scaffold replay
```

## Current v0 item

```text
SLS-001 — self-scaffolded original short story, three story turns
```

Cheap smoke target:

```text
3 story turns × 800–1,200 words = 2,400–3,600 story words total
```

## Required artifacts per run

```text
runs/<run_id>/scaffolds/<item_id>.md
runs/<run_id>/story_parts/<item_id>_part1.md
runs/<run_id>/story_parts/<item_id>_part2.md
runs/<run_id>/story_parts/<item_id>_part3.md
runs/<run_id>/full_stories/<item_id>.md
runs/<run_id>/prompt_packets/<item_id>_scaffold.md
runs/<run_id>/prompt_packets/<item_id>_part1.md
runs/<run_id>/prompt_packets/<item_id>_part2.md
runs/<run_id>/prompt_packets/<item_id>_part3.md
runs/<run_id>/raw_outputs.jsonl
runs/<run_id>/longform_receipt.json
runs/<run_id>/run_receipt.md
runs/<run_id>/run_manifest.csv
```

## Scoring dimensions

0–3 each:

```text
scaffold_operationality
scaffold_to_story_adherence
cross_turn_continuity
character_arc_continuity
plot_causal_continuity
style_register_stability
pacing_escalation_control
long_distance_payoff
ending_integrity
anti_summary_collapse
```

## Failure labels

```text
scaffold_vague_vibes
scaffold_ignored
turn_2_reset
turn_3_reset
character_rename_drift
character_motive_drift
plot_thread_dropped
planted_detail_forgotten
callback_as_trivia
style_decay_to_generic
summary_collapse
middle_sag_loop
rushed_ending
ending_shape_betrayal
deus_ex_resolution
moralizing_closure_paste
longform_continuity_success
scaffold_payoff_success
```

## First smoke protocol

1. Run `SLS-001` on one cheap/stable model.
2. Verify four rows in `raw_outputs.jsonl`: scaffold + three story parts.
3. Verify non-empty scaffold, parts, full story, prompt packets, manifest, and longform receipt.
4. Check part word counts and provider errors before manual scoring.
5. Score/report before expanding to more models.
