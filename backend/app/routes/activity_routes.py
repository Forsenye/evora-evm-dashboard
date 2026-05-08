import uuid

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.activity import Activity
from app.repositories.activity_repository import ActivityRepository
from app.repositories.project_repository import ProjectRepository
from app.schemas.activity_schema import (
    ActivityCreate,
    ActivityEvmData,
    ActivityUpdate,
    ActivityWithEvmResponse,
)
from app.schemas.evm_schema import EvmInput
from app.services.evm_calculation_service import EvmCalculationService

router = APIRouter(prefix="/api/v1", tags=["activities"])


def _build_activity_with_evm_response(activity: Activity) -> ActivityWithEvmResponse:
    indicators = EvmCalculationService.calculate_activity_indicators(
        EvmInput(
            bac=float(activity.bac),
            planned_progress=float(activity.planned_progress),
            actual_progress=float(activity.actual_progress),
            actual_cost=float(activity.actual_cost),
        )
    )

    return ActivityWithEvmResponse(
        id=activity.id,
        project_id=activity.project_id,
        name=activity.name,
        bac=float(activity.bac),
        planned_progress=float(activity.planned_progress),
        actual_progress=float(activity.actual_progress),
        actual_cost=float(activity.actual_cost),
        created_at=activity.created_at,
        updated_at=activity.updated_at,
        evm=ActivityEvmData(
            pv=indicators.pv,
            ev=indicators.ev,
            cv=indicators.cv,
            sv=indicators.sv,
            cpi=indicators.cpi,
            spi=indicators.spi,
            eac=indicators.eac,
            vac=indicators.vac,
            cost_status=indicators.cpi_status,
            schedule_status=indicators.spi_status,
        ),
    )


@router.post(
    "/projects/{project_id}/activities",
    response_model=ActivityWithEvmResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Crear actividad",
    description="Crea una nueva actividad asociada a un proyecto.",
)
def create_activity(
    project_id: uuid.UUID,
    payload: ActivityCreate,
    db: Session = Depends(get_db),
) -> ActivityWithEvmResponse:
    project_repository = ProjectRepository(db)
    if project_repository.get_project_by_id(project_id) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")

    activity_repository = ActivityRepository(db)
    activity = activity_repository.create_activity(project_id, payload)
    return _build_activity_with_evm_response(activity)


@router.get(
    "/projects/{project_id}/activities",
    response_model=list[ActivityWithEvmResponse],
    summary="Listar actividades por proyecto",
    description="Obtiene las actividades de un proyecto con indicadores EVM por actividad.",
)
def get_activities_by_project(
    project_id: uuid.UUID,
    db: Session = Depends(get_db),
) -> list[ActivityWithEvmResponse]:
    project_repository = ProjectRepository(db)
    if project_repository.get_project_by_id(project_id) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")

    activity_repository = ActivityRepository(db)
    activities = activity_repository.get_activities_by_project(project_id)
    return [_build_activity_with_evm_response(activity) for activity in activities]


@router.get(
    "/activities/{activity_id}",
    response_model=ActivityWithEvmResponse,
    summary="Obtener actividad",
    description="Obtiene una actividad por su identificador con indicadores EVM.",
)
def get_activity_by_id(
    activity_id: uuid.UUID,
    db: Session = Depends(get_db),
) -> ActivityWithEvmResponse:
    activity_repository = ActivityRepository(db)
    activity = activity_repository.get_activity_by_id(activity_id)
    if activity is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Activity not found")
    return _build_activity_with_evm_response(activity)


@router.put(
    "/activities/{activity_id}",
    response_model=ActivityWithEvmResponse,
    summary="Actualizar actividad",
    description="Actualiza una actividad existente.",
)
def update_activity(
    activity_id: uuid.UUID,
    payload: ActivityUpdate,
    db: Session = Depends(get_db),
) -> ActivityWithEvmResponse:
    activity_repository = ActivityRepository(db)
    activity = activity_repository.get_activity_by_id(activity_id)
    if activity is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Activity not found")

    updated = activity_repository.update_activity(activity, payload)
    return _build_activity_with_evm_response(updated)


@router.delete(
    "/activities/{activity_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar actividad",
    description="Elimina una actividad existente.",
)
def delete_activity(activity_id: uuid.UUID, db: Session = Depends(get_db)) -> Response:
    activity_repository = ActivityRepository(db)
    activity = activity_repository.get_activity_by_id(activity_id)
    if activity is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Activity not found")

    activity_repository.delete_activity(activity)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
