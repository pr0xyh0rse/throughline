# Throughline public dev preview package receipt

Timestamp: 20260626T231604Z UTC  
Lane: `DEV_CALIBRATION_PREP_PACKAGE`  
Final eval / leaderboard: false  
Hidden holdout rows: 0

## Construction

Built from the clean local candidate by copying the manifest-backed prompt/rubric/protocol spine and excluding bulk scored-output surfaces.

## Intentional exclusions

```text
CLEAN_EXPORT_RECEIPT.md
PACKAGE_ASSEMBLY_RECEIPT.md
README_dev_package_v0.md
reports/full historical scoring and scorer-friction reports
eval/scorer-friction artifacts
scorer_packets/
raw model outputs
runs/
backups/
__pycache__/
.pytest_cache/
local env files
```

## Counts

```text
probe_rows: 12
runnable_probe_rows: 11
source_rows: 14
dev_item_ids: 29
holdout_rows: 0
```

## Prep lineage

Built as a clean dev-calibration prep package from `throughline_public_dev_preview_20260626T125420Z`; excludes local env/cache files and clarifies probe-manifest vs runnable-probe counts.
