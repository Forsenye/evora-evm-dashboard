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

### Prompt 2

```text
Usa la skill EVORA MVP Builder.

Estamos en el proyecto EVORA, repositorio evora-evm-dashboard.

Objetivo de esta tarea:
Implementar la lógica central de Valor Ganado en el backend mediante el servicio EvmCalculationService y crear pruebas unitarias sólidas para validar los cálculos y los casos borde.

Rama esperada:
feature/evm-calculation-service

Antes de modificar archivos:
1. Ejecuta git status.
2. Ejecuta git branch.
3. Confirma que estás en feature/evm-calculation-service.
4. Si no estás en esa rama, indícalo y sugiere el comando correcto.

Archivos principales:
- backend/app/services/evm_calculation_service.py
- backend/app/schemas/evm_schema.py
- backend/tests/unit/test_evm_calculation_service.py
- AI_PROCESS.md
- README.md

Implementa el servicio:
backend/app/services/evm_calculation_service.py

Debe existir una clase:

EvmCalculationService

Con estos métodos:

1. calculate_activity_indicators(activity_input)
2. calculate_project_summary(activities)
3. interpret_cpi(cpi)
4. interpret_spi(spi)

La lógica debe calcular por actividad:

PV = (planned_progress / 100) * BAC
EV = (actual_progress / 100) * BAC
CV = EV - AC
SV = EV - PV
CPI = EV / AC
SPI = EV / PV
EAC = BAC / CPI
VAC = BAC - EAC

Reglas obligatorias:

1. planned_progress y actual_progress llegan como valores entre 0 y 100.
2. No dividir por cero.
3. Si actual_cost es 0, CPI debe ser None.
4. Si PV es 0, SPI debe ser None.
5. Si CPI es None o CPI es 0, EAC debe ser None.
6. Si EAC es None, VAC debe ser None.
7. Si actual_progress es 0, EV debe ser 0.
8. Si actual_progress es 0 y actual_cost es mayor que 0, CPI debe ser 0.
9. Para proyecto sin actividades, retornar resumen controlado con totales en 0 e indicadores no calculables en None.
10. Para consolidado de proyecto, no promediar CPI ni SPI de actividades.
11. Para consolidado, sumar BAC, PV, EV y AC; luego calcular CPI, SPI, EAC y VAC sobre los totales.

Interpretación CPI:

- CPI > 1: "Eficiente en costos"
- CPI == 1: "En presupuesto"
- CPI < 1: "Sobre presupuesto"
- CPI is None: "No calculable"

Interpretación SPI:

- SPI > 1: "Adelantado"
- SPI == 1: "En cronograma"
- SPI < 1: "Atrasado"
- SPI is None: "No calculable"

Crea o ajusta schemas en:
backend/app/schemas/evm_schema.py

Define modelos Pydantic para representar:

1. ActivityEvmIndicators
2. ProjectEvmSummary
3. EvmStatus

Usa nombres técnicos claros en inglés.

Crea pruebas unitarias en:
backend/tests/unit/test_evm_calculation_service.py

Las pruebas deben validar números reales, no solo que una función retorna algo.

Casos mínimos obligatorios:

1. calculate PV correctly.
2. calculate EV correctly.
3. calculate CV correctly.
4. calculate SV correctly.
5. calculate CPI when actual_cost is greater than zero.
6. return CPI None when actual_cost is zero.
7. calculate SPI when PV is greater than zero.
8. return SPI None when PV is zero.
9. return EAC when CPI is valid.
10. return EAC None when CPI is None.
11. return VAC when EAC is valid.
12. return VAC None when EAC is None.
13. handle actual_progress equals zero.
14. handle project without activities.
15. calculate consolidated project summary correctly.
16. verify consolidated CPI and SPI are calculated from totals, not averages.
17. interpret CPI greater than 1.
18. interpret CPI equal to 1.
19. interpret CPI less than 1.
20. interpret SPI greater than 1.
21. interpret SPI equal to 1.
22. interpret SPI less than 1.

Usa pytest.

Ejecuta:

cd backend
pytest tests/unit/test_evm_calculation_service.py

Si existe configuración de coverage, ejecuta también:

pytest --cov=app tests/unit/test_evm_calculation_service.py

Actualiza README.md con una sección breve:

## EVM Calculation Service

Explica:
- ubicación del servicio
- indicadores calculados
- cómo ejecutar las pruebas unitarias

Actualiza AI_PROCESS.md:
1. Agrega este prompt completo como el siguiente prompt cronológico.
2. Documenta que se implementó EvmCalculationService.
3. Documenta la decisión técnica de no promediar CPI/SPI para el consolidado.
4. Documenta la decisión de retornar None cuando CPI/SPI no sean calculables.

No agregues:
- AWS
- EC2
- Docker Compose nuevo si no existe
- autenticación
- roles
- frontend
- endpoints nuevos en esta tarea

Al finalizar, reporta:
1. Rama usada.
2. Archivos modificados.
3. Resumen técnico.
4. Pruebas ejecutadas.
5. Resultado de pruebas.
6. Pendientes.
7. Commit sugerido.

Commit sugerido:

Add EVM calculation service
```

