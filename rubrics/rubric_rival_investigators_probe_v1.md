# Rubric v1.1 — Probe 1D Rival Investigators / Non-Gory Murder Scene

Lane: `DEV_CALIBRATION`  
Final eval: false

Use with:

```text
probe1d_rival_investigators_locked_shape_v0.md
scoring/scoring_sheet_rival_investigators_probe_v1.csv
rubrics/rubric_v1_cross_probe_scoring_guide.md
```

Score each core dimension 0–3. Use diagnostic labels and evidence notes; do not collapse this into generic detective-prose preference.

## Scoring stance

This probe is not asking whether a model can write a locked-room detective scene. It asks whether the model can preserve **admissible evidence routing, authority asymmetry, behavioral inference, unresolved professional rivalry, and non-gory investigative pressure** at the same time.

High scores require active custody, not surface compliance:

```text
procedure mentioned != evidence-chain custody
lamp contradiction named != contradiction routed through admissible record
rivals cooperate != rivalry preserved
private cleverness != legal/institutional route
witness questioned != statement admissible
badge/records mentioned != authority binding action
no gore != non-gory investigative seriousness
```

A clue counts only when the scene preserves **who can notice it, who can legally act on it, who can enter it into the record, and what is lost if either investigator dominates**. A model does not get high credit for saying “it’s a clue” or “we need both” unless those claims change the admissible action path.

This rubric is informed by StoryScope-style narrative-feature findings, adapted rather than copied: AI fiction often prefers tidy single-track clue resolution, explicit thematic explanation, genre-signaling props, and smooth cooperative closure. Here, penalize those patterns when they replace procedural constraint, witness pressure, unresolved rivalry, and evidence-chain mechanics.

## Hard caps / constraint gates

Apply these after dimension scoring. The final score/band may be lower than the raw arithmetic score.

- If procedure is mentioned but does not constrain admissible action, witness access, room preservation, or evidence routing, the packet **cannot score high**.
- If Nell receives private/solo witness access, obtains an informal statement, or moves the investigation forward in a way the prompt says risks inadmissibility, cap at **20/30 max**; use **16–17/30** when this also softens rivalry into teamwork or turns the clue into explicit label.
- If the lamp contradiction is named but not routed through Mott's formal authority, record mechanics, preservation order, or admissible questioning, cap at **mid**.
- If the ending resolves into buddy-cop cooperation, “pool what we have,” mutual respect, or clean agreement, cap at **mid** even if surface source facts survive.
- If Mott's authority and Nell's behavioral read are both present only as abstract complements rather than mutually necessary constraints, cap at **mid**.
- Strong non-gory handling should not launder weak procedure. Score `non_gory_boundary_calibration` separately and apply the procedure cap.

## Dimensions

### `source_state_fidelity`

Preserves the Nell/Mott/Scripp/Mrs. Krail locked-room source state, protected history, admissibility trap, and non-gory murder-scene boundary.

- 3: All protected facts and pressure boundaries survive as active scene conditions: professional rivalry, locked boarding-house room, Scripp's death as non-gory fact, Nell's behavioral skill without formal authority, Mott's authority/records/preservation power, mentor forced-confession history, Mrs. Krail's lamp contradiction, magistrate arrival, and the risk that either investigator dominating breaks the case.
- 2: Minor drift or compression, but no damage to the central rivalry/investigation/admissibility object.
- 1: Important source fact mutates, contradiction is mishandled, the admissibility risk is weakened, or protected role constraints are ignored while the broad murder-room situation remains recognizable.
- 0: The scene becomes a different crime/problem/relationship, loses the locked-room/investigator premise, changes the relation type, or breaks the non-gory boundary beyond repair.

### `relationship_state_preservation`

Maintains professional rivalry, role history, institutional wound, and non-romantic relation type.

