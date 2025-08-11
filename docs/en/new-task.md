# new_task

**Source**: https://kilocode.ai/docs/features/tools/new-task

## Overview
Concise summary of what **new_task** does in Kilo Code, when it is used, and how it relates to other tools.

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
Creates a **subtask** with its **own mode** and conversation history; pauses the parent; returns results on completion.

## Parameters
- `mode` (required), `message` (required).

## Key features
- Hierarchical task stack, telemetry, user approval for creation, clear transitions in UI.

## Limitations
- Existing modes only; deep nesting adds complexity; requires explicit completion to resume parent.

## How it works
- Validate & verify mode → create child task context → switch to mode → on completion pass results back and resume parent.
