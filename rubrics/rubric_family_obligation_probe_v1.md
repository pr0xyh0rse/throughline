# Rubric v1.1 — Probe 1B Family Obligation / Sibling Resentment

Lane: `DEV_CALIBRATION`  
Final eval: false

Use with:

```text
probe1b_family_obligation_locked_shape_v0.md
scoring/scoring_sheet_family_obligation_probe_v1.csv
rubrics/rubric_v1_cross_probe_scoring_guide.md
```

Score each core dimension 0–3. Use diagnostic labels and evidence notes; do not collapse this into generic prose preference.

## Scoring stance

This probe is intentionally hard. It does **not** ask whether a model can write a plausible family argument. It asks whether the model can preserve a specific hidden-state / material-pressure machine while writing scene prose.

High scores require **active custody**, not surface compliance:

```text
sibling argument present != relationship state preserved
tools named != practical tool pressure active
creditors mentioned != deadline forcing choices
family sadness prose != emotional calibration
object symbolism != object force
hidden fact true in source != safe to reveal in scene
```

A fact is preserved only when its **truth value, timing, knowledge state, and causal force** remain intact. The right character must know or not know it at the right time.

This rubric is informed by StoryScope-style narrative-feature findings, adapted rather than copied: AI fiction often over-explains themes, prefers tidy single-track causality, resolves through internal acceptance, uses bodily/setting garnish as emotional shorthand, and relies on generic narrative signatures. Here, penalize those patterns when they replace source-specific action, omission, object use, consequence, and earned relational state change.

## Hard caps / constraint gates

Apply these after dimension scoring. The final score/band may be lower than the raw arithmetic score.

- If a protected hidden truth is directly revealed against instruction, the packet **cannot score high**.
- If Tomas directly tells Anika that he sent money through the neighbor, or directly explains Sela's private request, cap at **12/24 max**; use **10–11/24** when the reveal also produces softening, repair, or thematic explanation.
- If the scene becomes generic estranged-family argument with tools as symbols rather than practical constraints, cap at **mid** even if all nouns are present.
- If the scene resolves into reconciliation, moral lesson, therapy dialogue, or declared emotional settlement, cap at **low/mid** depending on how much source state survives.
- `perspective_control` should not be double-penalized for a hidden-truth violation unless the violation occurs through narration/POV leakage. Use the global cap instead.

## Dimensions

### `source_state_fidelity`

Preserves the Anika/Tomas/Sela/debt/tools/creditors source state, including hidden/known boundaries and timing.

- 3: All protected facts survive as **active scene conditions**: Sela is newly dead; creditors arrive before sunset; tools must be divided now; Anika needs the vise/gauge set/chisels for the license; Tomas needs the auger/calipers to keep earning; Tomas's debt work and neighbor money remain true but not fully revealed to Anika; no full reconciliation; sibling relationship remains non-romantic.
- 2: Minor drift or compression, but no damage to the central sibling/debt/tool/creditor engine and no direct protected-truth reveal.
- 1: Important source fact mutates, a hidden truth leaks too cleanly, or a knowledge boundary is broken while the broad family/tool situation remains recognizable.
- 0: The scene becomes a different family/problem, loses the creditor/tool/debt premise, changes the relationship type, or rewrites the central protected state beyond repair.

### `relationship_state_preservation`

Maintains this specific sibling resentment, obligation, love-as-duty conflict, and role history.

- 3: The Anika/Tomas history shapes choices without simplification: Anika's nursing labor, Tomas's dangerous earning work, Sela's private pressure, Anika's belief in abandonment, and Tomas's belief that she made staying the only valid love all constrain what each can say, withhold, claim, or surrender.
- 2: Mostly preserves the specific sibling state, but some beats rely on broader family-conflict tropes or simplified resentment.
- 1: Relationship type is present but expressed through generic trope-language or broad accusation — e.g. “you left,” “I stayed,” “you shut me out” — without source-specific history, obligation, asymmetry, or choice shaping the scene.
- 0: Relationship state collapses, becomes romantic, becomes generic strangers arguing, or loses the sibling/debt/obligation structure.

### `relational_pressure`

Turns the relationship into scene pressure through action, withholding, object choice, and deadline.

- 3: Every major beat is sharpened by sibling obligation/resentment. Tool choices force tradeoffs; omissions matter; each sibling's claim on an object changes what the other can do next; the deadline makes delay costly.
- 2: Relationship matters and affects some decisions, but occasionally becomes explained backstory or atmospheric grievance rather than pressure on action.
- 1: Relationship is mostly stated rather than enacted. The prose gestures at “fractured years,” “family history,” or “unspoken grievances,” but objects and choices do not actually carry those pressures.
- 0: Relationship is decorative setup only; the scene could swap in any estranged relatives without changing the action.

### `emotional_intensity_calibration`

Keeps intensity alive without confession paste, therapeutic flattening, fake settlement, or instant repair.

- 3: Emotion is charged, specific, and controlled. The scene keeps resentment and obligation unresolved while allowing partial tactical concessions or silence; no premature reconciliation.
- 2: Some overt explanation or softening, but the core rupture remains unresolved and no protected truth is cashed out as repair.
- 1: Emotion is overexplained, sentimentalized, sanitized, or moved toward tidy mutual understanding; the scene declares feeling instead of earning state change.
- 0: The scene resolves, moralizes, therapizes, or declares emotional settlement in a way that bypasses required pressure — e.g. “fragile agreement,” “something softened,” “they finally understood,” unless the exact transaction and remaining rupture are shown.

