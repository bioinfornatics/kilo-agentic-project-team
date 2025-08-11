# Workflow — Handoff
**stages:** PM → Full‑Stack → QA → UI/UX → DevOps

## Stage Requirements
- **PM:** `spec.md`, `acceptance.md`
- **Full‑Stack:** `diff.patch`, `tests/*`
- **QA:** `playwright/*.spec.ts`, `coverage/summary.json`
- **UI/UX:** `stories/**/*.stories.*`, `a11y/report.json`
- **DevOps:** `.github/workflows/*.yml`, `infra/**`, `otel/*`

## 
- `python scripts/scan_secrets.py`
- `python scripts/enforce_notices.py`

## Pre-commit
Run the following checks locally or in CI:
- `python ops/scan_secrets.py` (blocks on findings)
- `python ops/enforce_notices.py` (blocks if deps changed without notices)

## Mode Self‑Check
Before starting a handoff, validate modes and pins:
```bash
python scripts/test_mode_pins.py
```

## Memory Budget Check
Keep `.kilocode` lean; ensure long‑form memory stays outside. Verify token budgets:
```bash
python scripts/check_mb_tokens.py --max 800
```
