# FastAPI + Vite/React Stack Playbook (v1.2)

Scope:
- Monorepo: apps/api (FastAPI) + apps/web (Vite/React)
- DB: SQLite for MVP, migrate to Postgres via ADR
- Auth baseline: Email OTP -> JWT issuance
- Audit baseline: DB table audit_events

Pinned modules (see docs/ssot/PLAYBOOK_PIN.md):
- Execution Workflow Guidelines: docs/playbooks/EXECUTION_WORKFLOW_GUIDELINES.md
- Build Excellence (packaging): docs/playbooks/BUILD_PROMPT_EXCELLENCE.md

Release policies:
- Release builds must set PyInstaller EXE `console=False`
- Exclude tkinter unless explicitly required (license dialog etc.)

Conventions:
- Keep routers thin; logic in services
- Keep contracts updated: API.md + DB_SCHEMA.md
- ADR required for security/auth/audit/DB-migration/CI-governance/testing-strategy changes
