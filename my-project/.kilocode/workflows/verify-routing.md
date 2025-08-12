# /verify-routing.md

**Goal:** Ensure orchestrator routes to the most specific `code-*` specialization.

## Checks
- Confirm presence of `code-nextjs`, `code-fastapi`, `code-python`, `code-nestjs` in `.kilocodemodes`.
- For a Next.js change request, orchestrator must select `code-nextjs` (framework precedence).

## Acceptance
- A dry-run task shows selected mode and rationale with `[[n]]` pointing to `.kilocodemodes` lines.
