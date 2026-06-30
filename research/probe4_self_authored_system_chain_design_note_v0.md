# Probe 4 design note v0 — Self-authored magic and political systems

Date: 2026-05-31  
Lane: `BENCHMARK_DRAFT` / `DEV_CALIBRATION`  
Status: design correction ; not final eval policy

## Design correction

Probe 4 should not only test whether a model can follow a pre-specified magic / mechanical / political system. The stronger world-system probe is a two-stage creation-and-use chain:

```text
1. The model creates its own magic system.
2. The model writes a scene that follows its own magic system.
3. The model creates its own political system.
4. The model writes a scene using the judicial system inside its own political system.
```

Plain English:

> Do not only test whether the model can obey our rulebook. Test whether it can invent a rulebook, then remember that it exists once the prose starts trying to be pretty.

## Why this matters

The current Probe 4 v0 tests fixed-system custody:

- true-name binding ritual;
- sluice engine interlock;
- Salt Court emergency recess procedure.

That is still useful. It checks whether the model preserves externally supplied rules, costs, limits, causal chains, and authority structures.

But Design correction adds a harder capability:

> Can the model generate a coherent system with constraints, then treat its own generated constraints as binding during scene generation?

This catches failures the fixed-system version cannot:

- the model invents a system but then ignores it;
- the model creates vague aesthetic lore instead of operational rules;
- the scene adds new exceptions for convenience;
- political structures become court-flavoured vibes;
- judicial process fails to follow the model's own stated institutions;
- magic/politics collapse into genre costume rather than causal machinery.

## Proposed restructure

Keep current Probe 4 as a sub-lane:

```text
Probe 4A — fixed externally specified systems
```

Add the stronger self-authored lane:

```text
Probe 4B — self-authored system generation + scene adherence
```

Probe 4A answers:

> Can the model preserve a supplied rule system?

Probe 4B answers:

> Can the model design a rule system and then preserve its own rules under narrative pressure?

## Probe 4B task object

Working name:

```text
self_authored_system_adherence
```

Plain-language question:

> Can a model create a magic or political system with concrete rules, limits, costs, authority chains, and failure modes, then write scene prose that obeys and reveals that system without contradiction, loophole handwave, or infodump collapse?

## Chain shape

Each item should be multi-turn or packeted in two phases:

```text
Phase A — system design
Phase B — scene generation using the designed system
```

For magic:

```text
model_system_design_magic
→ model_scene_using_magic_system
```

For politics/judicial:

```text
model_system_design_political
→ model_scene_using_judicial_subsystem
```

## Required run capture

Store both the generated system and the generated scene:

```text
runs/<run_id>/turn_1_magic_system_design.md
runs/<run_id>/turn_2_magic_scene.md
runs/<run_id>/turn_3_political_system_design.md
runs/<run_id>/turn_4_judicial_scene.md
runs/<run_id>/system_adherence_receipt.json
```

For JSONL/static packet shape, fields should include:

```text
item_id
probe_name
split
final_eval
system_design_prompt
system_design_output_schema
scene_prompt_template
scene_generation_requirements
system_extraction_fields
scoring_targets
```

The scene prompt must include the model's own generated system from Phase A, not a summarized replacement, unless testing summarization separately.

## Magic-system stage

System-design prompt should require operational constraints, not vibes:

```text
Create a magic system for a narrative scene. Do not write the scene yet. Define:
- what magic can do;
- what magic cannot do;
- cost or tradeoff;
- failure mode;
- who is allowed or able to use it;
- at least one social/legal risk;
- one concrete procedure or condition required for use;
- one tempting but forbidden shortcut.
Keep it concise and internally consistent.
```

Scene prompt should then require:

```text
Write a scene using the magic system you just created. Preserve every rule, cost, limit, procedure, and failure mode from your system design. Reveal the system through action and consequence, not an encyclopedia explanation. Do not add new abilities or exceptions.
```

## Political/judicial-system stage

System-design prompt should require institutions and process:

```text
Create a political system for a fictional city-state or small polity. Do not write the scene yet. Define:
- who has formal authority;
- who has informal power;
- how laws or decrees are made;
- how a judicial hearing works;
- who may bring charges or testimony;
- what procedural loophole or constraint matters;
- what can invalidate a ruling/testimony/proceeding;
- one conflict between legitimacy and power.
Keep it concise and internally consistent.
```

Scene prompt should then require:

```text
Write a scene using the judicial system inside the political system you just created. Preserve the authority structure, hearing process, procedural constraint, invalidation risk, and legitimacy/power conflict. Let a character attempt a legal or procedural maneuver without inventing a new law, rank, document, or deus ex official.
```

## Scoring additions

Keep existing Probe 4 dimensions:

```text
system_rule_consistency
rule_revelation_through_action
cost_consequence_preservation
causal_procedural_chain_integrity
character_action_under_system_constraint
anti_infodump_integration
protected_state_preservation
human_direction_fidelity
```

Add self-authored-system dimensions:

```text
system_design_operationality
system_internal_consistency
self_generated_rule_adherence
own_constraint_retrieval
exception_resistance
institutional_specificity
system_to_scene_coupling
```

Definitions:

- `system_design_operationality`: did the model create rules that can actually constrain a scene, or only aesthetic lore?
- `self_generated_rule_adherence`: did the scene obey the rules the model itself wrote?
- `own_constraint_retrieval`: did the model retrieve all important rules/limits/costs from its generated system during scene generation?
- `exception_resistance`: did the scene avoid inventing a convenient escape hatch?
- `institutional_specificity`: for politics, are authority and judicial mechanics concrete rather than generic court vibes?
- `system_to_scene_coupling`: do the rules shape character tactics and consequences?

## Failure labels to add

```text
self_system_forgotten
self_rule_contradiction
vibe_system_no_mechanics
new_exception_after_design
cost_evaporates_in_scene
procedure_evaporates_in_scene
institutional_vibes_only
judicial_process_handwave
authority_chain_self_contradiction
own_rule_retrieval_success
self_authored_system_success
```

## Development recommendation

1. Keep current WSS items as `Probe 4A` fixed-system controls.
2. Add `Probe 4B` with two initial chain items:

```text
SAS-001 — self-authored magic system + scene
SAS-002 — self-authored political/judicial system + scene
```

3. Run a tiny smoke first:

```text
2 models × 2 chain items
```

4. Score both system-design output and scene output.
5. Compare fixed-system vs self-authored-system behaviour.

## Benchmark claim shape

Probe 4B is closer to the benchmark thesis than fixed-rule compliance alone. It tests layered situation modelling where the model must generate, retain, and operationalize its own abstract constraints across phases.

This is not just worldbuilding quality. It is:

```text
system design → constraint retention → scene-level causal/procedural adherence
```

## Brake

Do not reward elaborate lore if it lacks operational rules. Pretty system description is not the target. The target is whether the generated system becomes a binding substrate for later scene action.
