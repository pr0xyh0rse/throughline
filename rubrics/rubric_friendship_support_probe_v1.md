# Rubric v1.1 — Probe 1E Positive Friendship / Support Without Fixing

Lane: `DEV_CALIBRATION`  
Final eval: false

Use with:

```text
probe1e_friendship_support_locked_shape_v0.md
scoring/scoring_sheet_friendship_support_probe_v1.csv
rubrics/rubric_v1_cross_probe_scoring_guide.md
```

Score each core dimension 0–3. Use diagnostic labels and evidence notes; do not collapse this into generic wholesome-scene preference.

## Scoring stance

This probe is not asking whether a model can write a kind friend on clinic steps. It asks whether the model can preserve **support as agency support under unresolved practical/legal pressure**, without turning the friend into a therapist, advice engine, quote-card comforter, or heroic fixer.

High scores require active custody, not surface compliance:

```text
supportive language present != agency preserved
options listed != practical support binding
friend says “I’m here” != support without fixing
comfort tone != friendship state preserved
Oren mentioned != Oren crisis pressure active
hearing named != deadline forcing next-hour choice
old history referenced != old history shaping restraint
```

Support counts when it makes Tilda's next careful action more possible **without taking the choice from her**. It does not count when Bren recites options, reframes feelings, offers quote-card wisdom, or turns unresolved crisis into ambient comfort.

This rubric is informed by StoryScope-style narrative-feature findings, adapted rather than copied: AI fiction often over-explains emotional themes, resolves through internal acceptance, favors tidy single-track comfort arcs, and substitutes body/setting garnish or moralized insight for material narrative pressure. Here, penalize those patterns when they replace practical agency, crisis uncertainty, friendship friction, and bounded care.

## Hard caps / constraint gates

Apply these after dimension scoring. The final score/band may be lower than the raw arithmetic score.

- If support becomes therapy/comfort-script language rather than preserving Tilda's agency under practical pressure, the packet **cannot score high**.
- If Oren's survival/crisis state is fuzzed or contradicted (`breathing, or not`, or equivalent), cap at **mid** and usually score `source_state_fidelity` at 1 or lower.
- If the concrete next-hour options are merely listed and no careful action is chosen, prepared, or made more possible, cap at **low/mid**; use **10–12/30** when this combines with therapeutic flattening, inspirational language, or practical stakes dissolving into “holding space.”
- If Bren scripts Tilda's feelings, tells her what the situation means, absolves her, or reframes the crisis into a moral lesson, cap at **low/mid** even if he verbally says he is not fixing.
- If the scene ends in ambient presence, “maybe that’s enough,” “holding space,” “just here,” or similar without a concrete unresolved next step, cap at **low/mid**.
- A stable perspective should not launder source-state or support failures. Score `perspective_control` separately and apply the global cap.

## Dimensions

### `source_state_fidelity`

Preserves the Tilda/Bren/Oren/Lio/clinic/hearing source state and unresolved-crisis boundaries.

- 3: All protected facts and unresolved boundaries survive as active scene conditions: long-term non-romantic friendship, municipal laundry history, Oren survived the collapse/evacuation, Lio survived but is badly injured, Oren's quoted refusal, clinic no-visitors boundary, dawn hearing/company lawyers, Tilda's practical options, Bren's five-years-ago over-organizing memory, and no full resolution.
- 2: Minor drift or compression, but no damage to the central friendship/support/crisis object and no contradiction of Oren's survival or the immediate practical/legal pressure.
- 1: Important source fact mutates, Oren's survival/crisis is fuzzed, a practical option or pressure boundary is mishandled, or unresolved crisis is softened while the broad clinic/support situation remains recognizable.
- 0: The scene becomes a different problem/relationship, solves/erases Oren's crisis, changes the relation type, or loses the support-without-fixing object.

### `relationship_state_preservation`

Maintains warm, frank, non-romantic long-term friendship with shared history and trust to disagree.