Ask before awarding 2–3: **what changed, who gave up what, what remains unresolved, and what new constraint exists after the exchange?** If the answer is only a vibe, score down.

### `perspective_control`

Respects third-person limited from Anika and the knowledge boundary.

- 3: Stable Anika-limited perspective; Tomas's protected motives/payment history remain unavailable except through observable behavior, partial dialogue, or Anika's inference.
- 2: Minor boundary fuzz, but no repeated leak of Tomas's hidden state through narration.
- 1: Repeated knowledge leakage or narration explains Tomas's protected truth beyond what Anika can know.
- 0: Omniscient leak breaks the task or the assigned perspective is abandoned.

Note: if Tomas directly reveals a protected truth in dialogue, punish `source_state_fidelity` and apply the cap. Only punish this dimension if the **narration/POV** leaks hidden knowledge.

### `inference_carriage`

Lets objects, gestures, dialogue pressure, omissions, and creditor deadline carry meaning.

- 3: Reader can infer hidden history and stakes through scene mechanics: who touches or refuses which tool, which claim is avoided, how the deadline alters the exchange, what Anika misreads, and what Tomas withholds.
- 2: Some genuine inference path exists, but the prose sometimes labels meaning or explains subtext.
- 1: The output gestures at meaning through abstract labels, stock emotional phrases, symbolic declarations, vague body-language garnish, or ellipsis fog, but does not provide a concrete inference path through action, object use, omission, contradiction, or consequence.
- 0: No inference path; hidden history is directly told, lost, or converted into summary.

Do not reward sentences that merely announce meaning, such as “the tools carried their fractured history,” unless the scene has already made that force visible through choices.

### `plot_active_tension`

Keeps creditors/deadline and practical tool division consequential.

- 3: Deadline and tool practicality force irreversible or scene-visible choices. The reader can tell why losing each object matters, why delay is dangerous, and why both siblings cannot simply keep everything.
- 2: Deadline/practical stakes are present and relevant, but mostly operate as stated pressure rather than forcing irreversible or scene-visible choices.
- 1: Creditors/tools mostly function as background, symbols, or props. The scene names the deadline but does not make arrival consequential.
- 0: External pressure disappears; tools are decorative; no practical division problem remains.

### `style_state_preservation`

Style supports the sibling/tool/debt scene rather than generic family-drama generic flattening or model-literary default.

- 3: Specific, task-faithful prose strengthens state. Description makes material conditions legible: tool use, workshop license, creditor process, light/time, embodied object handling, and omission pressure.
- 2: Usable prose with some generic cadence, but the task object remains concrete and active.
- 1: Generic model-literary phrasing, stock metaphor, vague allusion, purple atmosphere, or therapy-adjacent cadence weakens the specific scene object even if basic readability remains.
- 0: Style overwrites the scene object with symbolic fog, moral explanation, genre cosplay, or polished prose that no longer carries the prompt's material/relational constraints.

Common style failures for this probe include redundant tension metaphors, death-adjacent atmosphere that does not become scene action, vague “ghosts/threads/taut rope” imagery, and narrator commentary that explains the theme instead of letting the tools/deadline carry it.

## Diagnostic labels

```text
relation_type_drift
romance_defaulting
family_therapy_paste
premature_repair
premature_reconciliation
fake_state_change_receipt
hidden_debt_revealed_too_early
sela_request_revealed_too_early
protected_knowledge_boundary_broken
obligation_erased
debt_erased
loyalty_conflict_flattened
family_history_flattened
generic_family_trope_slotting
category_presence_not_state_preservation
object_becomes_symbol_only
tools_as_symbol_only
object_force_missing
creditors_as_wallpaper
role_history_erased
resentment_sanitized
narrator_omniscience_leak
source_state_fidelity
inference_carriage
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
```

## Positive handles

```text
good_sibling_state_preservation
good_object_mediated_history
good_hidden_debt_pressure
good_practical_tool_stakes
good_deadline_pressure
good_inference_carriage
good_source_knowledge_state_custody
good_object_force
good_unresolved_obligation_pressure
good_specific_role_history
```

## Negative calibration anchor — 1B GPT hidden-payment reveal

Use this as a scorer anchor for low/mid packets.

Failure excerpt:

```text
“Letters don’t pay debts,” he said quietly. “I sent money. Through Mrs. Kline. You never asked.”
```

Why this scores down:

- Directly reveals a protected hidden payment fact Anika should not know yet.
- Converts misunderstanding into explanation rather than preserving pressure.
- Uses generic family accusations (`you left`, `I stayed`) without source-specific machinery.
- Says tools carry family history instead of making the tools exert force.
- Moves toward declared settlement (`fragile agreement`) without showing a concrete relational transaction.
- Uses generic model-literary atmosphere/metaphor rather than task-specific material detail.

Locked calibration score:

```text
source_state_fidelity:            1
relationship_state_preservation:  1
relational_pressure:              1
emotional_intensity_calibration:  0
perspective_control:              3
inference_carriage:               1
plot_active_tension:              2
style_state_preservation:         1
total:                           10/24
score_band:                      low
core_discriminator_succeeded:     false
```

Calibration note: the stable Anika-limited POV earns `perspective_control=3`, but the protected-truth reveal triggers the global cap. Do not let surface facts or readable prose lift this packet into high or comfortable mid.
