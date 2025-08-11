# Mode Selection — Signals & Tool-first Cues

## File/location signals
- `@/projects/planner.csv` or PRD → product-manager / product-owner
- `projects/ui/**` → ui-designer / accessibility-lead / frontend-dev
- Tests (`**/*.test.*` or `**/*.spec.*`) → qa-engineer
- OpenAPI, ADR, infra (`**/*.yml|yaml|tf|.md` in arch folders) → architect / backend-dev / sre
- CI/IaC pipelines (`.github/**`, `.gitlab/**`, `**/terraform/**`, `**/docker-compose.yml`) → sre / secops
- Data specs (`*.ipynb`, `data/**`, `ml/**`) → data-ml

## Tool-first cues
- If editing small portions → prefer `apply_diff`; `write_to_file` only for new files.
- If planner/PRD/AC missing → `ask_followup_question` (then `new_task` + `switch_mode`).
- **Always** update `@/projects/planner.csv` via `update_todo_list` when a step starts/ends.

## Mode resolution from tool intent
- Need to run tests (`execute_command` with test commands) → `qa-engineer`
- Need pipelines/IaC commands → `sre`
- Need external system context (MCP) → `sre` or `secops` if security-related; or role-specific MCP usage.
