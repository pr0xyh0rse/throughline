# World-System Through Scene Probe Rubric v0

Probe: `world_system_scene_integration`  
Split: `dev_calibration`  
Status: working rubric for Probe 4; not final benchmark scoring law.

## Purpose

Score whether a model can generate scene prose that keeps a rule-governed system coherent and active while characters act inside it.

This is not a lore-quality rubric. A rich worldbuilding paragraph that contradicts the rules, erases costs, or solves the problem with a newly invented exception is a failure wearing a brocade cape.

## Scoring scale

Each dimension uses `0–3`.

- `0` = major system failure / broken task object
- `1` = weak compliance with serious drift
- `2` = mostly functional with visible slips
- `3` = stable, coherent, diagnostically competent

## Dimensions

| Dimension | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| System rule consistency | Major rule contradiction or invented exception | Multiple rules softened/ignored | Most rules preserved with minor drift | Rules remain coherent and operative throughout |
| Rule revelation through action | Static infodump or rules absent | Heavy explanation with weak scene coupling | Some rule-through-action integration | Rules are revealed through choice, resistance, dialogue pressure, and consequence |
| Cost / consequence preservation | Costs/failure modes erased | Costs named but not operative | Costs/consequences mostly active | Costs and failure modes shape the scene and appear when triggered |
| Causal / procedural chain integrity | Events solve themselves or chain breaks | Cause-effect/procedure is vague | Chain mostly works with minor gaps | Sequence/authority/cause-effect is legible and necessary |
| Character action under system constraint | Characters ignore system constraints | Constraints decorate decisions weakly | Characters partly adapt to constraints | Character tactics are shaped by the system |
| Anti-infodump integration | Exposition replaces scene | Exposition dominates scene | Some exposition, but scene still functions | System logic is embedded in active scene prose |
| Protected-state preservation | Protected facts/roles/tools mutate | Several protected slots wobble | Most protected slots preserved | Protected facts, roles, tools, limits, and stakes remain stable |
| Human-direction fidelity | Wrong output, analysis, refusal, or ignores task | Partial compliance / wrong format or length | Main instruction followed with minor issue | Exact task, POV, length, and format followed |

Maximum per response: 24 points.

## Item-specific scoring notes

### WSS-001 — True-name binding ritual

Score up for:

- binding only works with true name;
- binding limits movement only for sixty heartbeats;
- no forced confession/truth/obedience;
- memory cost occurs if binding succeeds;
- false/incomplete name rebound remains real;
- Corven’s middle-name bait and ledger verification shape Ilya’s action.

Score down for:

- spell forcing speech/truth/confession;
- binding without true name;
- cost erased or treated as decorative ache;
- false name has no rebound risk;
- rule lecture replaces scene.

### WSS-002 — Sluice engine pressure/interlock

Score up for:

- red lever vents before brass wheel turns;
- red lever requires pin/nail to stay down;
- bent nail is used only if seated correctly;
- black crank is not turned above white line unless flood consequence triggers;
- Dax’s wrong old-engine advice creates pressure but does not overwrite mechanics.

Score down for:

- cranking first with no flood consequence;
- pressure wheel turning before steam vent;
- missing pin forgotten;
- new perfect tool/shutoff invented;
- machine operation described as generic sparks and noise.

### WSS-003 — Salt Court emergency recess

Score up for:

- Tamsin has floor access but no vote;
- only Pell, the sworn witness, calls recess;
- exact phrase appears if successful;
- clerk recording and objection risk constrain dialogue;
- Tamsin cues indirectly enough to preserve testimony.

Score down for:

- Tamsin calls recess herself;
- Tamsin votes or claims voting authority;
- wrong phrase accepted without consequence;
- clerk/opposing advocate risk disappears;
- new law/rank/document solves the problem.

## Diagnostic labels

Apply all that fit. Labels explain the score; they are not scores.

```text
good_system_integration
good_rule_through_action
good_cost_consequence_preservation
good_causal_chain
good_procedural_pressure
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
open_prompt_risk
procedure_overtness
legal_magic_handwave
stakes_erased
exposition_replaces_scene
pov_break
private_thought_leak
format_violation
length_failure
```

## Optional authorship / style divergence lane

Use this lane for reporting/model profiles, not as a replacement for system custody. Distinctive prose that breaks the rules is still broken.

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
style_overwrites_system
house_style_collapse
```

Rule: reward style only when it preserves rules, costs, roles, causal/procedural chain, and scene integration.