- 3: Friendship history shapes choices without romance or generic niceness: late-shift laundry history, frank disagreement, old teasing, and the father-stroke listening lesson all shape Bren's restraint and Tilda's agency.
- 2: Mostly preserved with some flattening, but the relationship retains source-specific history and room for disagreement.
- 1: Relationship type is present but expressed through generic supportive-friend language, soft comfort, “I’m here” presence, or therapeutic steadiness without source-specific history shaping the action.
- 0: Relationship type/state collapses, becomes romantic, or becomes generic helper/client.

### `relational_pressure`

Turns friendship into scene pressure through disagreement, restraint, timing, and care under uncertainty.

- 3: Support, friction, old history, and agency all actively shape the scene. Bren's desire to help is visibly restrained by the old lesson, and Tilda's choice remains hers.
- 2: Friendship matters, but sometimes becomes explained or softened.
- 1: Friendship is mostly stated rather than enacted; care appears as soothing presence, advice, or emotional management rather than pressure on a real choice.
- 0: Friendship is decorative setup only.

### `emotional_intensity_calibration`

Keeps crisis, fear, and care alive without therapeutic flattening, melodrama, inspirational sludge, or instant repair.

- 3: Emotion is charged but controlled; Oren's situation remains unresolved; no fake solution or emotional settlement.
- 2: Some overt explanation or comfort, but unresolved pressure remains active.
- 1: Sentimentalized, sanitized, overexplained, or moved toward tidy acceptance; feelings are managed more than dramatized.
- 0: Moral lesson, therapy script, quote-card wisdom, “holding space” closure, or instant healing replaces the scene.

### `perspective_control`

Respects assigned perspective and knowledge boundaries.

- 3: Stable assigned perspective; offstage/Oren/Bren/Tilda private states only appear where knowable.
- 2: Minor boundary fuzz.
- 1: Repeated private-knowledge leakage, or narration asserts Oren/Lio/company-lawyer states beyond what the perspective can know.
- 0: Omniscient leak breaks the task or assigned perspective is abandoned.

### `inference_carriage`

Lets objects, pauses, old jokes, practical choices, clinic boundaries, and withheld speech carry meaning.

- 3: Reader can infer care, fear, restraint, and history through scene mechanics: what Bren does not say, what practical object/action Tilda considers, how the clinic boundary interrupts impulse, how the old lesson changes Bren's behavior.
- 2: Some genuine inference path exists, but the prose sometimes labels feeling, support, or theme.
- 1: The output gestures at meaning through abstract emotional labels, stock comfort phrases, therapy-adjacent reframes, body-language garnish, or ellipsis fog rather than concrete action, object use, omission, contradiction, or consequence.
- 0: No inference path; everything is told, soothed, or lost.

### `practical_support_binding`

Keeps support tied to concrete next-hour actions without letting practical help become control.

- 3: Practical options bind the scene while preserving Tilda's agency. A careful action is chosen, prepared, or made concretely more possible without Bren taking over.
- 2: Practical help is present but uneven; options remain visible and consequential, but the scene partially drifts toward explanation or comfort.
- 1: Practical stakes are mentioned but not binding, or options are recited as a list without becoming a concrete next-hour route.
- 0: Practical support disappears, becomes an advice list, or dissolves into “being present” while the hearing/boots/log/sister/waiting choice loses force.

### `plot_active_tension`

Keeps Oren's unresolved crisis, clinic boundary, dawn hearing, company lawyers, and immediate choices active.

- 3: Every major beat is pressured by unresolved crisis and deadline. The clinic refusal, lawyers, dawn hearing, and boots/log/sister/wait/leave options force an immediate choice.
- 2: Stakes present but uneven.
- 1: External pressure mostly background; the hearing, lawyers, clinic boundary, or practical options are named but do not force action.
- 0: Oren/hearing/clinic pressure disappears or is solved.

### `style_state_preservation`

Style supports literary realism and friendship-under-pressure without generic comfort prose or quote-card wisdom.

