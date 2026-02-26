# Backend Architecture (FastAPI)

## Suggested structure
- main.py (app init)
- routers/ (HTTP routes)
- services/ (business logic)
- models/ (SQLAlchemy)
- schemas/ (Pydantic)
- db/ (engine/session + migrations)
- core/ (settings/logging/security helpers)

## Conventions (placeholders)
- Dependency injection via FastAPI dependencies
- Keep routers thin; put logic in services
