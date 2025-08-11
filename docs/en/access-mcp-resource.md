# access_mcp_resource

**Source**: https://kilocode.ai/docs/features/tools/access-mcp-resource

## Overview
Concise summary of what **access_mcp_resource** does in Kilo Code, when it is used, and how it relates to other tools.

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
Retrieves **resources** (text/images/structured) from an MCP server by **URI**. It is **read‑only** (contrast with `use_mcp_tool`).

## Parameters
- `server_name` (required) — MCP server id.
- `uri` (required) — resource identifier (supports **standard** resources and **resource templates**).

## Key features
- User approval, timeouts, connection‑state checks, and proper rendering of content types.

## Limitations
- Depends on connected servers; no offline/cache; URIs follow server-specific formats.

## How it works
- Validate hub/server/enablement → request `resources/read` via MCP SDK → return structured content for context.
