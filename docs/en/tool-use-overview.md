# Tool Use Overview

**Source**: https://kilocode.ai/docs/features/tools/tool-use-overview

## Overview
Concise summary of what **Tool Use Overview** does in Kilo Code, when it is used, and how it relates to other tools.

## Parameters
- See the official page for the complete parameter list and validation rules.

## What it does
- Practical description of the tool’s behavior and effect in the workspace.

## When to use
- Situations and decision criteria to invoke this tool.

## Key features
- Notable capabilities and safety properties.

## Limitations
- Known constraints and performance or security boundaries.

## How it works (flow)
- High-level steps from parameter validation to execution and result handling.

## Best practices
- Combine with related tools in typical patterns.

## Examples
- Short scenarios or XML-style invocation snippets.

## Overview
Kilo Code exposes a **tool system** that is grouped by purpose: **read**, **edit**, **browser**, **command**, **MCP**, and **workflow**. Some tools are **Always Available** in any mode: `ask_followup_question`, `attempt_completion`, `switch_mode`, `new_task`, `update_todo_list`.

## Key features
- **Mode-based gating**: `isToolAllowedForMode(tool, modeSlug, customModes, ...)` checks permissions before a call. 
- **Decision process**: mode validation → requirement checks (capabilities, permissions) → parameter validation.
- **Security layers**: file-system restrictions, command allowlists, network access controls.
- **Common patterns**: Info—`ask_followup_question → read_file → search_files`; Code—`read_file → apply_diff → attempt_completion`; Task—`new_task → switch_mode → execute_command`; Progress—`update_todo_list → execute_command → update_todo_list`.

## How it works (flow)
- Tools are invoked by direct needs, mode availability, or context triggers, with success/error handling and recovery strategies (retries, fallbacks).
