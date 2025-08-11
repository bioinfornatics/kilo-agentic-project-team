# browser_action

**Source**: https://kilocode.ai/docs/features/tools/browser-action

## Overview
Concise summary of what **browser_action** does in Kilo Code, when it is used, and how it relates to other tools.

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
Automates a Chromium browser via Puppeteer. Actions: `launch`, `click`, `type`, `scroll_{down|up}`, `close` with **screenshot feedback** each step.

## Parameters
- `action` (required), `url` (for `launch`), `coordinate` (for `click`), `text` (for `type`).

## Key features
- Local vs **remote** session, console logs capture, DOM stability wait, action history.

## Limitations
- Single-tool lock while active; viewport-relative clicks; must `close` before other tools; Chrome/Chromium only.

## How it works
- Validate & (launch/manage) session → interact → capture screenshots/logs → close.
