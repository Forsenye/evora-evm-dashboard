# EVORA

EVORA | Plataforma inteligente para seguimiento de proyectos con Valor Ganado.

## Stack tecnologico

- Backend: Python 3.11, FastAPI, Pydantic, SQLAlchemy, PostgreSQL, Pytest, Ruff
- Frontend: React, Vite, TypeScript, Tailwind CSS, Axios, Recharts
- Base de datos: PostgreSQL

## Estructura del repositorio

```text
evora-evm-dashboard/
|-- backend/
|   |-- app/
|   |   |-- core/
|   |   |-- models/
|   |   |-- repositories/
|   |   |-- routes/
|   |   |-- schemas/
|   |   `-- services/
|   |-- tests/
|   |   |-- unit/
|   |   `-- integration/
|   |-- .env.example
|   |-- pyproject.toml
|   |-- pytest.ini
|   `-- requirements.txt
|-- frontend/
|   |-- src/
|   |   |-- api/
|   |   |-- components/
|   |   |-- pages/
|   |   `-- types/
|   |-- .env.example
|   |-- package.json
|   |-- postcss.config.js
|   |-- tailwind.config.js
|   |-- tsconfig.json
|   `-- vite.config.ts
|-- database/
|   `-- init.sql
|-- docs/
|   |-- architecture.md
|   `-- technical-requirement.md
|-- .env.example
|-- .gitignore
|-- AI_PROCESS.md
`-- README.md
```

## Requisitos previos

- Python 3.11+
- Node.js 20+
- npm 10+
- PostgreSQL 14+

## Instalacion backend

```bash
cd backend
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Instalacion frontend

```bash
cd frontend
npm install
```

## Ejecucion backend

```bash
cd backend
.\.venv\Scripts\Activate.ps1
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Ejecucion frontend

```bash
cd frontend
npm run dev
```

## Pruebas backend

```bash
cd backend
.\.venv\Scripts\Activate.ps1
pytest
```

## Project CRUD API

Endpoints disponibles:

- `POST /api/v1/projects`
- `GET /api/v1/projects`
- `GET /api/v1/projects/{project_id}`
- `PUT /api/v1/projects/{project_id}`
- `DELETE /api/v1/projects/{project_id}`

Pruebas de integración de proyectos:

```bash
cd backend
pytest tests/integration/test_project_endpoints.py
```

Swagger:

- `http://localhost:8000/swagger-ui`

## EVM Calculation Service

- Ubicacion del servicio: `backend/app/services/evm_calculation_service.py`
- Indicadores calculados: PV, EV, CV, SV, CPI, SPI, EAC y VAC por actividad y consolidados por proyecto.
- Ejecucion de pruebas unitarias:

```bash
cd backend
pytest tests/unit/test_evm_calculation_service.py
pytest --cov=app tests/unit/test_evm_calculation_service.py
```

## Acceso a Swagger

- Swagger UI: `http://localhost:8000/swagger-ui`
- OpenAPI JSON: `http://localhost:8000/api-docs.json`

## Script de base de datos

```bash
psql -U postgres -d evora -f database/init.sql
```

## Flujo Gitflow

Ramas contempladas en esta fase:

- `main`
- `develop`
- `feature/project-setup`
- `feature/backend-foundation`
- `feature/frontend-foundation`
- `feature/documentation`
- `release/v1.0.0`

## Estado actual del MVP

- Base local del repositorio creada.
- Backend FastAPI inicial con routers de proyectos y actividades.
- Servicio EVM inicial con formulas base e interpretaciones CPI/SPI.
- Frontend dashboard con datos mock y grafica PV/EV/AC.
- Script inicial SQL y documentacion tecnica de arranque.
- Sin configuracion de despliegue cloud en esta fase.
