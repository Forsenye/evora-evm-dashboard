import uuid

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.activity import Activity
from app.repositories.activity_repository import ActivityRepository
from app.repositories.project_repository import ProjectRepository
from app.schemas.evm_schema import (
    ActivityWithEvmResponse,
    EvmInput,
    ProjectEvmDashboardSummary,
    ProjectEvmSummaryResponse,
)
from app.schemas.project_schema import ProjectCreate, ProjectResponse, ProjectUpdate
from app.services.evm_calculation_service import EvmCalculationService

router = APIRouter(prefix="/api/v1/projects", tags=["projects"])


def _round_number(value: float | None) -> float | None:
    if value is None:
        return None
    return round(value, 2)


def _to_evm_input(activity: Activity) -> EvmInput:
    return EvmInput(
        bac=float(activity.bac),
        planned_progress=float(activity.planned_progress),
        actual_progress=float(activity.actual_progress),
        actual_cost=float(activity.actual_cost),
    )


def _build_activity_with_evm(activity: Activity) -> ActivityWithEvmResponse:
    indicators = EvmCalculationService.calculate_activity_indicators(_to_evm_input(activity))
    return ActivityWithEvmResponse(
        id=str(activity.id),
        name=activity.name,
        bac=float(activity.bac),
        planned_progress=float(activity.planned_progress),
        actual_progress=float(activity.actual_progress),
        actual_cost=float(activity.actual_cost),
        evm=ProjectEvmDashboardSummary(
            bac=_round_number(float(activity.bac)) or 0.0,
            pv=_round_number(indicators.pv) or 0.0,
            ev=_round_number(indicators.ev) or 0.0,
            ac=_round_number(float(activity.actual_cost)) or 0.0,
            cv=_round_number(indicators.cv) or 0.0,
            sv=_round_number(indicators.sv) or 0.0,
            cpi=_round_number(indicators.cpi),
            spi=_round_number(indicators.spi),
            eac=_round_number(indicators.eac),
            vac=_round_number(indicators.vac),
            cost_status=indicators.cpi_status,
            schedule_status=indicators.spi_status,
        ),
    )


@router.post(
    "",
    response_model=ProjectResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Crear proyecto",
    description="Crea un nuevo proyecto.",
)
def create_project(payload: ProjectCreate, db: Session = Depends(get_db)) -> ProjectResponse:
    repository = ProjectRepository(db)
    return repository.create_project(payload)


@router.get(
    "",
    response_model=list[ProjectResponse],
    summary="Listar proyectos",
    description="Obtiene la lista de proyectos registrados.",
)
def get_projects(db: Session = Depends(get_db)) -> list[ProjectResponse]:
    repository = ProjectRepository(db)
    return repository.get_projects()


@router.get(
    "/{project_id}",
    response_model=ProjectResponse,
    summary="Obtener proyecto",
    description="Obtiene un proyecto por su identificador.",
)
def get_project_by_id(project_id: uuid.UUID, db: Session = Depends(get_db)) -> ProjectResponse:
    repository = ProjectRepository(db)
    project = repository.get_project_by_id(project_id)
    if project is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    return project


@router.put(
    "/{project_id}",
    response_model=ProjectResponse,
    summary="Actualizar proyecto",
    description="Actualiza los datos de un proyecto.",
)
def update_project(
    project_id: uuid.UUID,
    payload: ProjectUpdate,
    db: Session = Depends(get_db),
) -> ProjectResponse:
    repository = ProjectRepository(db)
    project = repository.get_project_by_id(project_id)
    if project is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")

    return repository.update_project(project, payload)


@router.delete(
    "/{project_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar proyecto",
    description="Elimina un proyecto existente.",
)
def delete_project(project_id: uuid.UUID, db: Session = Depends(get_db)) -> Response:
    repository = ProjectRepository(db)
    project = repository.get_project_by_id(project_id)
    if project is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")

    repository.delete_project(project)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get(
    "/{project_id}/evm-summary",
    response_model=ProjectEvmSummaryResponse,
    summary="Resumen EVM consolidado de proyecto",
    description="Obtiene el resumen EVM consolidado y el detalle por actividad para un proyecto.",
)
def get_project_evm_summary(
    project_id: uuid.UUID,
    db: Session = Depends(get_db),
) -> ProjectEvmSummaryResponse:
    project_repository = ProjectRepository(db)
    project = project_repository.get_project_by_id(project_id)
    if project is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")

    activity_repository = ActivityRepository(db)
    activities = activity_repository.get_activities_by_project(project_id)
    activity_inputs = [_to_evm_input(activity) for activity in activities]
    project_summary = EvmCalculationService.calculate_project_summary(activity_inputs)

    response_activities = [_build_activity_with_evm(activity) for activity in activities]
    summary = ProjectEvmDashboardSummary(
        bac=_round_number(project_summary.total_bac) or 0.0,
        pv=_round_number(project_summary.total_pv) or 0.0,
        ev=_round_number(project_summary.total_ev) or 0.0,
        ac=_round_number(project_summary.total_ac) or 0.0,
        cv=_round_number(project_summary.total_cv) or 0.0,
        sv=_round_number(project_summary.total_sv) or 0.0,
        cpi=_round_number(project_summary.cpi),
        spi=_round_number(project_summary.spi),
        eac=_round_number(project_summary.total_eac),
        vac=_round_number(project_summary.total_vac),
        cost_status=project_summary.cpi_status,
        schedule_status=project_summary.spi_status,
    )

    summary_status = None
    if not activities:
        summary_status = "Sin actividades registradas"

    return ProjectEvmSummaryResponse(
        project_id=str(project.id),
        project_name=project.name,
        total_activities=len(activities),
        summary=summary,
        activities=response_activities,
        status=summary_status,
    )
