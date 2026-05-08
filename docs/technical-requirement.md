# EVORA - Technical Requirement

## 1. Introduccion

EVORA es una aplicacion fullstack para gestion de proyectos y actividades con calculo automatico de indicadores de Valor Ganado (EVM).

## 2. Objetivo general

Construir un MVP local que permita registrar proyectos y actividades, calcular indicadores EVM por actividad y consolidarlos por proyecto para apoyar seguimiento tecnico y financiero.

## 3. Alcance

- CRUD de proyectos.
- CRUD de actividades asociadas a proyectos.
- Calculo EVM por actividad.
- Consolidacion EVM por proyecto.
- Dashboard web para visualizacion de datos e indicadores.

## 4. Requerimientos funcionales

- Crear, listar, consultar, editar y eliminar proyectos.
- Crear, listar, consultar, editar y eliminar actividades por proyecto.
- Registrar por actividad: nombre, BAC, progreso planificado, progreso real, AC.
- Exponer API REST documentada en Swagger.
- Visualizar tabla de actividades, tarjetas de resumen e indicador grafico PV/EV/AC.

## 5. Requerimientos no funcionales

- Arquitectura en capas con separacion de responsabilidades.
- Tipado y validacion de datos con Pydantic.
- Persistencia en PostgreSQL.
- Pruebas unitarias y de integracion iniciales.
- Lint de backend con Ruff.
- Configuracion local sin dependencias cloud.

## 6. Reglas de negocio EVM

Para cada actividad:

- PV = (porcentaje planificado / 100) * BAC
- EV = (porcentaje completado / 100) * BAC
- CV = EV - AC
- SV = EV - PV
- CPI = EV / AC, si AC > 0
- SPI = EV / PV, si PV > 0
- EAC = BAC / CPI, si CPI es calculable y distinto de cero
- VAC = BAC - EAC, si EAC es calculable

Interpretaciones:

- CPI > 1: eficiencia en costos
- CPI = 1: en presupuesto
- CPI < 1: sobre presupuesto
- CPI no calculable cuando AC = 0
- SPI > 1: adelantado
- SPI = 1: en cronograma
- SPI < 1: atrasado
- SPI no calculable cuando PV = 0

## 7. Casos borde

- Actividad con AC = 0: CPI y EAC/VAC no calculables.
- Actividad con PV = 0: SPI no calculable.
- Proyecto sin actividades: consolidado en cero y ratios no calculables.
- Progreso real = 0: EV en cero.
- Valores fuera de rango para porcentajes deben ser rechazados.

## 8. Criterios de aceptacion

- API funcional localmente con endpoints documentados.
- Endpoints base de proyectos y actividades responden correctamente.
- Servicio EVM calcula formulas y maneja divisiones por cero.
- Frontend muestra informacion mock con componentes solicitados.
- Pruebas unitarias EVM y pruebas de integracion base creadas.

## 9. Entregables

- Estructura completa del repositorio `evora-evm-dashboard`.
- Backend base FastAPI con pruebas.
- Frontend base React + Vite + Tailwind.
- Script SQL inicial `database/init.sql`.
- Documentacion: `README.md`, `AI_PROCESS.md`, `docs/technical-requirement.md`, `docs/architecture.md`.
