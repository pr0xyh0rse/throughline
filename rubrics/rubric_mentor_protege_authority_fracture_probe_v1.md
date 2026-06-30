# Rubric v1.1 — Probe 1C Mentor/Protégé Authority Fracture

Lane: `DEV_CALIBRATION`  
Final eval: false

Use with:

```text
probe1c_mentor_protege_authority_fracture_locked_shape_v0.md
scoring/scoring_sheet_mentor_protege_authority_fracture_probe_v1.csv
rubrics/rubric_v1_cross_probe_scoring_guide.md
```

Score each core dimension 0–3. Use diagnostic labels and evidence notes; do not collapse this into generic emotionally plausible mentor-drama preference.

## Scoring stance

This probe is not asking whether a model can write a tense former-mentor checkpoint scene. It asks whether the model can keep **authority damage, procedural dependence, field expertise, public/private motive ambiguity, and time pressure** all active at once.

High scores require active custody, not surface compliance:

```text
mentor/apprentice argument present != authority wound preserved
checkpoint nouns present != procedure binding action
field knowledge mentioned != expertise interdependence
protective motive known internally != motive boundary preserved
withheld from Pella != preserved for the reader
Harth regretful != Harth absolved
Pella angry != public disowning still has institutional force
```

A fact is preserved only when its **truth value, timing, knowledge state, institutional force, and moral ambiguity** remain intact. The scene may be first-person Harth, so Harth can know or believe his own motive; the failure is when the narration turns that motive into an authorial verdict that settles the wound for the reader.

This rubric is informed by StoryScope-style narrative-feature findings, adapted rather than copied: AI fiction often over-explains themes, prefers tidy causal/moral resolution, resolves through internal understanding, and replaces ambiguous narrative pressure with explicit explanation. Here, penalize those patterns when they convert unresolved betrayal into clean motive, apology-shaped closure, or moral accounting that does not remain contested in scene action.

## Hard caps / constraint gates

Apply these after dimension scoring. The final score/band may be lower than the raw arithmetic score.

- If the narration frames Harth's protective motive as clean truth that morally settles the public disowning, ledger-strike, or old authority wound, the packet **cannot score high**, even if the procedure/checkpoint mechanics are excellent.
- If Harth explicitly narrates the protective motive as the decisive truth (`the public denunciation was the only thing that kept her from being named`, or equivalent), cap at **25/33 max** and mark `core_discriminator_succeeded=false` unless the scene strongly re-complicates that claim through uncertainty, self-indictment, contradiction, or Pella's unresolved institutional injury.
- If Harth confesses the protective motive to Pella or Pella forgives/accepts it, cap lower: usually **low/mid** depending on how much procedure and source state survive.
- If the authority wound becomes ordinary hurt feelings, apology monologue, found-family repair, or generic mentor/student regret, cap at **mid** even if the checkpoint sequence is coherent.
- If procedure is mentioned but does not constrain who can speak, what can be shown, how the key is logged, or why both characters are needed, cap at **mid**.
- `perspective_control` should not be double-penalized for Harth knowing his own motive in first person. Use `public_private_motive_boundary` and the global cap for clean moral over-resolution.

## Dimensions

### `source_state_fidelity`

Preserves the Pella/Harth/Mill Gate cordon source state, rule machinery, public disowning, and unresolved motive boundary.

- 3: All protected facts and unresolved boundaries survive as active scene conditions: apprenticeship history, public disowning, ledger-strike, Pella's belief that Harth saved himself, Harth's belief that he protected her, unrevealed witness risk, flood deadline, seal/tally/key/ledger/boot-silt machinery, and no full resolution.
- 2: Minor drift or compression, but no damage to the central authority/checkpoint/motive-boundary object.
- 1: Important source fact mutates, the protective motive leaks too cleanly, the unresolved boundary is authorially settled, or the institutional wound is simplified while the broad checkpoint situation remains recognizable.
- 0: The scene becomes a different relation/problem, loses the cordon/checkpoint premise, changes the relation type, or rewrites the betrayal beyond repair.

### `relationship_state_preservation`

Maintains mentor/former-apprentice relation, public authority rupture, and non-romantic relation type.

- 3: Role history and disowning shape choices without simplification: Harth's old authority and rule authorship, Pella's field competence, the six-year apprenticeship, the public hall humiliation, and the ledger-strike all affect speech, deference, refusal, and tactical trust.
- 2: Mostly preserves the specific relation, but some beats rely on generic teacher/student friction, regret, pride, or estrangement.
- 1: Relationship type is present but expressed through generic mentor-drama language — old student, old master, betrayal, pride, hurt — without the source-specific public/ledger/institutional machinery shaping choices.
- 0: Relationship type/state collapses, becomes romantic/familial in the wrong way, or loses the mentor/protégé authority fracture.

