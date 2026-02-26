# Execution Workflow Guidelines (AI + Humans) — v1.2

This document defines **how work is executed** in this repo so changes are safe, test-gated, documented, and reproducible across humans and AI agents.

These guidelines are intentionally **process-oriented**. Domain truth belongs in split SSoT docs (`docs/ssot`, `docs/contracts`, `docs/quality`, `docs/architecture`) and decisions belong in ADRs (`docs/decisions`).

---

## 0) Authority & Precedence

If there is a conflict, the higher authority wins:

1) `The_Project_Offloader.md` (gatekeeper protocol: git gate + interaction format + version rules)
2) `docs/ssot/*` (governance + project state + playbook pin)
3) `docs/contracts/*`, `docs/quality/*`, `docs/architecture/*` (truth by domain)
4) `docs/decisions/*` (ADRs)
5) This file (execution discipline)
6) Chat instructions (lowest)

If two authoritative docs conflict, propose an ADR or fix the docs.

---

## 1) Definitions (so “non-trivial” isn’t subjective)

**File-changing work**: anything that would create/modify repo files or propose a commit/PR.

**Non-trivial change**: any change that affects at least one of:
- architecture boundaries or module structure
- auth/security/audit expectations
- data model/migrations, or SQLite→Postgres migration plan
- API contracts/versioning
- CI/gating/governance/testing strategy
- frontend architecture/tooling choices (routing/state/testing/build)
- any change with notable user-facing or operational risk

**Milestone**: a small, reviewable slice that can be tested and documented.

---

## 2) Non-negotiable Safety Gates

### 2.1 Git cleanliness + attribution gate (always first)
Before any file-changing work, run (read-only):
- `git status`
- `git diff --stat`
- `git diff --stat --staged`
- `git log --since="24 hours ago" --oneline`

If the repo is dirty or attribution is unclear:
- Summarize what changed (files + short descriptions)
- Ask how to resolve (commit/stash/discard/document)
- **STOP until resolved**

### 2.2 Mandatory Interaction Format (for ANY file-changing work)
For any file-changing work, the agent must output:

1) **RECAP**
   - repo state (git summary)
   - applicable rules to follow (cite exact doc paths)
2) **REQUEST**
   - restate what the user wants
3) **PROPOSAL**
   - next atomic milestone
4) **ADR CHECK**
   - ADR required? Yes/No
   - If Yes: propose ADR filename(s) to create/update before implementation
   - If No: one-sentence justification
5) **IMPACTED FILES**
   - exact file paths to create/modify
6) **CONFIRM**
   - ask “Confirm to proceed?” and wait

No modifications before confirmation.

---

## 3) Planning Discipline (what to do before code)

### 3.1 Pre-implementation validation (required for non-trivial work)
Before implementing:
- Clarify requirements and acceptance criteria
- Identify edge cases and failure modes
- Identify security/privacy concerns
- Identify data migration/rollback concerns
- Identify compatibility concerns (versions, build targets)
- Confirm “Definition of Done” for the milestone

If anything is unclear, ask targeted questions and propose reasonable defaults.

### 3.2 Reuse-first rule (avoid duplication)
Before writing new code:
- Search for existing helpers/utilities/modules
- Prefer extension over duplication
- If duplication is unavoidable, document why in PR description

---

## 4) Change Sequencing (avoid “everything at once”)

### 4.1 Keep changes small and single-intent
Rules:
- One dominant intent per milestone/PR
- Avoid mixing refactor + new behavior in one change set
- Prefer incremental commits with clear messages

### 4.2 “Bootstrap vs Feature vs Release” modes
- **Bootstrap mode**: create/align docs, CI, templates, repo rails. No business logic.
- **Feature mode**: implement one slice, add tests, update docs/contracts/ADRs.
- **Release mode**: run release checklist, build artifacts, sign, freeze version.

---

## 5) ADR Discipline (Decision Records)

### 5.1 ADR required triggers
Create an ADR when change affects:
- architecture boundaries / module structure
- auth/security/audit policy
- data model/migrations or SQLite→Postgres plan
- API contract versioning or breaking changes
- CI/gating/governance/testing strategy changes
- frontend architecture shifts (routing/state/tooling/testing/build)
- packaging/toolchain changes (PyInstaller profile changes, signing policy)

### 5.2 ADR workflow
- Create `docs/decisions/ADR-XXXX-<slug>.md` using the ADR template
- Link ADR in PR template
- If ADR not required, explicitly justify in PR (“No ADR required because…”)

---

## 6) Testing & Evidence (must be mechanical)

### 6.1 Source of truth
`docs/quality/TESTING.md` defines:
- required test layers
- required commands (local + CI)
- what counts as “test evidence”

### 6.2 Backend (FastAPI) standards
- Unit tests for pure logic
- Endpoint tests with `TestClient`
- Prefer dependency overrides for auth/db boundaries
- Any new router/service must have at least one representative test

### 6.3 Frontend (Vite/React) standards
- Component tests using React Testing Library
- Vitest + jsdom for unit/component tests
- Add smoke tests for critical flows as app grows
- Build must succeed (`npm run build`) before merge

### 6.4 PR evidence requirements
PR must include:
- commands run
- summary of results (pass/fail)
- CI status (when CI exists)

---

## 7) Documentation Update Obligations (drift control)

When you change:
- endpoints/routes → update `docs/contracts/API.md`
- DB schema/migrations → update `docs/contracts/DB_SCHEMA.md`
- test strategy/commands → update `docs/quality/TESTING.md`
- security/auth/audit policy → update `docs/quality/SECURITY.md` (+ ADR if meaningful)
- architecture boundaries → update `docs/architecture/*` (+ ADR if meaningful)
- governance/CI rules → update `docs/ssot/GOVERNANCE.md` (+ ADR if meaningful)

Rules:
- Never keep “truth” only in chat.
- Avoid huge docs: keep single markdown files under ~300 lines; split and link via `docs/ssot/INDEX.md`.

---

## 8) PR & Review Hygiene (even if PRs aren’t created in-chat)

Use `.github/PULL_REQUEST_TEMPLATE.md` as the structure:
- Scope / Why / Non-goals
- Alternatives considered (brief)
- Risks / rollback
- Tests run + evidence
- Docs updated checklist
- ADR link or justification

---

## 9) Definition of Done (per milestone)
A milestone is Done when:
- [ ] Scope is clear, single-intent
- [ ] Tests added/updated and pass
- [ ] Test evidence recorded
- [ ] Docs/contracts updated if impacted
- [ ] ADR created/linked if required (or justified as not required)
- [ ] CI passes (or it’s a known bootstrap limitation recorded as TODO)

---

## 10) When to STOP and ask the user
Stop and ask before proceeding if:
- repo state is dirty/undocumented
- requirements or acceptance criteria are unclear
- a change might cause data loss/security risk without explicit approval
- the change triggers an ADR but the decision isn’t made yet
- build/release/signing requires credentials/secrets/actions the agent cannot perform