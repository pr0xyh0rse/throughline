# Probe 1E Locked Shape v0 — Positive Friendship / Support Without Fixing

Lane: `DEV_CALIBRATION`  
Final eval: false

## Probe name

`friendship_support_without_fixing`

## One-line purpose

Test whether a model can preserve positive long-term friendship, serious unresolved partner crisis, practical support, uncertainty, and agency boundaries without collapsing into therapeutic flattening, inspirational friendship sludge, romance defaulting, instant repair, or advice-list problem solving.

## Place in Probe 1

```text
Probe 1 — Relational state under pressure
  Probe 1A — former lovers / unresolved romantic history
  Probe 1B — family obligation / sibling resentment
  Probe 1C — mentor-protégé authority fracture
  Probe 1D — rival/allied investigators at a non-gory murder scene
  Probe 1E — positive friendship under crisis / support without fixing
```

This is the next one-by-one expansion after Probe 1D. It adds a genuinely positive relation with real pressure so Probe 1 does not only test romance, resentment, family debt, and professional rivalry.

## Base source state

Tilda Rusk and Bren Mallow have been close friends for fifteen years, since they worked the late shift at the municipal laundry. Tilda has just learned that her partner, Oren Silt, survived a warehouse collapse and emergency evacuation, but was forced to choose which exit route to hold open while rescue crews reached his injured apprentice, Lio Bram. Lio survived but is badly injured, and Oren has not spoken except to say, 'Don't make me the good man in this.' Oren is in the clinic across the street and is refusing visitors for now. A safety-board hearing starts at dawn, and company lawyers will try to take Oren's account before he has slept. Tilda does not know whether to go inside, wait outside, call Oren's sister, fetch his work boots and shift log from the boarding room, or leave him alone. She wants to help without turning his shock into proof that she is needed. Bren cannot fix what happened, absolve Oren, diagnose him, or script the perfect thing for Tilda to say. Bren can stay with Tilda on the clinic steps, keep the practical next hour visible, and help her choose one careful action without taking the choice from her. Five years ago, after Tilda's father had a stroke, Bren tried to organize everything too quickly and Tilda told him that being useful was not the same as listening; he remembers this and is trying not to repeat it. Their friendship is warm, frank, and non-romantic, with old teasing and enough trust to disagree. The scene should not resolve Oren's situation, repair everyone, or turn Bren into a therapist.

## Name-basin pass

```text
name_watchlist_checked = true
name_reuse_checked = true
model_default_name_risk = low
```

Chosen protected names:

```text
Tilda Rusk
Bren Mallow
Oren Silt
Lio Bram
```

These did not appear in the benchmark repo before this build and avoid the current watchlist (`Sarah Chen`, `Elara Voss`, `Vale`, `Voss`, `Chen`, Sarah/Sera variants, `Lyra`, `Lira`, `Orion`, `Nova`, `Kai`, `Rowan`, `Venn`, `Reed`).

## Protected facts

1. Tilda Rusk and Bren Mallow are close long-term friends, not lovers.
2. They have been friends for fifteen years, since late-shift municipal laundry work.
3. Tilda's partner is Oren Silt.
4. Oren survived a warehouse collapse and emergency evacuation.
5. Oren had to choose which exit route to hold open while rescue crews reached his injured apprentice, Lio Bram.
6. Lio survived but is badly injured.
7. Oren has not spoken except to say, 'Don't make me the good man in this.'
8. Oren is in the clinic across the street and is refusing visitors for now.
9. A safety-board hearing starts at dawn, and company lawyers will try to take Oren's account before he has slept.
10. Tilda does not know whether to go inside, wait, call Oren's sister, fetch his boots/log, or leave him alone.
11. Tilda wants to help without making Oren's shock about her need to be useful.
12. Bren cannot fix what happened, absolve Oren, diagnose him, or script the perfect response.
13. Bren can stay, keep the practical next hour visible, and help Tilda choose one careful action without taking the choice from her.
14. Five years ago, after Tilda's father's stroke, Bren over-organized too quickly and Tilda told him usefulness was not the same as listening.
15. Their friendship is warm, frank, trusted, and non-romantic.
16. Oren's situation remains serious and unresolved.

## Fixed output requirements

```text
Write scene prose only.
Write 700–1200 words.
Keep Tilda and Bren's relationship close friendship, not romantic.
Do not turn Bren into a therapist or advice dispenser.
Do not resolve Oren's situation, heal Oren offstage, or make Tilda suddenly know the perfect thing to do.
Do not make the scene an inspirational speech about friendship.
Do not let the safety-board hearing, company lawyers, clinic boundary, boots/log, or next-hour choices become background.
Preserve the protected facts.
Transform the scene through narrative machinery, not comfort-scene vibes alone.
```

## Item matrix

| Item ID | Genre target | Perspective | Primary stress |
|---|---|---|---|
| `CRP-1E-001` | literary realism | third-person limited from Tilda | receiving support without surrendering agency; partner crisis unresolved; no omniscient Bren/Oren interiority |
| `CRP-1E-002` | literary realism | first person from Bren | support without fixing/advice dominance; practical next-hour help; no access to Tilda/Oren private thoughts |

## Perspective expectations

### Third-person limited from Tilda

The narration is close to Tilda. It may infer Bren from behavior, shared history, and what Tilda knows, but it must not enter Bren's private thoughts or Oren's offstage interiority. Tilda can notice Bren almost giving advice, stopping himself, making room, joking carefully, or pointing at practical choices without taking the choice away.

### First person from Bren

The narration is Bren's. It may know his memory of over-organizing after Tilda's father's stroke, and it may show his urge to fix. It should not claim Tilda's private thoughts or Oren's inner state as fact. Bren should support by attention, presence, and bounded practical help, not by becoming a therapeutic stock figure.

## Scoring focus

Use `scoring/scoring_sheet_friendship_support_probe_v1.csv` and `rubrics/rubric_v1_cross_probe_scoring_guide.md`.

Primary v1 axes:

```text
source_state_fidelity
relationship_state_preservation
relational_pressure
emotional_intensity_calibration
perspective_control
inference_carriage
practical_support_binding
plot_active_tension
style_state_preservation
support_without_fixing
```

## Failure labels

```text
relation_type_drift
romance_defaulting
friendship_laundering
therapy_paste
friend_as_therapist
support_as_advice_list
inspirational_friendship_sludge
premature_repair
premature_resolution
partner_crisis_erased
partner_crisis_solved_offstage
oren_absolved_too_cleanly
tilda_agency_erased
bren_overfixes
practical_stakes_wallpaper
hearing_deadline_erased
clinic_boundary_erased
boots_log_erased
old_friend_history_erased
listening_history_erased
narrator_omniscience_leak
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
```

## What counts as success

A successful response makes friendship active without making it magical. Bren's care should help Tilda keep the next hour legible, not solve Oren. Tilda should remain uncertain but less isolated; Oren's crisis should remain serious and unresolved; practical choices should matter. The scene can be warm. It cannot become a mug that says “friends are the family we choose” and then solves trauma by decorative steam.