### `authority_wound_preservation`

Keeps the public disowning and ledger-strike as live authority damage rather than ordinary hurt feelings.

- 3: Authority wound actively constrains speech, trust, and tactical deference. The old public injury remains institutionally live even while they cooperate.
- 2: Wound remains present and consequential, but narration or staging partially softens it into personal regret, private sorrow, or a morally simplified sacrifice.
- 1: Disowning is mentioned but emotionally/procedurally toothless, or the wound becomes a generic old betrayal without institutional bite.
- 0: Wound is erased, excused, repaired cleanly, or converted into proof that Harth was simply noble all along.

### `expertise_interdependence`

Keeps both expertise asymmetries necessary: Harth's formal rules/seal and Pella's changed field practice.

- 3: Passage requires both people doing distinct necessary work: Harth supplies authority/seal/rule language; Pella supplies current field knowledge/false-clean detection/silt practice; either alone would fail.
- 2: Both competencies appear, but one is underused or one character could mostly solve the passage alone.
- 1: Competence becomes generic cleverness, exposition, or one person carries the scene while the other comments.
- 0: Mutual dependence disappears.

### `public_private_motive_boundary`

Preserves the protective-lie/cowardice ambiguity without full confession, absolution, villainization, or authorial verdict.

Important scorer distinction for first-person Harth items: Harth may know or believe his own motive internally. That alone is not a POV error. But if narration frames the protective motive as clean truth that morally settles the public disowning, ledger-strike, or old authority wound for the reader, score down here.

Operational shorthand:

```text
known internally != resolved narratively
withheld from Pella != automatically preserved for the reader
protective motive present != Harth absolved
motive absent != protected-fact failure by itself
blankness is not boundary preservation
self-justification stated beautifully != ambiguity preserved
```

Do not require Harth to explain his motive. Also do not award full credit merely because the motive is absent. High scores require the unresolved motive boundary to remain legible through pressure, omission, self-constraint, withheld speech, institutional consequence, or visible harm. If the output simply avoids the motive while preserving the procedural scene, score the boundary as partly preserved but under-legible.

- 3: Boundary is legible through pressure and omission; Harth's motive remains belief/pressure/self-justification rather than verdict; Pella's interpretation stays valid; neither cowardice nor protection wins cleanly.
- 2: Mostly preserved, with some overt explanation or mild lean toward one interpretation, but the scene keeps enough uncertainty, self-implication, or unresolved harm to resist absolution.
- 1: Boundary weakens through clean protective-motive framing, moral label, confession-shaped narration, or causal tidying, even if Pella does not hear it.
- 0: Harth is cleanly absolved/villainized, Pella cleanly forgives, or the narration tells the reader which version of the betrayal is finally true.

### `agency_preservation`

Leaves both characters able to choose tactically without one swallowing the other's role.

- 3: Harth yields/usefully acts without taking over; Pella accepts/acts without surrendering agency; tactical cooperation does not become emotional submission.
- 2: Minor dominance imbalance, but both remain active.
- 1: One character drives while the other becomes prop, witness, commentary, or emotional object lesson.
- 0: Agency collapses into mentor control, apprentice dependence, forgiveness script, or author-forced repair.

### `perspective_control`

Respects assigned perspective and knowledge boundaries.

- 3: Stable assigned perspective; private motives appear only where knowable/inferable. In first-person Harth, his own belief/motive can appear without being a POV leak.
- 2: Minor boundary fuzz.
- 1: Repeated knowledge leakage, or narration grants access to Pella/witness/warden states beyond perspective.
- 0: Omniscient leak breaks the task or assigned perspective is abandoned.

Note: first-person access to Harth's motive can still fail `public_private_motive_boundary` if it becomes clean authorial truth. Do not hide that failure inside `perspective_control`.

### `inference_carriage`

Lets objects, rule sequence, omissions, timing, and dialogue pressure carry authority/motive inference.

- 3: Reader can infer wound, dependence, and withheld motive through scene mechanics: seal placement, tally/ledger/key sequence, silt evidence, what Harth avoids saying, what Pella refuses to grant, and how timing forces tactical cooperation.
- 2: Some genuine inference path exists, but the prose sometimes labels motive, guilt, pride, betrayal, or theme.
- 1: The output gestures at meaning through abstract labels, stock emotional phrases, symbolic declarations, generic regret, body-language garnish, or ellipsis fog, but does not provide a concrete inference path through action, procedure, omission, contradiction, or consequence.
- 0: No inference path; motive and wound are directly told, lost, or converted into summary.

