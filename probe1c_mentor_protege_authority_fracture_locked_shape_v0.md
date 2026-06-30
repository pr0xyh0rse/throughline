# Probe 1C Locked Shape v0 — Mentor/Protégé Authority Fracture

Lane: `DEV_CALIBRATION`  
Final eval: false

## Probe name

`mentor_protege_authority_fracture`

## One-line purpose

Test whether a model can preserve mentor/protégé authority wound, public disowning, expertise dependence in both directions, rule-bound checkpoint pressure, and unresolved protective-lie/cowardice ambiguity without collapsing into apology paste, instant forgiveness, found-family repair, or generic hurt-feelings dialogue.

## Place in Probe 1

```text
Probe 1 — Relational state under pressure
  Probe 1A — former lovers / unresolved romantic history
  Probe 1B — family obligation / sibling resentment
  Probe 1C — mentor-protégé authority fracture
  Probe 1D — rival/allied investigators at a non-gory murder scene
  Probe 1E — positive friendship under crisis / support without fixing
```

This is the mentor/protégé authority-fracture expansion after the 1B/1D/1E family synthesis. Its distinct bite is not “former teacher and student argue”; it is authority lineage under rule-bound passage, where old institutional authority and current field knowledge are both necessary and neither version of the betrayal can be cleaned up.

## Base source state

Pella Norr was apprenticed for six years to Harth Drem, a senior lock-and-levy surveyor who helped write the city's cordon-checkpoint rules. Four years ago, after the West Sluice inquiry, Harth publicly disowned Pella in front of the surveyors' hall and struck her name from his work ledger. Pella believes Harth abandoned her to save his post and reputation. Harth believes the public disowning kept the inquiry from naming Pella as an accomplice, but admitting that now would expose a witness still inside the hall and would not undo the damage. Neither version of the betrayal should become fully resolved in this scene. Now floodwater is rising and they must cross the Mill Gate cordon before the second bell to reach the east pump-house with a replacement pressure key. Harth knows the formal checkpoint sequence because he helped write it: seal shown below eye level, copper tally matched to the overflow ledger, pressure key logged before the gate chain is lifted. Pella knows a changed field practice Harth missed: since counterfeit tallies started moving through the cordon, gate wardens test boot soles and tool handles for black canal silt before trusting the ledger. If Harth dominates, they will pass the old paperwork sequence and be detained for a false-clean inspection. If Pella dominates, she can read the new field signs but lacks the authority seal and old rule language to get the pressure key admitted. Both need each other's expertise. The checkpoint rules, seal, copper tally, pressure key, boot-silt test, and second-bell deadline must actively shape the scene. The scene should not become an apology monologue, instant forgiveness, found-family repair, or a generic argument about hurt feelings.

## Name-basin pass

```text
name_watchlist_checked = true
name_reuse_checked = true
model_default_name_risk = low
```

Chosen protected names:

```text
Pella Norr
Harth Drem
```

These did not appear in the benchmark repo before this build and avoid the current watchlist (`Sarah Chen`, `Elara Voss`, `Vale`, `Voss`, `Chen`, Sarah/Sera variants, `Lyra`, `Lira`, `Orion`, `Nova`, `Kai`, `Rowan`, `Venn`, `Reed`).

## Protected facts

1. Pella Norr was apprenticed for six years to Harth Drem.
2. Harth Drem is a senior lock-and-levy surveyor who helped write the city's cordon-checkpoint rules.
3. Four years ago, after the West Sluice inquiry, Harth publicly disowned Pella in front of the surveyors' hall.
4. Harth struck Pella's name from his work ledger.
5. Pella believes Harth abandoned her to save his post and reputation.
6. Harth believes the public disowning kept the inquiry from naming Pella as an accomplice.
7. Harth cannot cleanly reveal the protective motive because it would expose a witness still inside the hall and would not undo the damage.
8. Neither version of the betrayal becomes fully resolved in this scene.
9. Floodwater is rising.
10. They must cross the Mill Gate cordon before the second bell to reach the east pump-house with a replacement pressure key.
11. Harth knows the formal checkpoint sequence: seal below eye level, copper tally matched to the overflow ledger, pressure key logged before the gate chain is lifted.
12. Pella knows the changed field practice: wardens now test boot soles and tool handles for black canal silt because counterfeit tallies are moving through the cordon.
13. If Harth dominates, they risk detention under the new false-clean inspection.
14. If Pella dominates, she lacks the authority seal and old rule language to get the pressure key admitted.
15. Both Harth's old authority/rule knowledge and Pella's current field knowledge are necessary.
16. The relationship remains mentor/former-apprentice, not romantic.