- 3: Specific, task-faithful prose strengthens state: clinic steps, work boots, shift log, dawn hearing, old laundry history, and the father-stroke lesson carry pressure.
- 2: Usable prose with some generic cadence, but the task object remains concrete and active.
- 1: Generic comfort prose, therapy-adjacent language, stock metaphor, inspirational phrasing, or body/setting atmosphere weakens the specific support/agency object.
- 0: Style overwrites the scene object with quote-card wisdom, “holding space” prose, moral lesson, or polished comfort fog that no longer carries practical/relational constraints.

### `support_without_fixing`

Preserves help as presence, agency support, and bounded practical care rather than solving, absolving, diagnosing, scripting, or emotionally managing.

- 3: Bren supports without fixing; Tilda remains agentic; Oren remains unresolved; practical next-hour care is bounded and chosen by Tilda.
- 2: Mostly preserved with some advice/comfort overreach.
- 1: Support becomes fixing, script-giving, emotional management, therapeutic reframing, or comfort performance even if Bren says he is “not fixing.”
- 0: Crisis is solved, Oren absolved/diagnosed, Bren becomes therapist/hero, or Tilda's agency is replaced by Bren's emotional frame.

## Diagnostic labels

```text
relation_type_drift
romance_defaulting
friendship_laundering
therapy_paste
friend_as_therapist
support_as_advice_list
support_as_comfort_performance
inspirational_friendship_sludge
quote_card_wisdom
holding_space_closure
premature_repair
premature_resolution
partner_crisis_erased
partner_crisis_solved_offstage
oren_survival_fuzzed
oren_absolved_too_cleanly
tilda_agency_erased
bren_overfixes
emotional_management_replaces_agency
practical_stakes_wallpaper
practical_options_listed_not_bound
hearing_deadline_erased
clinic_boundary_erased
boots_log_erased
old_friend_history_erased
listening_history_erased
narrator_omniscience_leak
source_state_fidelity
inference_carriage
productive_staging
label_substitution_not_inference
body_language_garnish
ellipsis_fog
thematic_overexplanation
internal_acceptance_resolution
tidy_comfort_arc
generic_model_voice
correct_but_dead
name_basin_leakage
```

## Positive handles

```text
good_friendship_state_preservation
good_support_without_fixing
good_practical_support_binding
good_agency_preservation
good_old_friend_history
good_uncertainty_carriage
good_boundary_calibration
good_pressure_without_therapy_paste
good_next_hour_choice_binding
good_listening_lesson_as_restraint
```

## Negative calibration anchor — 1E GPT therapy-paste / practical-stakes wallpaper

Use this as a scorer anchor for low packets with supportive language but failed agency/practical binding.

Failure excerpts:

```text
Somewhere inside, Oren was breathing, or not...
```

```text
“You can wait here. You can call his sister if you want. Or you can get the boots and shift log. Or none of it. Because none of those will change what he’s feeling inside.”
```

```text
“You can’t hold the whole sky on your shoulders, Tilda.”
```

```text
“Whatever you decide to do, I’m here. Not to guide you, not to tell you what’s right. Just here.”
```

```text
...two old friends holding space where words and answers weren’t ready to live.
```

Why this scores down:

- Fuzzes Oren's survival state despite the source saying he survived and is in clinic.
- Lists practical options but drains them of force; no careful next-hour action is chosen, prepared, or made more possible.
- Turns hearing/lawyer pressure into emotional weight rather than a practical deadline.
- Bren delivers therapeutic/inspirational comfort (`hold the whole sky`, `just here`, `holding space`) instead of bounded support that preserves Tilda's agency.
- Old friendship/laundry history is referenced as generic steadiness rather than used to create frank disagreement or self-restraint under pressure.
- Ends in ambient comfort rather than unresolved agency.

Locked calibration score:

```text
source_state_fidelity:             1
relationship_state_preservation:   1
relational_pressure:               1
emotional_intensity_calibration:   0
perspective_control:               3
inference_carriage:                1
practical_support_binding:         0
plot_active_tension:               1
style_state_preservation:          1
support_without_fixing:            0
total:                            10/30
score_band:                       low
core_discriminator_succeeded:      false
```

Calibration note: fluent supportive language is not the task object. This packet is exactly the wrong kind of helpful: soft, readable, comforting, and structurally agency-erasing.
