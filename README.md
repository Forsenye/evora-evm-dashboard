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

Nota:

- El backend habilita CORS para consumo local desde Vite en `http://localhost:5173`, `http://localhost:5174`, `http://127.0.0.1:5173` y `http://127.0.0.1:5174`.

## Ejecucion frontend

```bash
cd frontend
npm run dev
```

## Frontend Dashboard

- Ubicacion: `frontend/`
- Variable de entorno:

```bash
VITE_API_BASE_URL=http://localhost:8000
```

- Comandos:

```bash
cd frontend
npm install
npm run dev
npm run build
npm run lint
```

- Componentes principales:
  - `ProjectForm`
  - `ActivityForm`
  - `IndicatorCard`
  - `StatusBadge`
  - `ActivityTable`
  - `EvmChart`
  - `Dashboard`

- Endpoints consumidos:
  - `GET /api/v1/projects`
  - `POST /api/v1/projects`
  - `GET /api/v1/projects/{project_id}`
  - `POST /api/v1/projects/{project_id}/activities`
  - `GET /api/v1/projects/{project_id}/activities`
  - `GET /api/v1/projects/{project_id}/evm-summary`

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

## Activity CRUD API

Endpoints disponibles:

- `POST /api/v1/projects/{project_id}/activities`
- `GET /api/v1/projects/{project_id}/activities`
- `GET /api/v1/activities/{activity_id}`
- `PUT /api/v1/activities/{activity_id}`
- `DELETE /api/v1/activities/{activity_id}`

Datos requeridos para crear actividades:

- `name` (string, requerido, maximo 150)
- `bac` (numero, requerido, mayor que 0)
- `planned_progress` (numero, requerido, entre 0 y 100)
- `actual_progress` (numero, requerido, entre 0 y 100)
- `actual_cost` (numero, requerido, mayor o igual que 0)

Pruebas de integración de actividades:

```bash
cd backend
pytest tests/integration/test_activity_endpoints.py
```

Swagger:

- `http://localhost:8000/swagger-ui`

## Project EVM Summary API

Endpoint disponible:

- `GET /api/v1/projects/{project_id}/evm-summary`

Propósito:

- Entregar resumen EVM consolidado del proyecto y detalle EVM por actividad para consumo del dashboard.

Ejemplo de respuesta resumido:

```json
{
  "project_id": "uuid",
  "project_name": "Implementacion EVORA",
  "total_activities": 3,
  "summary": {
    "bac": 3000000.0,
    "pv": 1500000.0,
    "ev": 1200000.0,
    "ac": 1700000.0,
    "cv": -500000.0,
    "sv": -300000.0,
    "cpi": 0.71,
    "spi": 0.8,
    "eac": 4250000.0,
    "vac": -1250000.0,
    "cost_status": "Sobre presupuesto",
    "schedule_status": "Atrasado"
  },
  "activities": []
}
```

Prueba de integración:

```bash
cd backend
pytest tests/integration/test_project_evm_summary_endpoint.py
```

## EVM Calculation Service

- Ubicacion del servicio: `backend/app/services/evm_calculation_service.py`
- Indicadores calculados: PV, EV, CV, SV, CPI, SPI, EAC y VAC por actividad y consolidados por proyecto.
- Ejecucion de pruebas unitarias:

```bash
cd backend
pytest tests/unit/test_evm_calculation_service.py
pytest --cov=app tests/unit/test_evm_calculation_service.py
```

## Validacion end-to-end local

### Comandos backend

```bash
cd backend
.\.venv\Scripts\python -m pytest
.\.venv\Scripts\python -m pytest --cov=app
uvicorn app.main:app --reload
```

### Comandos frontend

```bash
cd frontend
npm install
npm run build
npm run lint
```

### Datos de prueba demo

Proyecto:

- `Implementacion EVORA`

Actividades:

- `Diseno de base de datos` | BAC `1000000` | planned `50` | actual `40` | AC `600000`
- `Desarrollo backend` | BAC `1000000` | planned `60` | actual `60` | AC `700000`
- `Desarrollo frontend` | BAC `1000000` | planned `40` | actual `20` | AC `400000`

Resultados esperados:

- BAC total: `3000000`
- PV total: `1500000`
- EV total: `1200000`
- AC total: `1700000`
- CV: `-500000`
- SV: `-300000`
- CPI aproximado: `0.71`
- SPI: `0.80`
- cost_status: `Sobre presupuesto`
- schedule_status: `Atrasado`

### Checklist de validacion

- [x] Backend tests: `64 passed`
- [x] Cobertura backend: `96%`
- [x] FastAPI levantado localmente y validado en `/health`
- [x] Swagger accesible en `/swagger-ui`
- [x] OpenAPI accesible en `/api-docs.json`
- [x] Endpoints de proyectos validados
- [x] Endpoints de actividades validados
- [x] Endpoint consolidado EVM validado
- [x] Caso borde AC=0 retorna CPI `null`
- [x] Caso borde planned_progress=0 retorna SPI `null`
- [x] BAC=0 retorna HTTP `422`
- [x] Porcentajes fuera de rango retornan HTTP `422`
- [x] Proyecto sin actividades retorna resumen controlado
- [x] Frontend build exitoso
- [x] Frontend lint exitoso

Nota:

- El dashboard se valida manualmente iniciando backend y frontend y cargando el proyecto demo para comprobar tabla, tarjetas, badges CPI/SPI y grafica PV/EV/AC.

## Consideraciones de ejecución en entornos corporativos

EVORA está preparado para ejecutarse localmente con backend FastAPI y frontend React/Vite.

En equipos corporativos pueden existir restricciones sobre Shell, ejecución de scripts, instalación de dependencias, uso de puertos locales, acceso del navegador a localhost o comunicación entre frontend y backend por CORS.

Si el entorno bloquea estas acciones, se recomienda ejecutar el MVP en un equipo personal, entorno de laboratorio o ambiente autorizado donde estén permitidos Python, Node.js, npm y navegación local.

No se recomienda modificar políticas de seguridad, firewall, navegador o restricciones corporativas sin autorización.

Validaciones alternativas recomendadas cuando hay restricciones:

- Backend: `cd backend && .\.venv\Scripts\python.exe -m pytest`
- Frontend (build): `cd frontend && npm run build`
- Validación funcional completa desde navegador solo en un entorno autorizado que permita localhost y puertos locales.

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
