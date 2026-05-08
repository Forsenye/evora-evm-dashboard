# EVORA - Architecture

## 1. Descripcion de capas

- Presentacion: React Dashboard para formularios, tabla, tarjetas e indicadores visuales.
- API: FastAPI expone endpoints REST de proyectos y actividades.
- Aplicacion: Services centralizan reglas de negocio y calculo EVM.
- Persistencia: Repositories encapsulan acceso a datos con SQLAlchemy.
- Datos: PostgreSQL almacena proyectos y actividades.

## 2. Diagrama textual

```text
React Dashboard
   -> FastAPI REST API
   -> Services
   -> EvmCalculationService
   -> SQLAlchemy
   -> PostgreSQL
```

## 3. Justificacion de separacion de responsabilidades

- Las rutas HTTP se enfocan en validacion de entrada/salida y codigos de estado.
- Los repositorios concentran operaciones CRUD y consultas.
- El servicio EVM encapsula formulas e interpretaciones para evitar duplicacion.
- Esta separacion mejora mantenibilidad, pruebas y evolucion del dominio.

## 4. Por que la logica EVM no debe estar en controladores

- Los controladores cambian por temas de transporte HTTP, no por reglas del negocio.
- Si EVM vive en controladores, la logica queda acoplada a FastAPI y se dificulta reutilizarla.
- Ubicar EVM en servicios permite pruebas unitarias directas sin levantar API.
- Centralizar calculos evita inconsistencias entre endpoints y facilita trazabilidad tecnica.
