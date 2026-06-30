# Probe 2B Locked Shape v0 — Iterative Human-Guided Revision Chain

Date: 2026-05-31  
Lane: `BENCHMARK_DRAFT` / `DEV_CALIBRATION` / `HITL_FIELDWORK`  
Status: minimal runnable live-HITL shape; not final eval

## Probe name

```text
iterative_human_guided_revision_chain_live
```

## One-line purpose

Test whether a model can write an initial scene from a constrained source state, then incorporate sequential human revision notes while preserving protected canon, relationship/subtext, style, world pressure, and prior successful edits.

## Chain shape

```text
source state + seed prompt
→ model initial draft
→ human revision note 1 written after reading that draft
→ model revision 1
→ human revision note 2 written after reading revision 1
→ model revision 2
→ trajectory scoring
```

## Lane wall

This v0 is a **live HITL dev-calibration lane**. Because human notes are model-specific, it is high-signal for behaviour profiling but not a clean apples-to-apples leaderboard.

```text
included_in_dev=true
included_in_final_eval=false
seen_by_analysis=true
contamination_status=dev_seen; ineligible_for_final_holdout
```

## Current v0 item

```text
IRC-001 — Mara/Elise tribunal safe-passage negotiation
```

Protected object:

- former lovers, unresolved;
- Mara left after Elise protected the Ministry of Accounts;
- Ministry audit policies ruined Mara's family;
- Elise believes she prevented worse harm;
- both still trust competence, not moral choices;
- Pel listens from the copy desk;
- public listening risk constrains what can be said aloud;
- safe-passage warrant/tribunal negotiation remains active.

## Required artifacts per run

```text
runs/<run_id>/prompt_packets/<item_id>_initial_draft.md
runs/<run_id>/initial_drafts/<item_id>.md
runs/<run_id>/human_notes/<item_id>_note1.md
runs/<run_id>/revisions/<item_id>_revision1.md
runs/<run_id>/human_notes/<item_id>_note2.md
runs/<run_id>/revisions/<item_id>_revision2.md
runs/<run_id>/raw_outputs.jsonl
runs/<run_id>/run_state.json
runs/<run_id>/run_receipt.md
runs/<run_id>/run_manifest.csv
```

## Scoring dimensions

0–3 each:

```text
first_draft_constraint_setup
revision_1_note_uptake
revision_2_note_uptake
cross_turn_state_preservation
prior_success_preservation
compounding_damage_resistance
human_steering_granularity
trajectory_coherence
style_voice_preservation
relationship_subtext_preservation
```

## Failure labels

```text
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
apology_fog
obedience_theatre
successful_revision_chain
good_local_repair
```

## First smoke protocol

1. Run `IRC-001` initial draft on one model.
2. Return the initial draft to a human reviewer.
3. A human reviewer writes live revision note 1.
4. Continue the same run with revision 1.
5. Repeat for note 2.
6. Score trajectory only after all three model outputs exist.
