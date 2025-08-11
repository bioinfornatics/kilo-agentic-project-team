# use_mcp_tool

**Source**: https://kilocode.ai/docs/features/tools/use-mcp-tool

## Overview
Concise summary of what **use_mcp_tool** does in Kilo Code, when it is used, and how it relates to other tools.

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
Executes a **tool** exposed by an MCP server with validated **arguments**. Extends Kilo with domain-specific capabilities.

## Parameters
- `server_name` (required), `tool_name` (required), `arguments` (JSON, schema‑validated).

## Key features
- Dual transports (stdio/SSE), Zod validations, content types (text/image/resource), timeouts, auto-restarts, always‑allow list.

## Limitations
- Server/tool availability & network reliability; one MCP op at a time; approval unless whitelisted.

## How it works
- Validate hub/server/tool/args → select transport → execute → format response (and chain with `access_mcp_resource` for resources).
