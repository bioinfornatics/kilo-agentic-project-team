# search_files

**Source**: https://kilocode.ai/docs/features/tools/search-files

## Overview
Concise summary of what **search_files** does in Kilo Code, when it is used, and how it relates to other tools.

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
Performs **regex** searches (Ripgrep) with 1‑line context before/after. Optional **glob** filter by file type/pattern.

## Parameters
- `path` (required), `regex` (required), `file_pattern` (optional).

## Key features
- Caps ~300 matches; truncates very long lines; merges nearby hits.

## Limitations
- Text-only; Rust regex flavor; default context size fixed.

## How it works
- Validate → resolve path → run rg with filters → format grouped results.
