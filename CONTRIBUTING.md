# Contributing to Throughline

Throughline is currently a public dev-calibration package, not a final hidden-holdout benchmark or leaderboard.

Useful feedback is welcome when it helps inspect the method: source custody, dev/final separation, prompt shape, rubric clarity, runner behavior, manifest consistency, documentation accuracy, or reproducibility of the validation path.

## Good issue or PR topics

- A manifest path, count, or status field appears inconsistent.
- A rubric category is ambiguous or hard to apply.
- A prompt shape does not match the documented probe purpose.
- A runner or validation script fails on a clean checkout.
- README, benchmark-card, license, or citation language overstates or understates the package status.
- A proposed future probe needs a clearer source lane, scoring target, or contamination boundary.

## Please do not submit

- Final-eval or hidden-holdout candidate items in public issues or pull requests.
- Private, unpublished, or third-party source material that you do not have rights to share.
- Raw model outputs, scoring packets, provider retry logs, or bulk evaluation reports unless a maintainer explicitly asks for them.
- Leaderboard claims, model rankings, or final benchmark claims based on this dev-calibration package.
- API keys, local environment files, cache files, or machine-local paths.

## Proposing new probes

If you want to propose a probe, describe the evaluation object rather than dropping item text first.

Useful shape:

```text
probe goal:
failure mode being tested:
source material status: synthetic / public-domain / licensed / other
whether item text is public/dev-visible:
expected scoring axes:
why this should be dev calibration vs future holdout:
```

Public issues are a dev-visible surface. Anything posted there should be treated as ineligible for future hidden final evaluation.

## Pull request hygiene

Before opening a PR, run:

```bash
python3 scripts/validate_benchmark_manifests.py --root . --warnings-as-errors
bash -n scripts/run_probe1_openrouter_matrix.sh
```

If you change package files, regenerate `MANIFEST.csv` so the public receipt matches the tree.

Keep generated outputs out of the repo. `runs/`, local environment files, `__pycache__/`, and `*.pyc` files should not be committed.

## Boundary reminder

The included dev-calibration materials are useful for inspection, calibration, and critique. They are not a final hidden evaluation set. A future final eval would require new unseen source states/items, hashes, a populated holdout manifest, and a separate freeze receipt.
