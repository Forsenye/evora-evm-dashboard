# AI Process Log

## 1. Herramientas de IA utilizadas

- Codex (GPT-5) como asistente de arquitectura, desarrollo full stack y DevOps local.

## 2. Prompts usados en orden cronologico

### Prompt 1

```text
Actúa como un arquitecto de software senior, full stack developer y DevOps engineer local.

Estoy trabajando en una prueba técnica para el cargo de Ingeniero de Desarrollo. Ya tengo creado el repositorio Git vacío. Necesito que generes la base completa del proyecto, la estructura de carpetas, archivos iniciales y configuración mínima para comenzar el desarrollo.

Nombre oficial del MVP:
EVORA

Nombre descriptivo:
EVORA | Plataforma inteligente para seguimiento de proyectos con Valor Ganado

Nombre técnico del repositorio:
evora-evm-dashboard

IMPORTANTE:
No generes configuración de despliegue en nube.
No generes documentación AWS.
No generes configuración EC2.
No agregues Kubernetes.
No agregues Terraform.
No agregues CI/CD todavía.
En esta fase solo necesito la base local del repositorio solicitada por la prueba técnica.

Contexto funcional:
Se debe construir una aplicación fullstack que permita gestionar proyectos y actividades, y calcular automáticamente indicadores de Valor Ganado, Earned Value Management, EVM.

La aplicación debe permitir:
1. Crear, listar, consultar, editar y eliminar proyectos.
2. Crear, listar, consultar, editar y eliminar actividades asociadas a proyectos.
3. Registrar por actividad:
   - Nombre
   - BAC, Budget at Completion
   - Porcentaje de avance planificado
   - Porcentaje de avance real completado
   - AC, Actual Cost
4. Calcular por actividad y consolidado por proyecto:
   - PV = porcentaje planificado * BAC
   - EV = porcentaje completado * BAC
   - CV = EV - AC
   - SV = EV - PV
   - CPI = EV / AC
   - SPI = EV / PV
   - EAC = BAC / CPI
   - VAC = BAC - EAC
5. Retornar interpretación de CPI:
   - CPI > 1: eficiencia en costos
   - CPI = 1: en presupuesto
   - CPI < 1: sobre presupuesto
   - CPI no calculable cuando AC = 0
6. Retornar interpretación de SPI:
   - SPI > 1: adelantado
   - SPI = 1: en cronograma
   - SPI < 1: atrasado
   - SPI no calculable cuando PV = 0
7. Mostrar en frontend:
   - Formulario de proyecto
   - Formulario de actividades
   - Tabla de actividades con indicadores calculados
   - Tarjetas de indicadores consolidados
   - Indicadores visuales para CPI y SPI
   - Gráfica comparativa PV, EV y AC por actividad

Stack técnico requerido:
Backend:
- Python 3.11
- FastAPI
- Pydantic
- SQLAlchemy
- PostgreSQL
- Pytest
- Ruff como linter

Frontend:
- React
- Vite
- TypeScript
- Tailwind CSS
- Axios
- Recharts

Base de datos:
- PostgreSQL
- Script inicial en database/init.sql

Documentación:
- README.md
- AI_PROCESS.md
- docs/technical-requirement.md
- docs/architecture.md

API:
- OpenAPI/Swagger disponible localmente.
- Configurar FastAPI para que Swagger esté disponible en /swagger-ui y OpenAPI en /api-docs.json.
- Cada endpoint debe tener descripción básica, request schema y response schema.

Gitflow:
El repositorio debe manejar:
- main
- develop
- feature/project-setup
- feature/backend-foundation
- feature/frontend-foundation
- feature/documentation
- release/v1.0.0

Como el repositorio ya existe, valida primero el estado actual de Git.
Si no existe rama develop, créala desde main.
Crea la rama feature/project-setup para esta primera base.
No hagas merge final a main todavía.

Mensajes de commit:
Usa commits descriptivos en imperativo.
Ejemplos:
- Add initial project structure
- Add backend FastAPI foundation
- Add frontend Vite foundation
- Add technical documentation templates
- Add database initialization script

No uses mensajes como:
- fix
- cambios
- wip
- ajustes

Estructura esperada del repositorio:

evora-evm-dashboard/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   ├── config.py
│   │   │   └── database.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── project.py
│   │   │   └── activity.py
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   ├── project_schema.py
│   │   │   ├── activity_schema.py
│   │   │   └── evm_schema.py
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── project_routes.py
│   │   │   └── activity_routes.py
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   └── evm_calculation_service.py
│   │   └── repositories/
│   │       ├── __init__.py
│   │       ├── project_repository.py
│   │       └── activity_repository.py
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── unit/
│   │   │   ├── __init__.py
│   │   │   └── test_evm_calculation_service.py
│   │   └── integration/
│   │       ├── __init__.py
│   │       ├── test_project_endpoints.py
│   │       └── test_activity_endpoints.py
│   ├── requirements.txt
│   ├── pytest.ini
│   ├── pyproject.toml
│   └── .env.example
│
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   │   └── evoraApi.ts
│   │   ├── components/
│   │   │   ├── ProjectForm.tsx
│   │   │   ├── ActivityForm.tsx
│   │   │   ├── ActivityTable.tsx
│   │   │   ├── IndicatorCard.tsx
│   │   │   ├── StatusBadge.tsx
│   │   │   └── EvmChart.tsx
│   │   ├── pages/
│   │   │   └── Dashboard.tsx
│   │   ├── types/
│   │   │   └── evm.ts
│   │   ├── App.tsx
│   │   ├── main.tsx
│   │   └── index.css
│   ├── package.json
│   ├── vite.config.ts
│   ├── tsconfig.json
│   ├── tailwind.config.js
│   ├── postcss.config.js
│   └── .env.example
│
├── database/
│   └── init.sql
│
├── docs/
│   ├── technical-requirement.md
│   └── architecture.md
│
├── README.md
├── AI_PROCESS.md
├── .gitignore
└── .env.example

Backend base:
1. Crea FastAPI en backend/app/main.py.
2. Configura título del API como "EVORA API".
3. Configura descripción: "API REST para gestión de proyectos, actividades e indicadores EVM".
4. Configura docs_url="/swagger-ui".
5. Configura openapi_url="/api-docs.json".
6. Crea endpoint GET /health con response:
   {
     "status": "ok",
     "service": "EVORA API"
   }
7. Crea routers base para projects y activities.
8. Crea modelos SQLAlchemy para Project y Activity.
9. Crea schemas Pydantic para request y response.
10. Crea EvmCalculationService con métodos vacíos o implementación inicial mínima:
   - calculate_activity_indicators
   - calculate_project_summary
   - interpret_cpi
   - interpret_spi
11. Incluye control base para divisiones por cero:
   - Si AC = 0, CPI debe ser None.
   - Si PV = 0, SPI debe ser None.
12. No pongas lógica de negocio en routes.
13. Deja comentarios mínimos solo cuando aporten contexto técnico.

Frontend base:
1. Crea proyecto React con Vite y TypeScript.
2. Configura Tailwind CSS.
3. Crea página Dashboard.
4. Crea componentes base:
   - ProjectForm
   - ActivityForm
   - ActivityTable
   - IndicatorCard
   - StatusBadge
   - EvmChart
5. Usa datos mock iniciales para renderizar el dashboard.
6. La gráfica debe usar Recharts.
7. No implementes diseño complejo.
8. El objetivo visual es que se entienda claramente:
   - Proyecto
   - Actividades
   - Indicadores
   - Estado CPI
   - Estado SPI
   - Comparación PV, EV y AC

Base de datos:
Crea database/init.sql con:
1. Extensión para UUID si aplica.
2. Tabla projects.
3. Tabla activities.
4. Relación project_id con ON DELETE CASCADE.
5. Restricciones:
   - bac > 0
   - planned_progress entre 0 y 100
   - actual_progress entre 0 y 100
   - actual_cost >= 0

README.md:
Crea un README inicial con:
1. Nombre del proyecto.
2. Descripción.
3. Stack tecnológico.
4. Estructura del repositorio.
5. Requisitos previos.
6. Instalación backend.
7. Instalación frontend.
8. Ejecución backend.
9. Ejecución frontend.
10. Pruebas backend.
11. Acceso a Swagger.
12. Script de base de datos.
13. Flujo Gitflow.
14. Estado actual del MVP.

AI_PROCESS.md:
Crea una plantilla inicial realista con secciones:
1. Herramientas de IA utilizadas.
2. Prompts usados en orden cronológico.
3. Cómo aprendí EVM.
4. Cómo validé las fórmulas.
5. Decisiones donde no seguí a la IA.
6. Decisión de arquitectura independiente.
7. Reflexión final.
8. Registro cronológico del trabajo.

En AI_PROCESS.md deja explícito este primer prompt como Prompt 1, sin resumirlo.
No inventes prompts futuros.

docs/technical-requirement.md:
Crea el documento técnico con:
1. Introducción.
2. Objetivo general.
3. Alcance.
4. Requerimientos funcionales.
5. Requerimientos no funcionales.
6. Reglas de negocio EVM.
7. Casos borde.
8. Criterios de aceptación.
9. Entregables.

docs/architecture.md:
Crea arquitectura textual con:
1. Descripción de capas.
2. Diagrama textual:
   React Dashboard
      -> FastAPI REST API
      -> Services
      -> EvmCalculationService
      -> SQLAlchemy
      -> PostgreSQL
3. Justificación de separación de responsabilidades.
4. Explicación de por qué la lógica EVM no debe estar en controladores.

Pruebas:
1. Crea pruebas unitarias iniciales para EvmCalculationService.
2. Incluye como mínimo:
   - cálculo PV
   - cálculo EV
   - cálculo CV
   - cálculo SV
   - CPI cuando AC > 0
   - CPI None cuando AC = 0
   - SPI cuando PV > 0
   - SPI None cuando PV = 0
   - proyecto sin actividades
   - avance real igual a cero
3. Crea pruebas de integración iniciales para:
   - GET /health
   - GET /projects
   - GET /projects/{project_id}
   - GET /projects/{project_id}/activities
4. Si aún no implementas persistencia completa, deja las pruebas preparadas y marcadas de forma limpia para completarlas, pero evita tests falsos que solo validen que algo retorna algo.

Archivos de configuración:
1. Crea .gitignore para Python, Node, entornos virtuales, variables de entorno, coverage y builds.
2. Crea backend/requirements.txt con dependencias necesarias.
3. Crea backend/pytest.ini.
4. Crea backend/pyproject.toml con configuración Ruff.
5. Crea frontend/package.json con scripts:
   - dev
   - build
   - preview
   - lint

No incluyas:
- AWS
- EC2
- Terraform
- Kubernetes
- GitHub Actions
- despliegue cloud
- autenticación
- roles
- notificaciones
- exportación PDF o Excel

Al finalizar:
1. Muestra el árbol de archivos generado.
2. Indica los comandos para ejecutar backend.
3. Indica los comandos para ejecutar frontend.
4. Indica los comandos para correr pruebas.
5. Indica los comandos Git ejecutados o sugeridos.
6. Realiza commit con mensaje:
   Add initial EVORA project foundation

Antes de modificar archivos, revisa el estado actual del repositorio con:
git status
git branch
```