### Prompt 3

```text
Usa la skill EVORA MVP Builder.

Estamos en el proyecto EVORA, repositorio evora-evm-dashboard.

Objetivo de esta tarea:
Implementar el CRUD backend para proyectos usando FastAPI, SQLAlchemy, Pydantic y arquitectura por capas.

Rama esperada:
feature/backend-project-crud

Antes de modificar archivos:
1. Ejecuta git status.
2. Ejecuta git branch.
3. Confirma que estás en feature/backend-project-crud.
4. Si no estás en esa rama, indícalo y sugiere el comando correcto.
5. No trabajes directamente sobre main ni develop.

Contexto:
El desafío técnico solicita una API REST para gestionar proyectos y actividades. En esta tarea solo debes implementar el CRUD de proyectos. No implementes todavía CRUD de actividades ni frontend.

Endpoints requeridos:

POST /api/v1/projects
GET /api/v1/projects
GET /api/v1/projects/{project_id}
PUT /api/v1/projects/{project_id}
DELETE /api/v1/projects/{project_id}

Arquitectura obligatoria:
- Las rutas deben vivir en backend/app/routes/project_routes.py.
- Los schemas deben vivir en backend/app/schemas/project_schema.py.
- El modelo SQLAlchemy debe vivir en backend/app/models/project.py.
- La lógica de acceso a datos debe vivir en backend/app/repositories/project_repository.py.
- No pongas lógica de base de datos directamente en routes.
- No pongas lógica de negocio dentro de routes.
- Mantén nombres técnicos en inglés.
- Mantén documentación y mensajes explicativos en español cuando aplique.

Modelo Project:
Debe tener como mínimo:

- id: UUID, primary key
- name: string, obligatorio, máximo 150 caracteres
- description: string opcional
- created_at: datetime
- updated_at: datetime

Reglas:
1. El nombre del proyecto es obligatorio.
2. El nombre no debe estar vacío.
3. La descripción es opcional.
4. Si el proyecto no existe, retornar HTTP 404.
5. Si el request es inválido, retornar HTTP 422.
6. DELETE debe retornar HTTP 204 si elimina correctamente.
7. No uses datos sensibles reales.
8. No quemes credenciales.
9. No agregues autenticación.
10. No agregues roles.
11. No agregues AWS, EC2 ni configuración cloud.
12. No agregues Docker Compose nuevo en esta tarea.

Schemas Pydantic requeridos:
Crear o ajustar en backend/app/schemas/project_schema.py:

1. ProjectBase
2. ProjectCreate
3. ProjectUpdate
4. ProjectResponse

ProjectCreate:
- name requerido
- description opcional

ProjectUpdate:
- name opcional
- description opcional

ProjectResponse:
- id
- name
- description
- created_at
- updated_at

Repository:
Crear o ajustar en backend/app/repositories/project_repository.py métodos claros:

1. create_project
2. get_projects
3. get_project_by_id
4. update_project
5. delete_project

Routes:
Crear o ajustar en backend/app/routes/project_routes.py:

1. POST /api/v1/projects
2. GET /api/v1/projects
3. GET /api/v1/projects/{project_id}
4. PUT /api/v1/projects/{project_id}
5. DELETE /api/v1/projects/{project_id}

Cada endpoint debe incluir:
1. response_model.
2. status_code cuando aplique.
3. descripción clara para Swagger.
4. manejo de 404 cuando el proyecto no exista.
5. uso de Depends para obtener sesión de base de datos.

Main:
Asegura que backend/app/main.py incluya el router de proyectos.

Swagger:
Debe seguir disponible en:
- /swagger-ui

OpenAPI:
Debe seguir disponible en:
- /api-docs.json

Pruebas de integración:
Crear o ajustar:
backend/tests/integration/test_project_endpoints.py

Debe incluir pruebas para:

1. create project successfully.
2. list projects successfully.
3. get project by id successfully.
4. return 404 when project does not exist.
5. update project successfully.
6. delete project successfully.
7. validate project name is required.

Las pruebas deben validar:
- status code.
- estructura del response.
- campos principales.
- comportamiento 404.
- comportamiento 422.

No crees pruebas vacías.
No crees pruebas que solo validen que algo retorna algo.
Las pruebas deben validar contrato real de API.

Si el proyecto todavía no tiene configuración completa de base de datos para tests, crea una configuración mínima y limpia para pruebas usando SQLite en memoria solo para testing, sin afectar PostgreSQL como base objetivo del proyecto.

Actualiza README.md:
Agrega una sección breve:

## Project CRUD API

Incluye:
- endpoints disponibles
- cómo ejecutar pruebas de integración de proyectos
- ruta Swagger

Actualiza AI_PROCESS.md:
1. Agrega este prompt completo como el siguiente prompt cronológico.
2. Documenta que se implementó el CRUD de proyectos.
3. Documenta que se mantuvo separación por capas.
4. Documenta que no se agregó lógica de base de datos en routes.

Ejecuta pruebas:

cd backend
pytest tests/integration/test_project_endpoints.py

Si hay pruebas unitarias existentes del servicio EVM, también ejecuta:

pytest

Al finalizar, reporta:
1. Rama usada.
2. Archivos creados.
3. Archivos modificados.
4. Resumen técnico.
5. Endpoints implementados.
6. Pruebas ejecutadas.
7. Resultado de pruebas.
8. Documentación actualizada.
9. AI_PROCESS actualizado.
10. Pendientes.
11. Commit sugerido.
12. Pull Request sugerido.

Commit sugerido:
Create project CRUD endpoints

Pull Request sugerido:
Create project CRUD endpoints
```