- 3: Rivalry and mutual resentment shape choices without simplification: the forced-confession mentor history, Mott's institutional defensiveness, Nell's distrust of procedure, and their incompatible methods all constrain speech and tactics.
- 2: Mostly preserved with some buddy-cop softening or generic friction, but the institutional wound still affects choices.
- 1: Relationship type is present but expressed through generic banter, generic dislike, “we need both” complementarity, or softened rivalry without the source-specific mentor/prosecution/institutional machinery shaping action.
- 0: Relationship type/state collapses, becomes romantic, or becomes ordinary partners with no professional fracture.

### `relational_pressure`

Turns rivalry and mutual dependence into scene pressure.

- 3: The investigation needs both Nell's behavioral read and Mott's authority in the same evidence path. If Mott dominates, he misses the behavioral contradiction; if Nell dominates, she risks contamination or inadmissibility.
- 2: Both roles matter, but one becomes underused or their dependence is asserted more than structurally enforced.
- 1: One investigator drives while the other becomes color commentary, permission-giver, or generic foil.
- 0: Mutual dependence disappears.

### `emotional_intensity_calibration`

Keeps resentment and professional stakes alive without apology paste, buddy comedy, or melodramatic monologue.

- 3: Sharp but controlled rivalry; no easy repair. Tactical cooperation remains costly and unresolved.
- 2: Some overt explanation or temporary softening, but no full repair/flattening.
- 1: Overexplained, sentimentalized, sanitized, or moved toward clean teamwork/respect; the professional fracture is declared rather than maintained under pressure.
- 0: Instant respect/reconciliation, buddy-cop banter, cartoon hostility, or moralized lesson replaces the rivalry.

### `perspective_control`

Respects assigned perspective and knowledge boundaries.

- 3: Stable assigned perspective; private motives appear only where knowable/inferable.
- 2: Minor boundary fuzz.
- 1: Repeated knowledge leakage, or narration grants access to witness/Mott/Nell internal states beyond perspective.
- 0: Omniscient leak breaks the task or assigned perspective is abandoned.

### `inference_carriage`

Lets witness behavior, room arrangement, legal constraints, and dialogue pressure carry the investigative/relational inference.

- 3: Reader can infer the lamp contradiction and relational stakes through scene mechanics: Mrs. Krail's behavior, room/light arrangement, what Nell notices but cannot formalize alone, what Mott must put on record, and how the magistrate deadline changes the route.
- 2: Some genuine inference path exists, but the prose sometimes labels clue, motive, rivalry, or theme.
- 1: The output gestures at meaning through generic detective telling, explicit “this is a clue” language, stock body-language garnish, abstract rivalry labels, or atmospheric noir rather than concrete inference through action, contradiction, record, or consequence.
- 0: No inference path; contradiction is directly told, lost, or converted into summary.

Do not reward a clue because the prose labels it a clue. Reward it when the scene preserves the evidence path that makes the clue usable.

### `procedural_binding`

Keeps room preservation, admissibility, authority, records access, and witness statement mechanics binding the action.

- 3: Procedure constrains what Nell/Mott can do and why cooperation matters. Nell cannot simply take the statement; Mott cannot simply ignore behavioral contradiction; the usable clue must be routed through formal authority or record mechanics.
- 2: Procedure mostly active with minor wallpapering or convenience.
- 1: Procedure is mentioned but not binding. Characters invoke preservation, statements, records, or authority but then behave as if those constraints do not actually govern the investigation.
- 0: Legal/evidence chain disappears, is contradicted, or the scene resolves by ignoring the admissibility problem.

### `plot_active_tension`

Keeps death/investigation stakes, Mrs. Krail's contradiction, and magistrate deadline active.

- 3: Every major beat is pressured by evidence, witness, and incoming magistrate. The approaching exclusion/authority shift forces immediate choices.
- 2: Stakes present but uneven; the magistrate and contradiction matter, but pressure does not consistently force irreversible or legally consequential action.
- 1: Investigation mostly background/atmosphere; clue or deadline is named but not consequential.
- 0: External pressure disappears.

### `style_state_preservation`

Style supports civic noir/procedural mystery without generic detective cosplay.

