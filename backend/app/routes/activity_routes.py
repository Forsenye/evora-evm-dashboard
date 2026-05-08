import uuid

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.activity import Activity
from app.repositories.activity_repository import ActivityRepository
from app.repositories.project_repository import ProjectRepository
from app.schemas.activity_schema import ActivityCreate, ActivityResponse, ActivityUpdate
from app.schemas.evm_schema import EvmInput
from app.services.evm_calculation_service import EvmCalculationService

router = APIRouter(tags=["activities"])


def _build_activity_response(activity: Activity) -> ActivityResponse:
    indicators = EvmCalculationService.calculate_activity_indicators(
        EvmInput(
            bac=float(activity.bac),
            planned_progress=float(activity.planned_progress),
            actual_progress=float(activity.actual_progress),
            actual_cost=float(activity.actual_cost),
        )
    )

    return ActivityResponse(
        id=activity.id,
        project_id=activity.project_id,
        name=activity.name,
        bac=float(activity.bac),
        planned_progress=float(activity.planned_progress),
        actual_progress=float(activity.actual_progress),
        actual_cost=float(activity.actual_cost),
        created_at=activity.created_at,
        updated_at=activity.updated_at,
        indicators=indicators,
    )


@router.get(
    "/projects/{project_id}/activities",
    response_model=list[ActivityResponse],
    summary="List activities by project",
    description="Return all activities for a project with EVM indicators per activity.",
)
def list_project_activities(
    project_id: uuid.UUID,
    db: Session = Depends(get_db),
) -> list[ActivityResponse]:
    project_repository = ProjectRepository(db)
    if project_repository.get_project(project_id) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")

    activity_repository = ActivityRepository(db)
    activities = activity_repository.list_by_project(project_id)
    return [_build_activity_response(activity) for activity in activities]


@router.post(
    "/projects/{project_id}/activities",
    response_model=ActivityResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create activity",
    description="Create a new activity associated to one project.",
)
def create_activity(
    project_id: uuid.UUID,
    payload: ActivityCreate,
    db: Session = Depends(get_db),
) -> ActivityResponse:
    project_repository = ProjectRepository(db)
    if project_repository.get_project(project_id) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")

    activity_repository = ActivityRepository(db)
    activity = activity_repository.create_activity(project_id, payload)
    return _build_activity_response(activity)


@router.get(
    "/activities/{activity_id}",
    response_model=ActivityResponse,
    summary="Get activity by id",
    description="Return one activity with calculated EVM indicators.",
)
def get_activity(activity_id: uuid.UUID, db: Session = Depends(get_db)) -> ActivityResponse:
    repository = ActivityRepository(db)
    activity = repository.get_activity(activity_id)
    if activity is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Activity not found")
    return _build_activity_response(activity)


@router.put(
    "/activities/{activity_id}",
    response_model=ActivityResponse,
    summary="Update activity",
    description="Update one activity by identifier.",
)
def update_activity(
    activity_id: uuid.UUID,
    payload: ActivityUpdate,
    db: Session = Depends(get_db),
) -> ActivityResponse:
    repository = ActivityRepository(db)
    activity = repository.get_activity(activity_id)
    if activity is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Activity not found")

    updated = repository.update_activity(activity, payload)
    return _build_activity_response(updated)


@router.delete(
    "/activities/{activity_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete activity",
    description="Delete one activity by identifier.",
)
def delete_activity(activity_id: uuid.UUID, db: Session = Depends(get_db)) -> Response:
    repository = ActivityRepository(db)
    activity = repository.get_activity(activity_id)
    if activity is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Activity not found")

    repository.delete_activity(activity)
    return Response(status_code=status.HTTP_204_NO_CONTENT)