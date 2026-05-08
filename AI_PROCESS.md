# AI_PROCESS

## Project

EVORA EVM Dashboard

## AI tools used

- Codex (GPT-5)

## Chronological prompts

### Prompt 1

```text
Actuas a senior fullstack software architect and repository setup engineer. 

You are working inside the repository evora-evm-dashboard.

Your task is to create the Codex project instructions and the reusable Codex Skill for this technical challenge.

Project context:
EVORA EVM Dashboard is a fullstack technical challenge for Trycore Colombia. The application must manage projects and activities, calculate Earned Value Management indicators, expose a REST API, provide a React dashboard, include tests, use Gitflow, and document the AI-assisted process.

Important:
Do not implement the application business logic yet.
Do not create the complete backend or frontend yet.
This task is only for creating the Codex guidance files and the project skill.

Create the following files:

1. AGENTS.md at the repository root.
2. .agents/skills/evora-evm-mvp/SKILL.md
3. AI_PROCESS.md if it does not exist.
4. docs/prompts/001-create-codex-skill.md

Content requirements for AGENTS.md:

- Explain that the project is EVORA EVM Dashboard.
- Define the stack:
  - Backend: Python 3.11, FastAPI, SQLAlchemy, Pydantic, PostgreSQL, Pytest.
  - Frontend: React, Vite, TypeScript, Tailwind CSS, Recharts.
  - DevOps: Docker, Docker Compose.
- Define quality rules:
  - Business logic must not live inside API route handlers.
  - EVM calculations must live in EvmCalculationService.
  - Use descriptive names.
  - Avoid commented dead code.
  - Avoid unused variables.
  - Avoid magic numbers and magic strings.
  - Use environment variables for configuration.
  - Do not hardcode credentials.
  - Keep README.md and AI_PROCESS.md updated.
- Define testing rules:
  - Unit tests for all EVM calculation logic.
  - Integration tests for each endpoint contract.
  - Minimum 80 percent coverage over business logic.
- Define Gitflow:
  - main for production.
  - develop for integration.
  - feature/* for features.
  - release/* before final merge to main.
- Define commit message rules:
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

Content requirements for .agents/skills/evora-evm-mvp/SKILL.md:

Use this frontmatter exactly:

---
name: evora-evm-mvp
description: Use this skill when working on EVORA EVM Dashboard, a fullstack technical challenge using FastAPI, React, PostgreSQL and Earned Value Management calculations. Trigger this skill for repository setup, backend architecture, EVM calculation logic, frontend dashboard, tests, Docker, README, AI_PROCESS.md, Gitflow and release preparation.
---

After the frontmatter, include the following sections:

# EVORA EVM MVP Skill

## Purpose
Explain that this skill guides the development of EVORA EVM Dashboard as a clean, testable and documented fullstack MVP.

## Functional scope
Include:
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
Document these formulas:
- PV = planned_percentage * BAC
- EV = completed_percentage * BAC
- CV = EV - AC
- SV = EV - PV
- CPI = EV / AC
- SPI = EV / PV
- EAC = BAC / CPI
- VAC = BAC - EAC

Clarify that percentages must be normalized from 0-100 to decimal values before calculations.

## Edge cases
Define how the system must handle:
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
Use this expected structure:
- backend/app/api/routes
- backend/app/core
- backend/app/db
- backend/app/models
- backend/app/schemas
- backend/app/services
- backend/app/repositories
- backend/tests

State clearly:
- EVM logic must live in backend/app/services/evm_calculation_service.py
- API routes must only orchestrate requests and responses.
- Repositories must handle data access.
- Services must handle business rules.
- Schemas must define request and response contracts.

## Frontend architecture rules
Use this expected structure:
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

Content requirements for AI_PROCESS.md:

Create the initial structure only. Include:
- Project: EVORA EVM Dashboard
- AI tools used
- Chronological prompts
- How I learned EVM
- How I validated formulas
- AI suggestions I did not follow
- Independent architecture decision
- Final reflection

Add this current prompt as the first chronological prompt entry. Do not summarize it. Store it in a clear Markdown block.

Content requirements for docs/prompts/001-create-codex-skill.md:

Save this same prompt in full, exactly as received, so the project has traceability of the first AI-assisted action.

Validation requirements:

After creating the files:
- Show the created file tree.
- Summarize the purpose of each file.
- Do not generate backend or frontend application code yet.
- Do not install dependencies yet.
- Do not push to GitHub.
```

## How I learned EVM

- Pending documentation update during implementation phase.

## How I validated formulas

- Pending documentation update during implementation phase.

## AI suggestions I did not follow

- Pending documentation update during implementation phase.
- Pending documentation update during implementation phase.

## Independent architecture decision

- Pending documentation update during implementation phase.

## Final reflection

- Pending documentation update during implementation phase.