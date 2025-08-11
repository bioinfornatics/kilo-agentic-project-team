# execute_command

**Source**: https://kilocode.ai/docs/features/tools/execute-command

## Overview
Concise summary of what **execute_command** does in Kilo Code, when it is used, and how it relates to other tools.

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
Runs **CLI commands** in a managed VS Code terminal with security checks (shell-quote parsing, `.kilocodeignore`, allowlists).

## Parameters
- `command` (required), `cwd` (optional).

## Key features
- Terminal reuse & state, real-time output, long-running processes, exit-code & signal mapping, interactive apps support.

## Limitations
- OS differences; elevated privileges may require user setup; remote dev quirks.

## How it works
- Validate/secure → create/reuse terminal → run → capture output/exit code → return status.
