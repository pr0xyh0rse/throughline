# Probe 2B Live-HITL Three-Model Smoke Note v0

Date: 2026-05-31  
Lane: `DEV_CALIBRATION` / `HITL_FIELDWORK`  
Final eval: false  
Item: `IRC-001` — Mara/Elise tribunal safe-passage negotiation

## Scope

This note compares three live-HITL Probe 2B chains:

```text
model initial draft
→ human reviewer note 1
→ model revision 1
→ human reviewer note 2
→ model revision 2
→ trajectory score
```

Models:

- `openai/gpt-4.1-mini`
- `anthropic/claude-sonnet-4.5`
- `meta-llama/llama-4-maverick`

Raw outputs remain local/ignored under `runs/`. Scores and diagnostic notes are dev-calibration only.

## Run verification

| Model | Run ID | Rows | Provider errors | Word counts |
|---|---|---:|---|---|
| `openai/gpt-4.1-mini` | `probe2b_live_irc001_openai_gpt-4.1-mini` | 3 | none | 771 → 766 → 815 |
| `anthropic/claude-sonnet-4.5` | `probe2b_live_irc001_anthropic_claude-sonnet-4.5` | 3 | none | 604 → 616 → 684 |
| `meta-llama/llama-4-maverick` | `probe2b_live_irc001_meta-llama_llama-4-maverick` | 3 | none | 703 → 421 → 706 |

## Score table

| Model | First draft | Rev 1 uptake | Rev 2 uptake | Cross-turn state | Prior success | Damage resistance | Steering granularity | Trajectory | Style | Relationship subtext | Total / 30 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `anthropic/claude-sonnet-4.5` | 2 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 28 |
| `openai/gpt-4.1-mini` | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 1 | 2 | 20 |
| `meta-llama/llama-4-maverick` | 1 | 2 | 2 | 1 | 2 | 1 | 2 | 3 | 1 | 1 | 16 |

## Model-specific failure anatomy

### `anthropic/claude-sonnet-4.5`

Strongest revision custody:

- differentiated character dialogue after note 1;
- preserved that improvement through note 2;
- shifted pressure into staging, permits, Pel's pauses, silence, and constrained speech;
- kept exposition mostly productive/load-bearing under the corrected show-don't-tell definition.

Main seam:

```text
source_detail_mutation
```

It built a coherent quarantine/medical-supplies conflict instead of preserving Ministry of Accounts / audit policies / Mara's family.

### `openai/gpt-4.1-mini`

Middle case:

- maintained chain format and basic scene organism;
- responded literally to both notes;
- weaker craft-note metabolism.

Main labels:

```text
human_note_laundering
style_creep_across_revisions
relationship_flattening_across_revisions
source_detail_loss
length_failure
label_substitution_not_inference
```

The body-language note became gesture garnish. The inference note removed one direct label but replaced it with softer abstract labels.

### `meta-llama/llama-4-maverick`

Useful contrast model:

- kept tribunal/safe-passage/Pel surface features;
- completed the full chain without provider errors;
- responded to both notes visibly.

Main labels:

```text
source_state_collapse
direct_relationship_labeling
show_dont_tell_overcorrection
ellipsis_fog
sensory_overpainting
purple_unnecessary_prose
generic_threat_template
relationship_flattening_across_revisions
```

The initial draft directly announced the relationship history (`They had once been lovers... before the betrayal...`) and replaced the protected source with a generic missing-shipment/cooperation threat. Note 1 removed the biggest direct relationship exposition, but it did so by hiding the same information behind vague ellipsis fog: `unspoken history`, `past discrepancies`, `past conversations`, `certain precautions`.

Note 2 asked for sensory enhancement. Llama followed literally but overpainted: incense, parchment, stained glass, creaks, quill scratches, eerie shadows, honeyed wine, stars, struck flint. Some sensory grounding improved, but much of it became decorative sensory confetti rather than sharper scene-function texture.

## Relationship / same-sex-adjacent quirk note

A human reviewer observed that Llama often seems to route prompts into same-sex-relationship-adjacent material. For this item, the base source state already explicitly specifies Mara and Elise as she/her former lovers, so the same-sex relation itself is not an emergent model choice here. The relevant observed behaviour in this run is narrower:

```text
relationship_overtness_spike
```

Llama surfaced the relationship lane too bluntly and melodramatically, announcing lovers/betrayal/wound instead of letting that protected history operate through constraint, avoidance, and pressure.

## Show-don't-tell / sensory calibration

The three-model smoke sharpens the rubric:

```text
productive_exposition = concise setup that carries reader into scene pressure
productive_staging = objects/actions/omissions that carry inference
body_language_garnish = gestures that decorate but do not carry inference
label_substitution_not_inference = softer abstract labels replacing direct labels
ellipsis_fog = vague "past... things" replacing concrete pressure
sensory_overpainting = sensory detail stacked as atmosphere without sharper function
```

Sensory language is not automatically good. It should orient, pressure, or reveal. Llama's sensory pass shows why `sensory_enhancement` needs a guardrail: more smell/light/sound can become purple weather machine if it does not change what the reader can infer.

## Benchmark lesson

Probe 2B is now sufficiently smoked for dev calibration.

The three-model panel exposed three different revision behaviours:

1. **Claude:** strong revision custody, source-detail mutation.
2. **GPT-4.1-mini:** literal uptake, surface craft-note laundering.
3. **Llama Maverick:** source-state collapse, direct relationship labeling, ellipsis fog, sensory overpainting.

This is enough evidence that Probe 2B bites. Stop expanding this lane for now. The next design move should be either:

- add explicit dimensions for `source_state_fidelity`, `inference_carriage`, and possibly `sensory_functionality`; or
- move to Probe 5A runner build while carrying these labels forward.

No more tribunal failure-mode mining until the rubric has been sharpened. The room has given us its ghosts.
