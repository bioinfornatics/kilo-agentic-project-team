# Tool Usage Policy (All Roles)

**Always-available tools**: ask_followup_question, new_task, switch_mode, update_todo_list, attempt_completion.

## Preferred edit pattern
1) read_file / search_files (with role path filters)
2) apply_diff (surgical patch; reference `@/path`)
3) attempt_completion (include DoD evidence + citations)

## File creation
- Use write_to_file only for new files (never for small edits). Prefer apply_diff for changes.

## Command execution
- Use execute_command ONLY if your role has a whitelist in `.kilocode/rules-<role>/allowed_commands.md`.
- If the command is not whitelisted, ask_followup_question and propose adding it or route via SRE.

## MCP usage
- access_mcp_resource to read external resources; use_mcp_tool to execute actions on MCP servers.
- If MCP server is disconnected or unknown, fail fast with the missing server name.

## Progress & tracking
- Wrap steps with update_todo_list at start & end of meaningful phases.
- If required inputs (PRD/AC/planner/API_SPEC) are missing → ask_followup_question first, then new_task/switch_mode if needed.