### Prompt 4

```text
Usa la skill EVORA MVP Builder.

Estamos en el proyecto EVORA, repositorio evora-evm-dashboard.

Objetivo de esta tarea:
Implementar el CRUD backend para actividades asociadas a proyectos usando FastAPI, SQLAlchemy, Pydantic, arquitectura por capas y el servicio EvmCalculationService ya existente.

Rama esperada:
feature/backend-activity-crud

Antes de modificar archivos:
1. Ejecuta git status.
2. Ejecuta git branch.
3. Confirma que estás en feature/backend-activity-crud.
4. Si no estás en esa rama, indícalo y sugiere el comando correcto.
5. No trabajes directamente sobre main ni develop.

Contexto funcional:
El desafío técnico solicita que cada actividad registre:
- Nombre
- BAC, Budget at Completion
- Porcentaje de avance planificado a la fecha de corte
- Porcentaje de avance real completado
- AC, Actual Cost

Con estos datos, el sistema debe calcular:
- PV
- EV
- CV
- SV
- CPI
- SPI
- EAC
- VAC

En esta tarea solo debes implementar CRUD de actividades y asegurar que las respuestas incluyan indicadores EVM por actividad. No implementes frontend ni resumen consolidado del proyecto en esta tarea, salvo que ya exista una función reusable.

Endpoints requeridos:

POST /api/v1/projects/{project_id}/activities
GET /api/v1/projects/{project_id}/activities
GET /api/v1/activities/{activity_id}
PUT /api/v1/activities/{activity_id}
DELETE /api/v1/activities/{activity_id}

Arquitectura obligatoria:
- Las rutas deben vivir en backend/app/routes/activity_routes.py.
- Los schemas deben vivir en backend/app/schemas/activity_schema.py.
- El modelo SQLAlchemy debe vivir en backend/app/models/activity.py.
- La lógica de acceso a datos debe vivir en backend/app/repositories/activity_repository.py.
- Los cálculos EVM deben usar EvmCalculationService.
- No pongas lógica de base de datos directamente en routes.
- No pongas fórmulas EVM dentro de routes.
- No pongas lógica EVM en schemas ni modelos.
- Mantén nombres técnicos en inglés.
- Mantén documentación y mensajes explicativos en español cuando aplique.

Modelo Activity:
Debe tener como mínimo:

- id: UUID, primary key
- project_id: UUID, foreign key hacia projects.id
- name: string, obligatorio, máximo 150 caracteres
- bac: numeric/float/decimal, obligatorio, mayor que 0
- planned_progress: numeric/float/decimal, obligatorio, entre 0 y 100
- actual_progress: numeric/float/decimal, obligatorio, entre 0 y 100
- actual_cost: numeric/float/decimal, obligatorio, mayor o igual que 0
- created_at: datetime
- updated_at: datetime

Relación:
- Una actividad pertenece a un proyecto.
- Un proyecto puede tener muchas actividades.
- Si se elimina un proyecto, sus actividades deben eliminarse por cascade si la base de datos/modelo lo permite.

Reglas de validación:
1. El nombre de la actividad es obligatorio.
2. El nombre no debe estar vacío.
3. BAC debe ser mayor que 0.
4. planned_progress debe estar entre 0 y 100.
5. actual_progress debe estar entre 0 y 100.
6. actual_cost debe ser mayor o igual que 0.
7. Si el proyecto no existe al crear una actividad, retornar HTTP 404.
8. Si la actividad no existe, retornar HTTP 404.
9. Si el request es inválido, retornar HTTP 422.
10. DELETE debe retornar HTTP 204 si elimina correctamente.

Schemas Pydantic requeridos:
Crear o ajustar en backend/app/schemas/activity_schema.py:

1. ActivityBase
2. ActivityCreate
3. ActivityUpdate
4. ActivityResponse
5. ActivityWithEvmResponse

ActivityCreate:
- name requerido
- bac requerido
- planned_progress requerido
- actual_progress requerido
- actual_cost requerido

ActivityUpdate:
- name opcional
- bac opcional
- planned_progress opcional
- actual_progress opcional
- actual_cost opcional

ActivityResponse:
- id
- project_id
- name
- bac
- planned_progress
- actual_progress
- actual_cost
- created_at
- updated_at

ActivityWithEvmResponse:
Debe incluir los campos de ActivityResponse y un objeto evm con:
- pv
- ev
- cv
- sv
- cpi
- spi
- eac
- vac
- cost_status
- schedule_status

Repository:
Crear o ajustar en backend/app/repositories/activity_repository.py métodos claros:

1. create_activity
2. get_activities_by_project
3. get_activity_by_id
4. update_activity
5. delete_activity

Routes:
Crear o ajustar en backend/app/routes/activity_routes.py:

1. POST /api/v1/projects/{project_id}/activities
2. GET /api/v1/projects/{project_id}/activities
3. GET /api/v1/activities/{activity_id}
4. PUT /api/v1/activities/{activity_id}
5. DELETE /api/v1/activities/{activity_id}

Cada endpoint debe incluir:
1. response_model.
2. status_code cuando aplique.
3. descripción clara para Swagger.
4. manejo de 404 cuando el proyecto o actividad no exista.
5. uso de Depends para obtener sesión de base de datos.
6. uso de EvmCalculationService para anexar indicadores EVM a las respuestas.

Main:
Asegura que backend/app/main.py incluya el router de actividades.

Swagger:
Debe seguir disponible en:
- /swagger-ui

OpenAPI:
Debe seguir disponible en:
- /api-docs.json

Pruebas de integración:
Crear o ajustar:
backend/tests/integration/test_activity_endpoints.py

Debe incluir pruebas para:

1. create activity successfully.
2. return 404 when creating activity for non-existing project.
3. list activities by project successfully.
4. get activity by id successfully.
5. return 404 when activity does not exist.
6. update activity successfully.
7. delete activity successfully.
8. validate activity name is required.
9. validate BAC must be greater than zero.
10. validate planned_progress cannot be lower than 0.
11. validate planned_progress cannot be greater than 100.
12. validate actual_progress cannot be lower than 0.
13. validate actual_progress cannot be greater than 100.
14. validate actual_cost cannot be negative.
15. verify activity response includes EVM indicators.
16. verify CPI is None when actual_cost is zero.
17. verify SPI is None when planned_progress is zero.

Las pruebas deben validar:
- status code.
- estructura del response.
- campos principales.
- indicadores EVM.
- comportamiento 404.
- comportamiento 422.

No crees pruebas vacías.
No crees pruebas que solo validen que algo retorna algo.
Las pruebas deben validar contrato real de API y cálculos reales.

Si el proyecto usa SQLite en memoria para tests, reutiliza esa configuración sin afectar PostgreSQL como base objetivo.

No agregues:
- AWS
- EC2
- Docker Compose nuevo
- autenticación
- roles
- frontend
- resumen consolidado si no es necesario para esta tarea

Actualiza README.md:
Agrega una sección breve:

## Activity CRUD API

Incluye:
- endpoints disponibles
- datos requeridos para crear actividades
- cómo ejecutar pruebas de integración de actividades
- ruta Swagger

Actualiza AI_PROCESS.md:
1. Agrega este prompt completo como el siguiente prompt cronológico.
2. Documenta que se implementó el CRUD de actividades.
3. Documenta que las respuestas de actividades incluyen indicadores EVM.
4. Documenta que se mantuvo separación por capas.
5. Documenta que la lógica EVM se reutilizó desde EvmCalculationService y no se duplicó en routes.

Ejecuta pruebas:

cd backend
pytest tests/integration/test_activity_endpoints.py

También ejecuta:

pytest

Al finalizar, reporta:
1. Rama usada.
2. Archivos creados.
3. Archivos modificados.
4. Resumen técnico.
5. Endpoints implementados.
6. Pruebas ejecutadas.
7. Resultado de pruebas.
8. Documentación actualizada.
9. AI_PROCESS actualizado.
10. Pendientes.
11. Commit sugerido.
12. Pull Request sugerido.

Commit sugerido:
Create activity CRUD endpoints

Pull Request sugerido:
Create activity CRUD endpoints
```

