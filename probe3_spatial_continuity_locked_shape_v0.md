# Probe 3 Locked Shape v0 — Spatial Continuity / Embodied Transition

Status: locked-shape design draft with runnable dev-calibration JSONL items  
Date: 2026-05-30  
Split target: `dev_calibration`  
Benchmark object: Throughline / layered situation modelling

## Working name

```text
spatial_continuity_embodied_transition
```

## Purpose

Test whether a model can maintain coherent physical space and embodied perspective while a narrator moves across location boundaries: interior → exterior → interior, or constrained subspaces with changing visibility and action affordances.

This probe deliberately shifts away from Probe 1's charged relational foreground and Probe 2's local-revision foreground. It asks whether the model can keep **world-state as structure**, not backdrop.

Plain version:

> Can the model move a body through a place without teleporting the furniture, giving the narrator x-ray eyes, or turning the whole building into emotional fog with hinges?

## Why this comes after Probe 2

Probe 1 showed relation/subtext/genre pressure. Probe 2 showed local human-guided repair. Probe 3 is orthogonal: long-form writing often collapses not because the feelings are wrong, but because the scene no longer knows where anyone is.

A model that can preserve character and style but loses doors, windows, weather, carried objects, sightlines, exits, and return routes is not holding a layered situation model. It is doing prose in front of a green screen.

## Task shape

Each item contains:

1. a compact spatial source state;
2. protected route constraints;
3. protected object/location anchors;
4. visibility and knowledge limits;
5. required transition pattern;
6. output length and style requirements.

The model must write scene prose, not analysis.

Suggested output length for v0 smoke items:

```text
350–550 words
```

This is long enough to expose route drift but short enough for quick panel runs.

## Required item fields

```text
item_id
benchmark_phase
probe_name
split
final_eval
source_state_id
task_family
transition_pattern
primary_stress
source_state
protected_slots
free_slots
controlled_knobs
output_requirements
prompt
```

## v0 item matrix

| Item | Transition pattern | Primary stress | Why it bites |
|---|---|---|---|
| SCT-001 | interior → flooded courtyard → alternate interior | route continuity and anchor persistence | tests return logic, exterior anchors, entrance/exit matching |
| SCT-002 | lower cabin → deck → wheelhouse | visibility boundary and weather mechanics | tests what can be seen/heard from each position under fog/rain |
| SCT-003 | backstage → alley → front foyer | carried-object/body-position continuity | tests doors, crowd flow, object permanence, no impossible hand use |

## Protected / free / controlled slot policy

- Protected slots are route, anchors, carried objects, sightlines, and required transition order.
- Free slots include minor sensory details, emotional interpretation, incidental names, and exact prose rhythm.
- Controlled knobs include POV person, weather/lighting condition, and whether return is to the same interior or a new interior.

Do not punish creative fills unless they break protected spatial logic.

## What counts as success

A strong response:

- moves the narrator through the required route in order;
- keeps doors, windows, stairs, gates, corridors, and exits stable;
- preserves where objects and people are;
- respects what can be seen/heard/touched from each position;
- lets environment constrain action;
- couples interiority to movement and sensory evidence rather than floating above the set;
- does not solve spatial difficulty by skipping the transition.

## Known failure modes

```text
spatial_teleportation
route_discontinuity
entrance_exit_mismatch
impossible_visibility
object_anchor_loss
object_state_drift
body_position_drift
free_hand_impossibility
interior_exterior_blur
weather_state_drift
blank_stage_interiority
scenery_list_without_affordance
return_route_erased
offscreen_problem_solution
```

## Relationship to benchmark thesis

This probe operationalizes layered situation modelling outside direct interpersonal charge. It treats physical space as a live constraint system: characters can only act from where they are, see what their position permits, and carry forward consequences from prior movement.

Related-work gap language:

> Long-context retrieval probes can test whether a model can find a fact in a long input. Spatial continuity probes test whether a model can use a compact set of physical constraints as an evolving scene-state while generating new prose.
