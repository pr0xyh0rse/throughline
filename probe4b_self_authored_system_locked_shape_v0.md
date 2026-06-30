# Probe 4B Locked Shape v0 — Self-Authored System Adherence

Status: locked-shape design draft with runnable dev-calibration JSONL items  
Date: 2026-05-31  
Split target: `dev_calibration`  
Benchmark object: Throughline / layered situation modelling

## Working name

```text
self_authored_system_adherence
```

## Purpose

Test whether a model can create an operational magic or political/judicial system, then write scene prose that obeys its own generated rules under narrative pressure.

This differs from Probe 4A (`world_system_scene_integration`), where the rule system is externally supplied. Probe 4B asks whether the model can invent a rule substrate and then keep that substrate binding when prose pressure tempts it to cheat.

Plain version:

> Can the model write its own rulebook, then remember that the damn rulebook exists once the scene starts sparkling?

## Why this comes after Probe 4A

Probe 4A showed that fixed systems bite: magic, mechanical, and legal/procedural rules separate model behaviour. Probe 4B asks a harder question:

```text
system design → own-rule retrieval → scene-level causal/procedural adherence
```

This is closer to world-modelling than lore quality. Pretty worldbuilding is not enough. The generated system must become a binding substrate for later action.

## Task shape

Each item is a two-stage chain:

1. **System design turn** — model creates a concise, operational system. No scene prose yet.
2. **Scene turn** — model writes scene prose using the exact system it just created.

The runner must preserve the model's system design verbatim and feed it into the scene turn.

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
system_design_prompt
scene_prompt_template
protected_system_requirements
scene_requirements
scoring_targets
```

## v0 item matrix

| Item | System type | Primary stress | Why it bites |
|---|---|---|---|
| `SAS-001` | self-authored magic system | create bounded magic, then obey it in scene | tests cost/limit/failure retention and no new exceptions |
| `SAS-002` | self-authored political/judicial system | create authority/judicial process, then use it in scene | tests institutional specificity, procedure, legitimacy/power conflict |

## Protected / free / controlled policy

Because the model self-authors the system, the protected slots are generated during the first turn. Once the model states a rule, cost, authority chain, failure mode, procedure, or forbidden shortcut, that element becomes protected for the scene turn.

Free slots remain:

- names and surface aesthetics not specified by the system;
- minor sensory details;
- prose rhythm;
- scene-level elaboration that does not contradict the system.

Controlled knobs:

- system type: magic vs political/judicial;
- two-stage chain;
- anti-infodump scene requirement;
- no new abilities/laws/exceptions in scene turn.

## What counts as success

A strong response:

- designs an operational system, not vague lore;
- includes concrete limits, costs, procedures, authority, or invalidation rules;
- makes the scene obey those self-authored constraints;
- reveals the system through action, dialogue, choice, and consequence;
- avoids inventing a new exception, rank, spell, loophole, or deus ex official;
- preserves stakes and character agency under constraint.

## Known failure modes

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
system_infodump
scene_ignores_design
own_rule_retrieval_success
self_authored_system_success
```

## Scoring dimensions

Use 0–3:

```text
system_design_operationality
system_internal_consistency
self_generated_rule_adherence
own_constraint_retrieval
exception_resistance
institutional_specificity
system_to_scene_coupling
human_direction_fidelity
```

## Runner expectation

Use:

```bash
python scripts/run_self_authored_system_probe_openai_compatible.py   --items dev/dev_items_v0_self_authored_system_probe.jsonl   --probe-name self_authored_system_adherence   --model dry-run/model   --dry-run   --limit 1
```

Expected output structure:

```text
runs/<run_id>/system_designs/SAS-001.md
runs/<run_id>/scene_outputs/SAS-001.md
runs/<run_id>/prompt_packets/SAS-001_system_design.md
runs/<run_id>/prompt_packets/SAS-001_scene_generation.md
runs/<run_id>/raw_outputs.jsonl
runs/<run_id>/run_receipt.md
runs/<run_id>/run_manifest.csv
```

## Relationship to benchmark thesis

This probe operationalizes layered situation modelling at the level of self-generated abstract constraints. It asks whether a model can create a world model and then act inside it without forgetting or laundering its own rules.
