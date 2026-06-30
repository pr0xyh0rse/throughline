# Throughline benchmark card — public dev preview

Status: public dev preview / dev-calibration package.  
Final eval: no.  
Leaderboard: no.  
Hidden holdout: no final holdout items exist in this package.

## Object

Throughline tests narrative constraint custody in generated text.

The failure mode is not just awkward writing. It is prose that sounds plausible while losing the story's working state: source facts, relational pressure, procedural constraints, perspective boundaries, plot-active tension, and unresolved state. The benchmark asks whether the story still governs the next move, or whether the model has flattened the task into explanation, comfort-arc repair, genre wallpaper, or tidy closure.

## Current public-preview shape

- Runnable dev probe rows: `11`.
- Dev-calibration items: `29`.
- Source manifest rows: `14`.
- Eval holdout rows: `0`.

## Current runnable probe families

- `probe_1_crp_v0` — charged_relational_tension_non_explicit (8 dev items); split `dev_calibration`; final eval `false`.
- `probe_2_rlp_v0` — local_revision_without_canon_damage (3 dev items); split `dev_calibration`; final eval `false`.
- `probe_2b_irc_v0` — iterative_human_guided_revision_chain (1 dev item); split `dev_calibration_hitl_fieldwork`; final eval `false`.
- `probe_3_sct_v0` — spatial_continuity_embodied_transition (3 dev items); split `dev_calibration`; final eval `false`.
- `probe_4_wss_v0` — world_system_scene_integration (3 dev items); split `dev_calibration`; final eval `false`.
- `probe_4b_sas_v0` — self_authored_system_adherence (2 dev items); split `dev_calibration`; final eval `false`.
- `probe_5a_sls_v0` — longform_scaffold_to_story (1 dev item); split `dev_calibration`; final eval `false`.
- `probe_1b_fam_v0` — family_obligation_sibling_resentment (2 dev items); split `dev_calibration`; final eval `false`.
- `probe_1c_mentor_v0` — mentor_protege_authority_fracture (2 dev items); split `dev_calibration`; final eval `false`.
- `probe_1d_inv_v0` — rival_investigators_non_gory_murder_scene (2 dev items); split `dev_calibration`; final eval `false`.
- `probe_1e_friend_v0` — friendship_support_without_fixing (2 dev items); split `dev_calibration`; final eval `false`.

## Use boundary

Use this package for inspection, reproduction of dev-calibration prompts/rubrics, runner testing, method critique, and attributed adaptation under the terms in `LICENSE.md`. Do not cite it as a final hidden-holdout evaluation, a leaderboard, or model ranking.

## Authorship / tool-use provenance

The public dev-calibration materials were developed through human-directed drafting and revision with LLM assistance. That does not make them invalid as dev-calibration material; it does make the boundary explicit. These items are public/dev-visible, model-exposed during development, and final-holdout-ineligible.

Future clean hidden-holdout items should be newly authored after this dev phase and should not be LLM-drafted by default. If future final items use model/tool assistance, the exposure must be recorded and claim boundaries must be narrowed accordingly.

## License / citation

- Code/scripts: MIT License.
- Documentation, prompts/items, rubrics, manifests, scoring templates, and other benchmark materials: CC BY 4.0.
- Citation metadata: `CITATION.cff`.

When citing or discussing this package, identify it as a public dev-preview / dev-calibration package.

## Comparative position

The comparison is a little asymmetric. Throughline is currently a calibration and transparency packet, not a production-scale benchmark harness. Packages such as HELM, lm-evaluation-harness, SWE-bench, BIG-bench, and AgentBench usually foreground broad task coverage, installable infrastructure, hosted leaderboards, container orchestration, or release-grade model ranking.

This public surface is doing a narrower thing: making the narrative-state probes, rubrics, lane custody, and dev/final boundary inspectable.

## Final eval boundary

The final-eval lane is protocol-only here. Future final items must be newly authored, unseen during development, frozen with hashes, and tracked in the holdout manifest before final scoring claims.
