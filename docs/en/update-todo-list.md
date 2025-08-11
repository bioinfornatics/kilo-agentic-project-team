# update_todo_list

**Source**: https://kilocode.ai/docs/features/tools/update-todo-list

## Overview
Concise summary of what **update_todo_list** does in Kilo Code, when it is used, and how it relates to other tools.

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
Replaces the entire **TODO checklist** with updated statuses (`[ ]`, `[-]`, `[x]`). Drives progress visibility.

## Parameters
- `todos` (required): markdown checklist.

## Key features
- Single-level list, batch updates, persistent reminders, reordering.

## Limitations
- No nesting/dependencies/scheduling; full replacement each update.

## How it works
- Validate & parse → replace list → integrate reminders → continue tracking.
