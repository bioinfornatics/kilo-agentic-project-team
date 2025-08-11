# Edit Safety Policy
**severity:** high • **category:** safety • **owners:** platform

## When
- Any file edit in repo

## Checks
- Enforce **file_scope_regex** from current mode.
- Forbid destructive operations (`rm -rf /`, `DROP TABLE`, `git reset --hard`).

## Action on violation
- **Block edit** and instruct safe alternative or sandboxed path.