## How I learned EVM

- Se implementaron las fórmulas base de Valor Ganado en `EvmCalculationService` para actividad y consolidado.
- Se reforzó la diferencia entre métricas por actividad y métricas consolidadas calculadas sobre totales del proyecto.
- Se implementó el CRUD de proyectos en API REST con prefijo versionado `/api/v1/projects`.
- Se implementó el CRUD de actividades en API REST y cada respuesta incluye indicadores EVM por actividad.

## How I validated formulas

- Se diseñaron pruebas unitarias con valores controlados para PV, EV, CV, SV, CPI, SPI, EAC y VAC.
- Se incluyeron casos borde para división por cero, progreso real en cero, BAC en cero y proyecto sin actividades.
- Se agregaron pruebas de integración para crear, listar, consultar, actualizar y eliminar proyectos, incluyendo validaciones 404 y 422.
- Se agregaron pruebas de integración del CRUD de actividades para validar contrato, reglas 422 y cálculo EVM en respuesta.

## AI suggestions I did not follow

- No se agregaron endpoints ni cambios de frontend en esta tarea para respetar el alcance solicitado.
- No se introdujo infraestructura adicional (AWS/EC2/Docker Compose nuevo) para mantener el foco en lógica EVM y pruebas.

## Independent architecture decision

- En el consolidado de proyecto no se promedian CPI ni SPI por actividad; se calcula sobre sumatorias de BAC, PV, EV y AC.
- Cuando CPI o SPI no son calculables, se retorna `None` para el indicador correspondiente y estado textual `"No calculable"`.
- Se mantuvo la separación por capas (routes/schemas/repositories/models) y no se agregó lógica de base de datos dentro de routes.
- La lógica EVM en actividades se reutilizó desde `EvmCalculationService` y no se duplicaron fórmulas en routes.

## Final reflection

- La implementación del servicio EVM con pruebas unitarias exhaustivas reduce riesgo funcional y facilita evolución incremental del backend.
