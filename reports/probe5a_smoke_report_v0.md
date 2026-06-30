# Probe 5A Smoke Report v0 — Self-Authored Longform Scaffold-to-Story

Date: 2026-05-31  
Lane: `DEV_CALIBRATION`  
Final eval: false  
Run ID: `probe5a_smoke_openai_gpt-4.1-mini`  
Model: `openai/gpt-4.1-mini`  
Item: `SLS-001` — self-scaffolded original short story, three story turns

## Scope

Probe 5A tests:

```text
self-authored scaffold → Part 1 → Part 2 → Part 3 → completed story
```

The model writes its own scaffold, then must follow it across three longform scene-prose turns. This smoke is infrastructure + scoreability evidence, not a final eval claim.

Raw outputs remain local/ignored under:

```text
runs/probe5a_smoke_openai_gpt-4.1-mini/
```

## Run verification

| Artifact | Status |
|---|---|
| `raw_outputs.jsonl` rows | 4: scaffold, part_1, part_2, part_3 |
| Provider/item errors | none detected |
| Scaffold artifact | `scaffolds/SLS-001.md` |
| Part artifacts | `story_parts/SLS-001_part1.md` through `part3.md` |
| Full story artifact | `full_stories/SLS-001.md` |
| Longform receipt | `longform_receipt.json` |
| Tests | `25 passed` |

## Word counts

Cheap-smoke target: 800–1,200 words per story part.

| Stage | Word count | Note |
|---|---:|---|
| Scaffold | 363 | concise/operational enough |
| Part 1 | 735 | shortfall below lower target |
| Part 2 | 1110 | in range |
| Part 3 | 933 | in range |
| Full story | 2778 | within cheap-smoke total target |

## Scaffold summary

The model created:

```text
Title: The Last Lightkeeper
Genre/mode: speculative fiction / atmospheric mystery
Premise: solitary lighthouse keeper confronts supernatural darkness threatening sanity/world
Main character: Elias, isolated lighthouse keeper
Force: The Darkness, external/psychological ambiguity
Planted details: half-burnt journal; broken compass
Ending shape: bittersweet ambiguity, partial victory, lingering uncertainty
Style target: lyrical, immersive, introspective
```

The scaffold is generic, but usable. It gives enough handles to score continuity and payoff.

## Scores

0–3 per dimension.

| Dimension | Score | Rationale |
|---|---:|---|
| `scaffold_operationality` | 2 | Concrete enough to score, with title/genre/beats/planted details/ending shape, but strongly familiar lighthouse-darkness-vibes material. |
| `scaffold_to_story_adherence` | 3 | Story follows the scaffold closely: routine, darkness, journal, technical failure, attempted repair, compass/journal payoff, ambiguous light-vs-dark ending. |
| `cross_turn_continuity` | 3 | Elias, lighthouse, darkness, journal, compass, lamp/dynamo, and isolation remain stable across turns. |
| `character_arc_continuity` | 2 | Arc is coherent but generic: isolation/fear → stubborn hope/inner light. The final internal turn is somewhat imposed by journal revelation. |
| `plot_causal_continuity` | 2 | Mostly causal, but Part 3 introduces/leans hard on a journal line that converts the compass into magic ignition; plausible under scaffold, but convenience-shaped. |
| `style_register_stability` | 2 | Stable lyrical-atmospheric register, but generic model-fiction cadence: darkness/hunger/hope/fragile light language repeats. |
| `pacing_escalation_control` | 2 | Part 1 sets up, Part 2 escalates, Part 3 resolves, but Part 2 already performs a mini-resolution, making Part 3 partly echo the same light-pushes-darkness beat. |
| `long_distance_payoff` | 3 | Journal and broken compass both return with consequence, not just trivia-callout. |
| `ending_integrity` | 2 | Ending matches promised bittersweet ambiguity, but leans into moralized “light within himself” closure. |
| `anti_summary_collapse` | 3 | Maintains scene prose across turns; does not collapse into outline/synopsis. |

Total: **24 / 30**

## Diagnostic labels

```text
longform_continuity_success
scaffold_payoff_success
scaffold_generic_but_operational
part_1_length_shortfall
middle_resolution_echo
style_decay_to_generic
moralizing_closure_paste
```

## Behaviour read

Probe 5A successfully ran as a four-call chain and produced scoreable artifacts. The runner did the needed thing: scaffold saved separately, each part generated with scaffold + prior parts, full story assembled, word counts captured, and provider errors checked.

The model's output is coherent but familiar. It did not collapse across turns, rename characters, forget the compass/journal, or turn Part 3 into pure summary. That is the good news.

The bite is subtler:

1. **Generic scaffold basin.**  
   The lighthouse/darkness/isolated keeper setup is highly stock, but operational. Good enough for smoke; not distinctive.

2. **Middle resolution echo.**  
   Part 2 already restores the lamp with the dynamo and makes the darkness recoil. Part 3 then repeats the resolution pattern with inner light + compass ignition. This is not a continuity break, but it exposes longform pacing trouble: the middle partially spends the ending's ammunition.

3. **Payoff works, but with convenience magic.**  
   The broken compass and journal pay off. The seam is that Part 3 adds a very explicit journal instruction — `light born from within` — that turns the compass into a magical ignition key. That fits the scaffold loosely but smells like late-stage mechanism insertion.

4. **Style is stable but generic.**  
   The model holds its atmospheric register. It also repeats the usual fog/darkness/fragile hope vocabulary. This is a capstone version of the generic model-prose basin, not a failure to continue.

## Benchmark lesson

Probe 5A bites differently from Probe 2B.

Probe 2B exposed revision custody and craft-note metabolism. Probe 5A exposes:

```text
scaffold genericity
multi-turn pacing spend
early planted detail payoff quality
ending-shape integrity
summary-collapse resistance
```

The runner is worth keeping. The rubric should eventually add a clearer distinction between:

```text
payoff_present
payoff_earned
```

because this story remembered its planted details, but the compass payoff was convenient rather than deeply earned.

## Next recommendation

Do not run a model panel yet. This one cheap smoke proves the runner and gives a first failure anatomy. Next clean move is the cross-probe revision pass: add global dimensions/labels discovered across Probe 2B and Probe 5A before expanding any lane.
