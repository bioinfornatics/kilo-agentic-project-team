# ask_followup_question

**Source**: https://kilocode.ai/docs/features/tools/ask-followup-question

## Overview
Concise summary of what **ask_followup_question** does in Kilo Code, when it is used, and how it relates to other tools.

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
Asks a **single targeted question** with optional **suggested answers** to close information gaps. Always available.

## Parameters
- `question` (required), `follow_up` (optional XML `<suggest>` list).

## Key features
- Presents interactive choices, wraps user response in `<answer>…</answer>`, maintains history, resets mistake counters.

## Limitations
- One question per call; suggestions must be complete; no enforced schema on answers.

## How it works
- Parse question + suggestions → transform to JSON for UI → collect answer (text/images) → proceed with task.
