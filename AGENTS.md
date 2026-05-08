# AGENTS.md

## Project

This repository contains **EVORA EVM Dashboard**, a fullstack technical challenge for Trycore Colombia.

## Stack

- Backend: Python 3.11, FastAPI, SQLAlchemy, Pydantic, PostgreSQL, Pytest
- Frontend: React, Vite, TypeScript, Tailwind CSS, Recharts
- DevOps: Docker, Docker Compose

## Quality rules

- Business logic must not live inside API route handlers.
- EVM calculations must live in `EvmCalculationService`.
- Use descriptive names.
- Avoid commented dead code.
- Avoid unused variables.
- Avoid magic numbers and magic strings.
- Use environment variables for configuration.
- Do not hardcode credentials.
- Keep `README.md` and `AI_PROCESS.md` updated.

## Testing rules

- Unit tests for all EVM calculation logic.
- Integration tests for each endpoint contract.
- Minimum 80 percent coverage over business logic.

## Gitflow

- `main` for production.
- `develop` for integration.
- `feature/*` for features.
- `release/*` before final merge to `main`.

## Commit message rules

- Commits must be in English.
- Commits must be descriptive.
- Commits must use imperative mood.
- Valid examples:
  - Add project setup structure
  - Add EVM calculation service
  - Add activity CRUD endpoints
  - Fix CPI edge case when AC is zero
- Invalid examples:
  - fix
  - cambios
  - wip
  - prueba