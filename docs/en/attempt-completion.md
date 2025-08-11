# attempt_completion

**Source**: https://kilocode.ai/docs/features/tools/attempt-completion

## Overview
Concise summary of what **attempt_completion** does in Kilo Code, when it is used, and how it relates to other tools.

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
Signals **task completion** with a concise result; can optionally run **one demo command** (with user approval). Always available.

## Parameters
- `result` (required), `command` (optional).

## Key features
- Special completion UI, feedback loop for refinement, telemetry, subtask completion flow.

## Limitations
- Not for partial progress; one command only; command requires approval.

## How it works
- Present result (strip closing XML tags internally) → (optionally) request to run command → capture feedback → continue/finish.
