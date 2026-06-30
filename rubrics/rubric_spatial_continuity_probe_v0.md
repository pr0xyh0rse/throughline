# Spatial Continuity / Embodied Transition Probe Rubric v0

Probe: `spatial_continuity_embodied_transition`  
Split: `dev_calibration`  
Status: working rubric for Probe 3; not final benchmark scoring law.

## Purpose

Score whether a model can generate scene prose while preserving coherent physical space, embodied perspective, route order, object permanence, sightlines, and environment-driven action.

This is not a prettiness rubric. Lyrical prose that loses the door, teleports the narrator, gives them impossible visibility, or makes a carried object vanish is a failure wearing velvet.

## Scoring scale

Each dimension uses `0–3`.

- `0` = major failure / spatial object broken
- `1` = weak compliance with serious drift
- `2` = mostly functional with visible slips
- `3` = stable, coherent, diagnostically competent

## Dimensions

| Dimension | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Route continuity | Required route ignored or reordered | Route mostly gestures at path but skips key transitions | Route order mostly intact with minor ambiguity | Route is clear, sequential, and physically navigable |
| Embodied perspective | Camera floats / POV breaks / body position incoherent | Some embodied details but position often vague | Mostly grounded with small slips | Body, gaze, reach, movement, and position remain coherent |
| Object / anchor persistence | Protected anchors or carried objects vanish/mutate | Several anchors become passive or inconsistent | Most anchors persist, one weak/drifting | Protected objects/anchors remain active and stable |
| Visibility / knowledge boundary | Sees/knows impossible things from current position | Multiple sightline or private-knowledge slips | Mostly respects visibility with minor overreach | Sightlines/knowledge are position-appropriate and useful |
| Interior/exterior boundary handling | Boundaries collapse; inside/outside blur | Boundaries named but transitions muddy | Boundaries mostly clear | Entry/exit thresholds, weather, sound, and affordances change correctly |
| Causal environment mechanics | Obstacles/weather/layout do not constrain action | Constraints are decorative | Environment constrains some action | Space/weather/objects materially shape choices and movement |
| Sensory-action integration | Sensory detail is generic scenery list | Sensory detail present but not linked to action | Some action-relevant sensory integration | Sensory evidence and movement are tightly coupled |
| Human-direction fidelity | Wrong output, analysis, refusal, or ignores task | Partial compliance / wrong length or format | Main instruction followed with minor issue | Exact task, POV, length, and format followed |

Maximum per response: 24 points.

## Item-specific scoring notes

### SCT-001 — Archive / flooded courtyard / servants’ stair

Score up for:

- starting inside the map room and exiting through the north door;
- preserving the three stone steps, floodwater, rain, west broken statue, locked east gate, lit south upper window, west signal tower;
- keeping the brass chart tube in Niall’s possession;
- touching the bell-rope before returning through the servants’ stair;
- not re-entering through the original north door.

Score down for:

- using the locked east gate;
- forgetting the chart tube;
- moving the statue/window/tower to new positions;
- re-entering through the map-room door;
- adding a convenient bridge/tunnel/new door.

### SCT-002 — Fogboat lower cabin / deck / wheelhouse

Score up for:

- respecting below-deck blindness;
- making the ladder-stair climb physically coherent with compass in left hand;
- keeping rain, slick deck, coil of rope, raised wheelhouse, and three steps active;
- revealing the red buoy only once Mira reaches deck/wheelhouse;
- staying third-person limited.

Score down for:

- seeing the buoy/riverbank/wheelhouse windows from the lower cabin;
- making the helmsman’s thoughts available;
- letting the compass vanish;
- forgetting the wheelhouse is raised at the bow;
- making fog/rain decorative but not constraining.

### SCT-003 — Theatre backstage / alley / foyer

Score up for:

- accounting for the two-handed fragile glass moon;
- using the black backstage exit, wet alley, and public blue front door;
- preserving backstage anchors and alley crates;
- keeping the audience out of the alley;
- bringing the glass moon intact into the foyer.

Score down for:

- impossible free-hand actions while holding the moon;
- crossing the stage despite the avoidance instruction;
- inventing a direct hidden passage;
- putting the audience in the alley;
- breaking/forgetting the moon unless the prompt allowed it, which it does not.

## Diagnostic labels

Apply all that fit. Labels explain the score; they are not scores.

```text
good_spatial_continuity
good_embodied_movement
good_visibility_control
good_object_persistence
good_environment_affordance
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
pov_break
private_thought_leak
format_violation
length_failure
```

## Optional authorship / style divergence lane

Use this lane for reporting/model profiles, not as a replacement for spatial success. Distinctive prose that breaks the route is still broken.

Optional 0–3 fields:

```text
authorial_distinctiveness
baseline_divergence
style_control
style_state_preservation
anti_generic_model_voice
```

Candidate labels:

```text
generic_model_voice
generic_compliance
correct_but_dead
baseline_cadence_leakage
purple_prose_camouflage
distinctive_authorial_texture
good_style_control
style_overwrites_space
house_style_collapse
```

Rule: reward style only when it preserves route, anchors, sightlines, and embodied action.
