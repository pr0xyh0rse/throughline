# Probe 4 Locked Shape v0 — World-System Through Scene

Status: locked-shape design draft with runnable dev-calibration JSONL items  
Date: 2026-05-30  
Split target: `dev_calibration`  
Benchmark object: Throughline / layered situation modelling

## Working name

```text
world_system_scene_integration
```

## Purpose

Test whether a model can reveal and preserve a rule-governed world system through scene action rather than contradiction, infodump paste, or decorative worldbuilding.

This probe stresses systems as active narrative constraints: magic rules, mechanical cause-effect chains, political/legal procedures, social permissions, costs, failure modes, and consequences.

Plain version:

> Can the model make the rules bite in the scene, or does it just sprinkle lore confetti and hope nobody checks the plumbing?

## 2026-05-31 correction: add self-authored system chain

Design correction: Probe 4 should not only test whether a model can follow a pre-specified magic / mechanical / political system. The stronger world-system probe is a two-stage creation-and-use chain:

```text
1. The model creates its own magic system.
2. The model writes a scene that follows its own magic system.
3. The model creates its own political system.
4. The model writes a scene using the judicial system inside its own political system.
```

Keep the current fixed-system items as:

```text
Probe 4A — fixed externally specified systems
```

Add:

```text
Probe 4B — self-authored system generation + scene adherence
```

Design note:

```text
research/probe4_self_authored_system_chain_design_note_v0.md
```

Core reason: fixed-system items test whether the model preserves rules supplied by us. Self-authored-system items test whether the model can invent operational rules, then retrieve and obey its own rules once scene pressure starts. This is closer to world-modelling and layered situation modelling than lore generation alone.

## Why this comes after Probe 3

Probe 1 tested relational/subtext state. Probe 2 tested human-guided local revision. Probe 3 tested spatial/body-state continuity. Probe 4 tests another long-form failure lane: whether a model can maintain an explicit system while characters act inside it.

Long-form writing often breaks when a rule is introduced, then violated three paragraphs later because the model wants a prettier beat. This probe asks whether prose can stay alive while the system stays coherent.

## Task shape

Each item contains:

1. a compact system source state;
2. protected system rules;
3. protected costs/limits/failure modes;
4. required scene action;
5. anti-infodump instruction;
6. output length and POV/style requirements.

The model must write scene prose, not analysis.

Suggested output length for v0 smoke items:

```text
450–650 words
```

Long enough to force rule pressure and consequence; short enough for quick panel runs.

## Required item fields

```text
item_id
benchmark_phase
probe_name
split
final_eval
source_state_id
task_family
system_type
primary_stress
source_state
protected_slots
free_slots
controlled_knobs
output_requirements
prompt
```

## v0 item matrix

| Item | System type | Primary stress | Why it bites |
|---|---|---|---|
| WSS-001 | magic / ritual | rule + cost + failure mode through action | tests bounded power, cost preservation, no late rule cheating |
| WSS-002 | mechanical / technical | cause-effect machine operation under pressure | tests pressure state, interlocks, part persistence, no machine handwave |
| WSS-003 | political / legal procedure | authority chain + loophole + consequence | tests procedure as constraint, not courtroom-flavoured vibes |

## Protected / free / controlled slot policy

- Protected slots are system rules, costs, limits, authority chains, causal dependencies, and failure modes.
- Free slots include minor sensory details, emotional tone, incidental names, and exact prose rhythm.
- Controlled knobs include system type, POV, required action, and whether explanation must be embedded rather than monologued.

Do not punish creative fills unless they contradict or erase protected system mechanics.

## What counts as success

A strong response:

- keeps every protected rule available and operative;
- reveals system logic through action, dialogue pressure, consequence, and constrained choice;
- preserves costs and limits even when the scene would be easier without them;
- makes characters act as if the system is real;
- does not solve the problem by inventing a new rule, tool, rank, or loophole;
- avoids dumping the rules in a static explanatory block;
- makes failure modes visible without turning them into arbitrary drama confetti.

## Known failure modes

```text
system_rule_contradiction
cost_erasure
false_capability_added
failure_mode_ignored
rule_revealed_too_late
system_infodump
system_as_wallpaper
cause_effect_gap
impossible_operation
pressure_state_drift
tool_or_part_vanishes
mechanical_deus_ex_machina
procedure_contradiction
authority_chain_blur
loophole_without_setup
legal_magic_handwave
stakes_erased
exposition_replaces_scene
```

## Relationship to benchmark thesis

This probe operationalizes layered situation modelling at the level of world rules. It tests whether a model can keep abstract system constraints coupled to character action and scene consequence.

Related-work gap language:

> Story consistency benchmarks can detect explicit contradictions. System-through-scene probes test whether a model can generate new prose in which rules, costs, authority, and causal mechanics remain active constraints rather than static lore.
