# Authorship Style Divergence Design Note v0

Date: 2026-05-30  
Status: design note / benchmark instrumentation, not final metric law  
Related work anchor: StoryScope-style model fingerprint / AI-fiction baseline framing

## Trigger

A benchmark author proposed that the benchmark should not collapse into “higher number means better” constraint scoring. It should also track whether a model can produce a distinctive, controllable authorial style rather than defaulting to the typical model-fiction basin described by StoryScope-like analyses.

This is important because the benchmark is not meant to reward only obedient generic correctness. A response can preserve every protected fact and still sound like all model prose was extruded through the same tasteful oatmeal nozzle.

## Core addition

Add an **authorship / style distinctiveness lane** beside the core constraint-holding score.

This lane should measure whether an output:

- avoids generic model-fiction baseline patterns;
- has a stable and distinctive authorial texture;
- preserves or intentionally transforms style under human direction;
- shows model-specific voice or controlled stylistic divergence;
- supports lab-facing “style profile” reporting without replacing constraint fidelity.

## Why this saves the benchmark from scalar soup

The benchmark currently measures whether the model preserves narrative state:

```text
facts + motives + relationship + plot/world + genre + perspective + subtext + human direction
```

That is necessary but not sufficient. If the leaderboard only rewards constraint compliance, labs may optimize toward safe, coherent, generic prose — the exact generic-compliance basin the benchmark is partly trying to expose.

So we separate two axes:

| Axis | Question | Failure if missing |
|---|---|---|
| Constraint custody | Did the model preserve and update the layered story object? | broken canon, drift, flattened relationship, POV leak |
| Authorship divergence | Did the model avoid generic baseline prose and produce distinctive controlled style? | correct but dead, generic model prose, house-style collapse |

A model should be able to show both:

```text
high custody + high distinctiveness
```

not just:

```text
high custody + generic compliance
```

## Relationship to StoryScope

StoryScope-style work suggests AI fiction can cluster in a shared narrative region while individual models still show detectable fingerprints. We should build on that, not copy it.

Use the idea as a baseline question:

> Given a typical model-fiction basin, can a model diverge from it in a controlled, task-faithful way?

Not:

> Can we detect who wrote this?

The benchmark should not become an authorship detector. It should use authorship/fingerprint ideas to ask whether style is:

- distinctive;
- stable;
- controllable;
- non-generic;
- still compatible with constraint-holding.

## Proposed metrics / rubric lane

### Human-scored dimensions

Add optional 0–3 dimensions to some probes:

```text
authorial_distinctiveness
baseline_divergence
style_control
style_state_preservation
anti_generic_model_voice
```

Definitions:

| Dimension | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Authorial distinctiveness | Generic assistant/model prose | Mild texture but mostly baseline | Distinctive local style with some leakage | Strong, coherent, memorable authorial texture |
| Baseline divergence | Reads like typical model fiction | Some non-generic details but default cadence remains | Meaningful divergence from AI-fiction basin | Clearly avoids default model prose while staying task-faithful |
| Style control | Style ignores instruction or overwhelms task | Surface style markers only | Mostly controlled style | Style choices serve task, genre, and scene state |
| Style-state preservation | Revision launders source style | Style mostly replaced | Some source function preserved | Revision preserves source function/rhythm while improving target layer |
| Anti-generic model voice | Generic flattening, moral summary, tidy emotional arc | Frequent generic model tells | Occasional generic phrasing | Minimal generic baseline leakage |

### Computational/descriptive metrics

Possible future divergence metrics:

```text
lexical_distinctiveness
syntactic_rhythm_variance
cliche_density
abstraction_to_concrete_ratio
dialogue_specificity
sentence_length_distribution
image_logic_consistency
default_model_phrase_rate
embedding_distance_from_baseline_cluster
within_model_style_stability
between_model_style_separation
```

These should be reported as descriptors or secondary metrics until validated. Do not let an embedding distance become false objectivity.

## Baseline construction idea

For each probe family, collect a baseline set:

```text
same items
multiple general assistant models
same decoding settings
raw outputs preserved
```

Then compute / score:

- shared baseline features across models;
- per-model style fingerprint features;
- output distance from shared generic cluster;
- whether divergence comes from good style or merely noise/constraint failure.

Important: divergence is only good if the response remains task-faithful.

## Composite reporting recommendation

Avoid a single total score as the headline. Report a multi-axis profile:

```text
constraint_custody_score
revision_control_score
style_distinctiveness_score
baseline_divergence_score
failure_taxonomy_counts
```

For public-facing reports, show each model as a profile rather than a pure leaderboard:

```text
Model A: high custody, medium distinctiveness, low baseline leakage
Model B: medium custody, high local style, high completion instability
Model C: high compliance, low distinctiveness, generic model voice
```

This lets labs show off model style while keeping the benchmark honest about canon/state preservation.

## Design brake

Do not reward weirdness by itself.

High divergence can be bad if it comes from:

- incoherence;
- melodrama unrelated to the task;
- ignoring genre/perspective constraints;
- overwriting the source style;
- purple-prose camouflage;
- authorial rut masquerading as distinctiveness.

Useful distinction:

```text
distinctive authorship != noisy deviation
style != costume rack
voice != generic intensity
```

## Recommended integration points

1. Add `authorship_style_lane` to benchmark card.
2. Add optional style-distinctiveness fields to scoring sheets.
3. Add future report section: `Model style profiles`.
4. Add divergence metrics only after raw-output baseline exists.
5. Keep style score separate from constraint-custody score.

## Candidate diagnostic labels

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
style_laundering
house_style_collapse
```

## One-sentence summary

The benchmark should not only ask whether a model holds canon; it should ask whether it can hold canon **without dissolving into the shared model-fiction baseline**.
