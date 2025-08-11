# list_files

**Source**: https://kilocode.ai/docs/features/tools/list-files

## Overview
Concise summary of what **list_files** does in Kilo Code, when it is used, and how it relates to other tools.

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
Lists files/dirs at a path; optionally **recursive**. Respects `.gitignore` and `.kilocodeignore` and avoids huge trees by truncating.

## Parameters
- `path` (required), `recursive` (optional).

## Key features
- Skips heavy dirs (`node_modules`, `.git`) recursively; caps at ~200 entries; 10s traversal timeout.

## Limitations
- Not for confirming just-created files; can't list root/home; perf limits on giant repos.

## How it works
- Validate → resolve path → traverse (with filters/timeouts) → format (dirs first, lock mark for ignored files).
