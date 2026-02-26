# Architecture Overview

## System boundaries
- Backend: FastAPI (apps/api)
- Frontend: Vite + React (apps/web)
- DB: SQLite for MVP; planned migration to Postgres

## Data flow (placeholder)
Browser (React) ↔ API (FastAPI) ↔ DB (SQLite/Postgres)

## Deployment targets (placeholder)
- Local dev
- CI
- Windows desktop packaging (optional)
