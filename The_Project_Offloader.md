# The Project Offloader (Gatekeeper)

This file is the **gatekeeper** and the top of the repo’s enforcement stack.

It is intentionally **thin**. Detailed truth lives in:
- Governance/state: `docs/ssot/*`
- Architecture: `docs/architecture/*`
- Contracts: `docs/contracts/*`
- Quality: `docs/quality/*`
- Decisions: `docs/decisions/*`

## 0) Non-negotiable Git Gate (must run first)
Before any file changes, run (read-only):
- `git status`
- `git diff --stat`
- `git diff --stat --staged`
- `git log --since="24 hours ago" --oneline`

If the repo is dirty or attribution is unclear: **STOP** and resolve (commit/stash/discard/document) before proceeding.

## 1) Mandatory Interaction Format (for ANY file change)
1) RECAP (repo state + applicable rules)
2) REQUEST (user intent)
3) PROPOSAL (next milestone)
4) ADR CHECK (required? filename or justification)
5) IMPACTED FILES (exact paths)
6) CONFIRM (“Confirm to proceed?” and wait)

No modifications until confirmation.

## 2) Active / Frozen Versions
Exactly one ACTIVE version at a time. Published versions are FROZEN.

| Version | Status | Date | Notes |
|---|---|---:|---|
| v0.1.0 | ACTIVE | 2026-02-26 | Initial scaffold |

**Transition rule:** you cannot start the next ACTIVE version until the previous is published and marked FROZEN.

## 3) Read Order (every agent must do this first)
1) `docs/ssot/INDEX.md`
2) `docs/ssot/GOVERNANCE.md`
3) `docs/quality/TESTING.md`
4) `docs/quality/SECURITY.md`
5) `docs/contracts/API.md` and `docs/contracts/DB_SCHEMA.md`
6) `docs/decisions/*` (ADRs)

## 4) Update Obligations (when changing code)
If you change…
- API routes → update `docs/contracts/API.md`
- DB schema/migrations → update `docs/contracts/DB_SCHEMA.md`
- Security/auth/audit expectations → update `docs/quality/SECURITY.md` + ADR if meaningful
- Testing approach/commands → update `docs/quality/TESTING.md` + ADR if meaningful
- Governance/CI/branch rules → update `docs/ssot/GOVERNANCE.md` + ADR

## 5) Prompt to Resume This Project (required)
> “Read `The_Project_Offloader.md` fully and treat it as authoritative.  
> Follow the git gate. Read the split SSoT docs in the read order.  
> Respect ACTIVE vs FROZEN versions.  
> Use the mandatory interaction format and wait for confirmation before modifying files.  
> Update the relevant docs/contracts/ADRs whenever changes affect them.”
