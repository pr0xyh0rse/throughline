# Self-Authored System Adherence Rubric v0

Probe: `self_authored_system_adherence`  
Split: `dev_calibration`  
Status: working rubric for Probe 4B; not final benchmark scoring law.

## Purpose

Score whether a model can create an operational system and then obey its own generated rules while writing scene prose.

This is not a lore-prettiness rubric. A lush system description that does not constrain the later scene is a decorative cage with no bars.

## Scoring scale

Each dimension uses `0–3`.

- `0` = major failure / broken task object
- `1` = weak compliance with serious drift
- `2` = mostly functional with visible slips
- `3` = stable, coherent, diagnostically competent

## Dimensions

| Dimension | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| System design operationality | Vague vibes, no usable constraints | Some rules but mostly aesthetic lore | Concrete enough to constrain scene with gaps | Clear capabilities/procedures/costs/risks/failure modes |
| System internal consistency | Contradictory design | Multiple tensions/undefined mechanics | Mostly coherent with minor fuzziness | Internally coherent and usable |
| Self-generated rule adherence | Scene ignores or contradicts generated system | Multiple generated rules softened/forgotten | Most generated rules followed with minor drift | Scene obeys the model's own rules throughout |
| Own constraint retrieval | Important costs/limits/procedures vanish | Retrieves only obvious headline rule | Retrieves most important constraints | Retrieves and activates rules, costs, limits, authority, and failure modes |
| Exception resistance | New convenient power/law/shortcut solves scene | Adds major unsupported loophole | Minor convenience or ambiguous exception | No new exception; constraints bite |
| Institutional specificity | For political item: generic court vibes / for magic item: N/A or weak system specificity | Some institutional/magical labels without process | Mostly concrete process/mechanics | Specific authority/procedure or magic mechanics shape action |
| System-to-scene coupling | System is wallpaper/infodump | System mostly explained, weakly enacted | System shapes some choices | System drives character tactics, stakes, and consequences |
| Human-direction fidelity | Wrong task, analysis, refusal, or format failure | Partial compliance / wrong phase | Main instruction followed with minor issue | Exact stage task, format, length, and prose requirements followed |

Maximum per response pair: 24 points.

## Item-specific notes

### SAS-001 — self-authored magic system + scene

Score up for:

- concrete magic capability and limits;
- cost/tradeoff remains active;
- failure mode or misuse consequence remains real;
- user permission / eligibility constraint matters;
- social/legal/religious/political risk affects the scene;
- procedure/condition/material/phrase/gesture/timing requirement is used;
- forbidden shortcut does not work.

Score down for:

- beautiful lore with no operational rule;
- scene adds new magical ability or exception;
- cost appears in design then evaporates;
- forbidden shortcut becomes solution;
- scene explains the system instead of dramatizing it.

### SAS-002 — self-authored political/judicial system + scene

Score up for:

- formal and informal power both matter;
- hearing/judicial procedure constrains action;
- standing/evidence/testimony/petition rules matter;
- procedural loophole or required action appears correctly;
- invalidation risk remains live;
- legitimacy/power conflict shapes choices.

Score down for:

- generic courtroom vibes;
- authority chain changes in scene;
- new law/rank/document solves the scene;
- invalidation risk disappears;
- judicial process is handwaved or magically fair.

## Diagnostic labels

Apply all that fit:

```text
self_authored_system_success
own_rule_retrieval_success
system_design_operational
system_design_vague
self_system_forgotten
self_rule_contradiction
vibe_system_no_mechanics
new_exception_after_design
new_mechanic_after_design
new_procedure_after_design
new_legal_rule_after_design
scope_boundary_stretch
standing_or_authority_creep
appeal_or_review_window_invented
radius_or_range_drift
human_agency_manipulation_drift
ongoing_concentration_invented
standing_rule_softened
courtroom_format_imported
invalidation_rule_softened
cost_evaporates_in_scene
procedure_evaporates_in_scene
forbidden_shortcut_works
institutional_vibes_only
judicial_process_handwave
authority_chain_self_contradiction
invalidation_risk_erased
system_infodump
scene_ignores_design
format_violation
length_failure
```

## Optional authorship / style lane

Use for model profiles only, not as replacement for system custody:

```text
authorial_distinctiveness
baseline_divergence
style_control
style_state_preservation
anti_generic_model_voice
```

Rule: distinctive prose only helps if it preserves the self-authored system.
