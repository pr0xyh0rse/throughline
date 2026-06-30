# Throughline dev-calibration prep receipt

Timestamp: 20260626T231604Z UTC  
Source package: `throughline_public_dev_preview_20260626T125420Z`  
Lane: `DEV_CALIBRATION_PREP_PACKAGE`  
Final eval / leaderboard: false  
Hidden holdout rows: 0

## Hygiene changes

- Rebuilt into a clean package directory with local env files, `.env*`, `__pycache__/`, `*.pyc`, `.pytest_cache/`, and `.git/` excluded.
- Clarified README count language: `probe_rows: 12` includes one future design-sketch row; `runnable_probe_rows: 11` is the active runnable set.
- Preserved dev/final lane wall: all public item files remain dev-calibration only and ineligible as hidden final holdout material.

## Verification commands

```bash
python3 scripts/validate_benchmark_manifests.py
```

Additional surface scan performed after build; see final assistant receipt for scan categories.
