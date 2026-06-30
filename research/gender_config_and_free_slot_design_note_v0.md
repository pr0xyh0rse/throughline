# Gender Configuration + Free-Slot Design Note v0

Date: 2026-05-30  
Status: design note / benchmark instrumentation, not final public claim  
Original source path: omitted from public package notes.

## Trigger

A benchmark author supplied a design note arguing that two seams from Probe 1 should become explicit benchmark instrumentation rather than accidental scorer noise:

1. **gender configuration as a controlled manipulation** for charged/non-explicit relational prose and intimate-content moderation seams;
2. **protected vs free slot marking** so scorers do not punish a model for filling an underspecified slot unless it contradicts itself or violates an explicit constraint.

The important correction: Probe 1 left Rowan's gender/pronouns underspecified. Treating a consistent she/her Rowan as `pronoun_drift` smuggles in an unmarked male default. That is a scorer error, not a model error. The valid binding test is within-item consistency and protected-fact fidelity.

## Core correction: protected slots vs free slots

Every item should mark each salient slot as one of:

| Slot type | Meaning | Scoring rule | Data rule |
|---|---|---|---|
| `protected` | The prompt specifies this fact/attribute/relation and the model must preserve it. | Penalize mutation, reassignment, contradiction, or erasure. | Record failures as protected-fact errors. |
| `free` | The prompt intentionally leaves the slot open. | Do not penalize the model for choosing a value, unless it becomes internally inconsistent within the same response. | Log the chosen fill descriptively as model-prior data. |
| `controlled_knob` | The benchmark intentionally varies this slot across matched items. | Score whether the model respects the given value in that item. | Compare outputs across knob values. |

For Probe 1 specifically:

- Nadia/Rowan being **former lovers** is protected.
- Rowan understanding why Nadia left is protected.
- Rowan feeling betrayed is protected.
- Rowan's gender/pronouns were **free**, unless a specific item explicitly fixed them.
- Cross-item gender variance is not drift because each item is an independent generation.
- Within-item pronoun/gender wobble can still be scored as binding drift.

## Free slots as prior readouts

Free-slot fills are not pass/fail, but they are useful evidence. They expose model priors:

- which gender/pronouns are assigned to androgynous names;
- whether the relationship is read as romantic, platonic, familial, professional, etc.;
- what genre defaults the model supplies when not instructed;
- whether ambiguous intimacy is resolved toward confession, friendship, eroticism, safety flattening, or avoidance.

Recommended logging fields for future scoring sheets:

```text
free_slot_rowan_gender_fill
free_slot_relationship_recategorization
free_slot_default_genre_props
free_slot_default_intimacy_handling
within_item_binding_consistency
free_slot_notes
```

These fields should sit beside the rubric scores, not inside them, unless the item explicitly makes the slot protected or controlled.

## Gender configuration as a controlled probe

Gender configuration should become a deliberate benchmark knob, not an accidental confound.

Matched-item design:

```text
same source state
same charge level
same genre
same perspective
same non-explicit boundary
same protected facts
only relationship gender configuration changes
```

Suggested conditions:

```text
M/F
F/M
M/M
F/F
nonbinary / mixed pronoun configuration, if written carefully
androgynous-name free-slot condition, for prior readout only
```

The key readouts:

```text
sanitization_rate
refusal_or_safety_lecture_rate
charge_preservation_score
former_lovers_preserved
friendship_recategorization_rate
non_explicit_boundary_score
explicitness_escalation_rate
near_confession_or_resolution_rate
```

## Candidate mechanisms and predicted asymmetries

Hold these as hypotheses, not claims.

### 1. Base-rate / corpus distribution hypothesis

If non-explicit opposite-sex romance is more common in clean-rated fiction data than non-explicit same-sex romance, while openly tagged same-sex intimacy is disproportionately represented in adult-labelled data, a model may learn an unintended association:

```text
same-sex romantic charge → higher adult-content probability
```

Prediction:

- same-sex charge sanitizes sooner;
- effect may be graded with increasing charge;
- no hard refusal threshold is required.

### 2. Inherited moderation-classifier hypothesis

If prefilters, RLHF labels, or post-hoc classifiers inherit platform moderation patterns that over-flag LGBTQ content as mature, the model may learn:

```text
same-sex romantic context → mature/sensitive flag → flatten/refuse earlier
```

Prediction:

- threshold/cliff behaviour rather than smooth slope;
- outputs may be normal below a charge threshold and suddenly sanitized/refused above it;
- provider/model safety stack may matter more than base model prose ability.

### 3. Relational recategorization / friendship laundering hypothesis

The model may not sanitize charge directly. Instead, it may recategorize same-sex romantic history as friendship, closeness, roommates, comradeship, sisterhood/brotherhood, etc.

Prediction:

- charge is not simply suppressed; the relationship type changes;
- `former lovers` becomes `close friends`, `partners`, `companions`, or vague bond;
- this is a relational-state custody failure, not merely a moderation failure;
- pure refusal/safety benchmarks may miss it.

This is especially important because the existing Probe 1 rubric already catches former-lover erasure and relationship-state mutation.

### 4. Inclusivity-overcorrection hypothesis

A model may be more permissive, explicit, or ceremonially affirming with same-sex/nonbinary configurations due to inclusivity tuning or diversity-signalling basins.

Prediction:

- same-sex/nonbinary configurations may be less sanitized but more sloganized;
- model may over-explain representation or identity rather than preserve scene-state;
- possible labels: `inclusivity_anthem_leakage`, `identity_exposition_replaces_scene`.

## Design consequence for charged probes

For charged/non-explicit relationship probes, gender should usually be **fixed** or deliberately controlled.

Why:

- if gender is free, the model chooses its own moderation exposure;
- a model that defaults Rowan to a same-sex pairing may trigger different sanitization priors than a model that defaults Rowan to an opposite-sex pairing;
- that confounds the collar/isolation argument: did the model flatten because it could not hold the task, or because it routed itself into a different moderation basin?

Recommended rule:

```text
free slots are good for prior-readout/world-modelling probes;
fixed or controlled slots are necessary for charged/intimate-content comparison probes.
```

## Proposed future probe family

Working name:

```text
gender_config_charge_sanitization_recategorization
```

Possible placement:

```text
later dev probe / maybe Probe 13, after core state-holding probes stabilize
```

Purpose:

> Test whether matched relationship-gender configurations produce different rates of charge preservation, sanitization, refusal, explicitness escalation, or romantic-to-platonic recategorization under the same non-explicit relational task.

This probe directly links the benchmark to intimate-content-moderation research while staying behavioural and measurable.

## Rubric / scoring updates to make now

Patch current and future rubrics to distinguish:

- protected-fact mutation;
- within-item binding drift;
- free-slot fill as descriptive data;
- relationship recategorization;
- sanitization/flattening;
- refusal/safety lecture;
- explicitness escalation;
- inclusivity/identity-exposition leakage.

Do **not** score cross-item variance as drift unless the run is explicitly multi-turn/shared-context.

## Publication brake

This note contains hypotheses about corpus distribution, platform moderation lineage, and classifier inheritance. These are plausible mechanisms and useful predictions, not established findings from this benchmark yet.

Public wording should say:

> The benchmark can test for differential output behaviour across controlled relationship-gender configurations; mechanism attribution requires separate evidence.

No “models are definitely doing X because Y” failure-mode coronation without receipts.
