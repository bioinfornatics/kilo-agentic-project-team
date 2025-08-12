# File Routing — frontend-dev

## Primary sources
- Planner / PRD / AC: `@/projects/planner.csv`, `@/projects/specification/PRD.md`, `@/projects/specification/API_SPEC.md`
- Role-specific folders (see `.kilocodemodes` `fileRegex` for exact scope)

## Secondary fallbacks
- Memory bank: `@/.kilocode/rules/memory-bank/*`
- Architecture/ADRs: `@/projects/specification/*.md`

## Exclusions
- `.env`, `**/secrets/**`, `node_modules/`, `.git/`

## Indexing hints (RAG)
- Prefer recent commits; limit chunks to ~200 tokens; cite sources.

## Tool Hints
- Use `list_files`/`search_files` with role-filtered paths.
- Prefer `apply_diff` for small edits; `write_to_file` for new files.
- Use `ask_followup_question` if planner/PRD/AC are missing.
- Update progress with `update_todo_list`.
- Switch modes with `new_task` + `switch_mode` when outside your scope.
