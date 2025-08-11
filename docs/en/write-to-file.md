# write_to_file

**Source**: https://kilocode.ai/docs/features/tools/write-to-file

## Overview
Concise summary of what **write_to_file** does in Kilo Code, when it is used, and how it relates to other tools.

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
Creates new files or **fully replaces** existing ones with an **interactive diff approval**. Use for **new files**; prefer `apply_diff` for edits.

## Parameters
- `path` (required), `content` (required), `line_count` (required).

## Key features
- Diff view with user edits; truncation detection; path/permission checks; cleans model artefacts.

## Limitations
- Slow on large files; full overwrite; interactive only; requires exact `line_count`.

## How it works
- Validate + preprocess content → open diff → wait for approval (and edits) → write and confirm.
