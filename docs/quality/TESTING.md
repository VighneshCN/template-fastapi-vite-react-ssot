# Testing Strategy (SSoT)

## Backend (FastAPI)
Required:
- pytest
- FastAPI TestClient pattern
Commands:
- install: pip install -r requirements.txt -r requirements-dev.txt
- run: pytest -q

## Frontend (Vite/React)
Required:
- Vitest + React Testing Library
Commands (recommend lockfile; template uses npm install until lock exists):
- cd apps/web
- npm install
- npm run lint
- npm run test
- npm run build

## Evidence rule
Every PR must include test evidence:
- commands run
- pass/fail summary
