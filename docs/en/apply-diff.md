# apply_diff

**Source**: https://kilocode.ai/docs/features/tools/apply-diff

## Overview
Concise summary of what **apply_diff** does in Kilo Code, when it is used, and how it relates to other tools.

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
Performs **surgical edits** to existing files using a **diff block** with **line numbers** (MultiSearchReplaceDiffStrategy). Prefer this for **small changes**.

## Parameters
- `path` (required), `diff` (required; includes `:start_line:` markers).

## Key features
- Fuzzy matching with thresholds (≈0.8–1.0), context `BUFFER_LINES` (~40), overlap windows, formatting/indent preservation, diff preview, `.kilocodeignore` checks, mistake counters per file.

## Limitations
- Requires distinct target text; large/ambiguous files may need manual review.

## How it works
- Validate → check `.kilocodeignore` → load file → locate matches → prepare patch → **user reviews diff** → apply if approved.
