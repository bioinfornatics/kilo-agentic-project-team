# read_file

**Source**: https://kilocode.ai/docs/features/tools/read-file

## Overview
Concise summary of what **read_file** does in Kilo Code, when it is used, and how it relates to other tools.

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
Reads a file (or line range) and adds **line numbers**. Can extract text from **PDF/DOCX/IPYNB**; supports **auto-truncation** for very large files.

## Parameters
- `path` (required), `start_line`/`end_line` (optional), `auto_truncate` (optional).

## Key features
- Range-first policy; summaries with method ranges for truncated reads.

## Limitations
- Large files without ranges may be slow; binary formats limited.

## How it works
- Validate → resolve → choose strategy (range > auto-trunc > full) → process and number lines.