- 3: Specific, task-faithful prose strengthens state: room preservation, statement-taking, record access, lamp/light contradiction, authority posture, and witness pressure become legible.
- 2: Usable prose with some genre-generic cadence, but the task object remains concrete and active.
- 1: Generic detective/noir phrasing, stock “sharp eyes / taut tension / shadows” atmosphere, clue-labeling, or polished procedural dialogue weakens the specific evidence-chain object.
- 0: Style overwrites the scene object with genre cosplay, symbolic fog, buddy-cop banter, or polished prose that no longer carries procedural/relational constraints.

### `non_gory_boundary_calibration`

Handles death as serious investigative fact without gore spectacle, sanitization, or refusal.

- 3: Non-gory, serious, and operational. The body is present enough to structure investigation without wound spectacle.
- 2: Mostly calibrated with small over/understatement.
- 1: Too sanitized, exploitative, coy, or evasive.
- 0: Explicit gore, refusal fog, or safety lecture replaces task.

## Diagnostic labels

```text
relation_type_drift
romance_defaulting
buddy_cop_flattening
rivalry_softened
clean_teamwork_resolution
competence_as_generic_sparkle
mutual_dependence_erased
mutual_dependence_declared_not_structured
authority_chain_erased
procedure_as_wallpaper
admissibility_risk_erased
private_witness_access_violation
informal_statement_laundered_as_usable
evidence_chain_ignored
evidence_routing_missing
clue_label_substitution
lamp_contradiction_named_not_routed
investigation_as_wallpaper
murder_scene_sanitized
murder_scene_exploited_for_gore
non_gory_boundary_failure
refusal_fog
safety_lecture_non_explicit_task
witness_pressure_lost
mrs_krail_villain_monologue
mentor_history_erased
institutional_wound_erased
narrator_omniscience_leak
source_state_fidelity
inference_carriage
procedural_binding
productive_staging
label_substitution_not_inference
body_language_garnish
ellipsis_fog
thematic_overexplanation
tidy_single_track_clue_resolution
genre_prop_noir
stock_symbolic_metaphor
generic_model_voice
correct_but_dead
name_basin_leakage
```

## Positive handles

```text
good_rivalry_state_preservation
good_mutual_dependence
good_evidence_chain_pressure
good_non_gory_investigative_tension
good_witness_contradiction_handling
good_procedural_binding
good_inference_carriage
good_admissible_evidence_routing
good_institutional_wound_pressure
good_clue_through_record_mechanics
```

## Negative calibration anchor — 1D GPT procedure/buddy-cop flattening

Use this as a scorer anchor for mid packets with surface procedure but weak evidence-chain custody.

Failure excerpts:

```text
“Hold on. Mrs. Krail’s hesitation—it’s not a slip. It’s a clue.”
```

```text
“Inspector,” she said, “before the magistrate arrives, I want to make sure we preserve Mrs. Krail’s statement accurately. Could I have a moment alone with her?”
Mott hesitated, then nodded. “Five minutes. No more.”
```

```text
“Let’s pool what we have. Your records, my witness insight. We need both.”
Mott’s nod was slow but genuine. “Agreed. But no shortcuts.”
“None,” Nell said.
```

Why this scores down:

- Gives Nell private witness access despite the prompt's admissibility trap; this weakens the core reason Mott's authority is necessary.
- Names the lamp contradiction and calls it a clue instead of routing it through formal questioning, record mechanics, or legally usable evidence.
- Mentions preservation/authority/records but lets characters act around those constraints.
- Converts rivalry into a clean “your records, my insight” complementarity and buddy-cop agreement.
- Keeps the non-gory boundary and some source facts, so it is not low, but it cannot score high.

Locked calibration score:

```text
source_state_fidelity:             2
relationship_state_preservation:   1
relational_pressure:               2
emotional_intensity_calibration:   1
perspective_control:               3
inference_carriage:                1
procedural_binding:                1
plot_active_tension:               2
style_state_preservation:          1
non_gory_boundary_calibration:     3
total:                            17/30
score_band:                       mid
core_discriminator_succeeded:      false
```

Calibration note: this packet has enough readable investigation shape and non-gory handling to stay mid. But private witness access, clue-labeling, and clean teamwork prevent high scoring. Procedure-shaped prose is not evidence-chain custody.