## 3. Como aprendi EVM

- Identifique formulas base de EVM solicitadas para traducirlas a funciones deterministicas.
- Defini escenarios de division por cero para CPI y SPI.
- Organice interpretaciones textuales como parte del servicio de dominio.

## 4. Como valide las formulas

- Se construyeron pruebas unitarias con valores controlados para PV, EV, CV, SV, CPI y SPI.
- Se validaron casos de borde: AC = 0, PV = 0, proyecto sin actividades y avance real = 0.

## 5. Decisiones donde no segui a la IA

- No se agrego despliegue cloud ni CI/CD por restriccion explicita de alcance.
- Se mantuvo arquitectura base local sin autenticacion para respetar fase MVP.

## 6. Decision de arquitectura independiente

- Se aislo EVM en `EvmCalculationService` para mantener controladores HTTP livianos y logica reutilizable.

## 7. Reflexion final

- La IA acelero la construccion inicial del esqueleto fullstack.
- El criterio ingenieril se aplico para mantener foco en alcance, mantenibilidad y trazabilidad tecnica.

## 8. Registro cronologico del trabajo

- Paso 1: Validacion inicial de estado Git y ramas.
- Paso 2: Creacion de estructura backend, frontend, database y docs.
- Paso 3: Implementacion de API base, modelos, schemas, repositorios y servicio EVM.
- Paso 4: Implementacion de dashboard base con datos mock y grafica comparativa.
- Paso 5: Creacion de pruebas unitarias e integracion iniciales.
- Paso 6: Documentacion tecnica y cierre con commit.
