# Governance (Enforceable)

## Merge gates (required for main)
- PR required
- CI must pass
- Tests required (per `docs/quality/TESTING.md`)
- Test evidence must be included in PR (commands + results)
- Docs updated when relevant (SSoT/contracts/quality/architecture)

## Working discipline
- No progressing on a dirty git state for changes intended to merge.
- Small, reviewable changesets.

## ADR policy
ADR REQUIRED for changes affecting:
- architecture boundaries
- auth/security/audit policy
- data model or migrations
- API contract decisions/versioning
- CI/gating/governance/testing strategy changes

PR must include:
- ADR link, OR
- explicit “ADR not required because …” justification.

## Versioning
- One ACTIVE version at a time.
- Published versions are FROZEN.
- Version transitions must be recorded in the Offloader version table + changelog.
