# list_code_definition_names

**Source**: https://kilocode.ai/docs/features/tools/list-code-definition-names

## Overview
Concise summary of what **list_code_definition_names** does in Kilo Code, when it is used, and how it relates to other tools.

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
Builds a **structural map** of top-level definitions (classes, functions, interfaces) in a directory using Tree‑sitter. Great for refactor planning.

## Parameters
- `path` (required).

## Key features
- Shows **line numbers + code snippets**; supports many languages; caps at ~50 files; non-recursive.

## Limitations
- Top-level only; parser variability; no usage relationships.

## How it works
- Validate → scan top-level files → parse (AST queries) → sort and print definitions.
