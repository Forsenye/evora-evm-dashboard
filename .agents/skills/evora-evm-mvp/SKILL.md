---
name: evora-evm-mvp
description: Use this skill when working on EVORA EVM Dashboard, a fullstack technical challenge using FastAPI, React, PostgreSQL and Earned Value Management calculations. Trigger this skill for repository setup, backend architecture, EVM calculation logic, frontend dashboard, tests, Docker, README, AI_PROCESS.md, Gitflow and release preparation.
---

# EVORA EVM MVP Skill

## Purpose
This skill guides the development of EVORA EVM Dashboard as a clean, testable, and documented fullstack MVP.

## Functional scope
- Project creation
- Project listing
- Project detail
- Project update
- Project deletion
- Activity creation
- Activity listing by project
- Activity update
- Activity deletion
- EVM calculation by activity
- Consolidated EVM calculation by project
- Dashboard with indicators and chart

## EVM indicators
- PV = planned_percentage * BAC
- EV = completed_percentage * BAC
- CV = EV - AC
- SV = EV - PV
- CPI = EV / AC
- SPI = EV / PV
- EAC = BAC / CPI
- VAC = BAC - EAC

Percentages must be normalized from 0-100 to decimal values before calculations.

## Edge cases
The system must handle:
- AC equals zero
- PV equals zero
- BAC equals zero
- Real progress equals zero
- Project without activities
- Invalid percentages below 0 or above 100
- Division by zero
- Empty activity list

When division is not possible, return null for the affected indicator and provide a clear interpretation.

## Backend architecture rules
Expected structure:
- backend/app/api/routes
- backend/app/core
- backend/app/db
- backend/app/models
- backend/app/schemas
- backend/app/services
- backend/app/repositories
- backend/tests

Rules:
- EVM logic must live in backend/app/services/evm_calculation_service.py
- API routes must only orchestrate requests and responses.
- Repositories must handle data access.
- Services must handle business rules.
- Schemas must define request and response contracts.

## Frontend architecture rules
Expected structure:
- frontend/src/api
- frontend/src/components
- frontend/src/pages
- frontend/src/services
- frontend/src/types
- frontend/src/routes

The dashboard must include:
- Project form
- Activity form
- Activity table
- Consolidated indicators cards
- CPI and SPI visual status
- PV, EV and AC comparison chart by activity

## Testing rules
Create unit tests for:
- PV calculation
- EV calculation
- CV calculation
- SV calculation
- CPI calculation
- SPI calculation
- EAC calculation
- VAC calculation
- AC equals zero
- PV equals zero
- BAC equals zero
- Empty activity list
- Invalid percentages

Create integration tests for:
- Create project
- List projects
- Get project detail
- Update project
- Delete project
- Create activity
- List activities by project
- Update activity
- Delete activity
- Get project EVM summary

## Documentation rules
Maintain:
- README.md
- AI_PROCESS.md
- docs/architecture.md
- docs/api.md
- docs/database.md

AI_PROCESS.md must include:
- AI tools used
- Chronological prompts
- How EVM was learned
- How formulas were validated
- Two cases where AI suggestions were not followed
- One independent architecture decision
- Final honest reflection

## Gitflow rules
Use:
- main
- develop
- feature/project-setup
- feature/codex-skill
- feature/backend-base
- feature/evm-calculation-service
- feature/projects-api
- feature/activities-api
- feature/frontend-dashboard
- feature/tests
- feature/docker-compose
- feature/documentation
- release/mvp-v1

Commits must be descriptive and imperative.

Good examples:
- Add Codex project instructions
- Add EVORA EVM skill
- Add project setup structure
- Add FastAPI backend base
- Add EVM calculation service
- Add project CRUD endpoints
- Add activity dashboard table
- Add EVM unit tests
- Add Docker Compose setup
- Add AI process documentation

Bad examples:
- fix
- cambios
- wip
- prueba