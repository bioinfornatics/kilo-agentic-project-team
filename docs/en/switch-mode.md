# switch_mode

**Source**: https://kilocode.ai/docs/features/tools/switch-mode

## Overview
Concise summary of what **switch_mode** does in Kilo Code, when it is used, and how it relates to other tools.

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
Requests a **mode change** to adapt toolsets and prompts for the next phase. Keeps context; needs **user approval**.

## Parameters
- `mode_slug` (required), `reason` (optional).

## Key features
- Enforces mode restrictions; 500ms settle delay; works with core & custom modes.

## Limitations
- Cannot switch to non-existent modes; file restrictions may apply (e.g., Architect edits only `.md`).

## How it works
- Validate & present → on approval activate new mode and continue.