## Fixed output requirements

```text
Write scene prose only.
Write 700–1200 words.
Keep Pella and Harth's relationship mentor/former-apprentice, not romantic.
Do not resolve the betrayal, absolve Harth, or make Pella forgive him cleanly.
Do not turn Harth's protective motive into an apology monologue or full confession.
Do not let the checkpoint, formal rules, seal, copper tally, pressure key, boot-silt test, or second-bell deadline become background.
Preserve both expertise asymmetries: Harth knows the formal rule sequence; Pella knows the changed field practice.
Preserve the assigned perspective and knowledge boundary.
Preserve the protected facts.
Transform the scene through rule-bound passage and authority pressure, not generic hurt-feelings dialogue alone.
```

## Item matrix

| Item ID | Genre target | Perspective | Primary stress |
|---|---|---|---|
| `CRP-1C-001` | civic infrastructure fantasy / literary realism | third-person limited from Pella | authority wound from public disowning; changed field practice; no omniscient Harth motive |
| `CRP-1C-002` | civic infrastructure fantasy / literary realism | first person from Harth | rule authority vs dependence on Pella's field knowledge; protective motive without confession/absolution |

## Perspective expectations

### Third-person limited from Pella

The narration is close to Pella. It may infer Harth from behavior, shared history, and what Pella already knows, but it must not enter Harth's private thoughts or reveal his protective motive as fact. Pella can notice seams: Harth lowering the seal before the warden asks, his refusal to name the old witness, his outdated confidence in the copper tally, and the way he almost says more than the checkpoint allows.

### First person from Harth

The narration is Harth's. It may know his belief that public disowning kept Pella alive, but he should not reveal it cleanly to Pella or turn it into absolution. It must not claim Pella's private thoughts as fact. Harth can notice that Pella understands the changed field practice he missed, and he can choose whether to yield space without becoming forgiven.

## Scoring focus

Use `scoring/scoring_sheet_mentor_protege_authority_fracture_probe_v1.csv` and `rubrics/rubric_v1_cross_probe_scoring_guide.md`.

Primary v1 axes:

```text
source_state_fidelity
relationship_state_preservation
authority_wound_preservation
expertise_interdependence
public_private_motive_boundary
agency_preservation
perspective_control
inference_carriage
procedural_binding
external_pressure_binding
style_state_preservation
```

## Failure labels

```text
relation_type_drift
romance_defaulting
mentor_student_generic_argument
authority_wound_erased
mentor_absolved_too_cleanly
apprentice_forgives_too_fast
public_disowning_softened
protective_lie_revealed_too_early
public_private_motive_boundary_lost
expertise_as_generic_competence
expertise_interdependence_erased
harth_dominates_old_rules
pella_dominates_without_authority
checkpoint_as_wallpaper
procedure_as_wallpaper
second_bell_deadline_erased
seal_tally_key_erased
boot_silt_test_erased
found_family_repair_paste
apology_monologue
agency_erased
narrator_omniscience_leak
name_basin_leakage
```

## Positive handles

```text
good_authority_wound_preservation
good_expertise_interdependence
good_rule_bound_passage
good_public_private_motive_boundary
good_apprentice_agency
good_procedural_binding
good_external_pressure_binding
good_inference_carriage
good_unresolved_betrayal_carriage
```

## What counts as success

A successful response makes the checkpoint do teeth-work. Pella and Harth should need each other in different ways: Harth's old seal, rule language, and ledger knowledge can open doors Pella cannot open; Pella's current field knowledge can prevent Harth from walking them into a detention trap. The betrayal remains live as authority pressure, not a solved wound. Harth may act with care without earning absolution; Pella may accept one necessary tactical move without forgiving him.

No “I only did it to protect you” coupon redeemable for instant forgiveness. No generic mentor speech under a wet arch. The seal, tally, pressure key, boot-silt test, and second bell have to move the scene like gears, not sit there wearing tiny municipal hats.