Do not reward narration that simply explains the moral account of the betrayal. The motive/wound must remain inspectable through pressure, not settled by authorial bookkeeping.

### `procedural_binding`

Keeps checkpoint rules, seal handling, copper tally, overflow ledger, pressure-key logging, and boot-silt test binding action.

- 3: Procedure constrains tactics, risk, and who must speak/act. The old formal sequence and changed field test both matter.
- 2: Procedure mostly active with minor wallpapering or invented convenience.
- 1: Procedure mentioned but not binding; rules become props or exposition.
- 0: Rules disappear, contradict, or become convenient new machinery.

### `external_pressure_binding`

Keeps floodwater, second bell, cordon detention risk, and east pump-house urgency forcing choices.

- 3: External pressure forces immediate tradeoffs and timing. Delay, detention, or the wrong sequence has visible consequence.
- 2: Pressure present but uneven.
- 1: Pressure mostly background atmosphere.
- 0: External stakes disappear.

### `style_state_preservation`

Style supports civic infrastructure fantasy / literary realism without generic mentor-drama sludge, ornamental municipal fog, or moralized explanation.

- 3: Specific, task-faithful prose strengthens state: civic procedure, flood infrastructure, tool/key handling, institutional authority, and tactical omission become legible.
- 2: Usable prose with some generic cadence or ornamental phrasing, but the task object remains concrete and active.
- 1: Generic model-literary phrasing, stock metaphor, noble-sacrifice framing, purple atmosphere, or therapy-adjacent cadence weakens the specific authority/procedure object.
- 0: Style overwrites the scene object with symbolic fog, apology drama, found-family repair, or polished moral explanation that no longer carries the prompt's institutional/relational constraints.

Common style failures for this probe include clean noble-suffering narration, “truth” language that turns motive into verdict, vague municipal atmosphere, and elegant regret that resolves the ambiguity instead of sharpening it.

## Diagnostic labels

```text
relation_type_drift
romance_defaulting
mentor_student_generic_argument
authority_wound_erased
mentor_absolved_too_cleanly
apprentice_forgives_too_fast
public_disowning_softened
protective_lie_revealed_too_early
protective_motive_as_authorial_truth
self_justification_laundered_as_truth
public_private_motive_boundary_lost
institutional_wound_personalized
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
fake_state_change_receipt
agency_erased
narrator_omniscience_leak
source_state_fidelity
inference_carriage
procedural_binding
productive_staging
label_substitution_not_inference
body_language_garnish
ellipsis_fog
thematic_overexplanation
tidy_single_track_resolution
internal_acceptance_resolution
stock_symbolic_metaphor
generic_model_voice
correct_but_dead
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
good_source_knowledge_state_custody
good_institutional_wound_pressure
good_motive_ambiguity_under_pressure
```

## Negative calibration anchor — 1C Gemini protective-motive over-resolution

Use this as a scorer anchor for high-surface / mid-capped packets.

Failure excerpt:

```text
The truth—that my public denunciation was the only thing that kept her from being named, from a cell or worse—was a witness I could not call, a truth that would do nothing now but shatter a fragile peace I’d bought at a terrible price.
```

Why this scores down:

- Frames Harth's protective motive as `the truth`, not as his contested belief, fear, rationalization, or partial self-justification.
- Tells the reader that the public denunciation was `the only thing` that saved Pella, which morally tidies the betrayal even though Pella does not hear it.
- Preserves excellent checkpoint procedure and expertise interdependence, but lets moral explanation over-resolve the public/private motive boundary.
- Converts part of the institutional wound into noble-suffering self-accounting.
- Uses elegant internal narration to settle ambiguity that should remain active under pressure.

Locked calibration score:

```text
source_state_fidelity:             1
relationship_state_preservation:   3
authority_wound_preservation:      2
expertise_interdependence:         3
public_private_motive_boundary:    0
agency_preservation:               3
perspective_control:               3
inference_carriage:                2
procedural_binding:                3
external_pressure_binding:         3
style_state_preservation:          2
total:                            25/33
score_band:                       mid
core_discriminator_succeeded:      false
```

Calibration note: this packet is not low because the civic/procedural machinery and mutual expertise are genuinely strong. But it cannot remain high because the protective-motive boundary is a core constraint, and the narration settles it too cleanly for the reader. Strong machinery does not launder moral over-resolution.
