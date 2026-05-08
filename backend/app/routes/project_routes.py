import uuid

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.activity import Activity
from app.models.project import Project
from app.repositories.project_repository import ProjectRepository
from app.schemas.evm_schema import EvmInput
from app.schemas.project_schema import ProjectCreate, ProjectResponse, ProjectUpdate
from app.services.evm_calculation_service import EvmCalculationService

router = APIRouter(prefix="/projects", tags=["projects"])


def _to_evm_input(activity: Activity) -> EvmInput:
    return EvmInput(
        bac=float(activity.bac),
        planned_progress=float(activity.planned_progress),
        actual_progress=float(activity.actual_progress),
        actual_cost=float(activity.actual_cost),
    )


def _build_project_response(project: Project) -> ProjectResponse:
    activities = [_to_evm_input(activity) for activity in project.activities]
    summary = EvmCalculationService.calculate_project_summary(activities)

    return ProjectResponse(
        id=project.id,
        name=project.name,
        description=project.description,
        created_at=project.created_at,
        updated_at=project.updated_at,
        summary=summary,
    )


@router.get(
    "",
    response_model=list[ProjectResponse],
    summary="List projects",
    description="Return all registered projects with EVM consolidated summary.",
)
def list_projects(db: Session = Depends(get_db)) -> list[ProjectResponse]:
    repository = ProjectRepository(db)
    projects = repository.list_projects()
    return [_build_project_response(project) for project in projects]


@router.get(
    "/{project_id}",
    response_model=ProjectResponse,
    summary="Get project by id",
    description="Return one project and its consolidated EVM indicators.",
)
def get_project(project_id: uuid.UUID, db: Session = Depends(get_db)) -> ProjectResponse:
    repository = ProjectRepository(db)
    project = repository.get_project(project_id)
    if project is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    return _build_project_response(project)


@router.post(
    "",
    response_model=ProjectResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create project",
    description="Create a new project.",
)
def create_project(payload: ProjectCreate, db: Session = Depends(get_db)) -> ProjectResponse:
    repository = ProjectRepository(db)
    project = repository.create_project(payload)
    return _build_project_response(project)


@router.put(
    "/{project_id}",
    response_model=ProjectResponse,
    summary="Update project",
    description="Update one project by identifier.",
)
def update_project(
    project_id: uuid.UUID,
    payload: ProjectUpdate,
    db: Session = Depends(get_db),
) -> ProjectResponse:
    repository = ProjectRepository(db)
    project = repository.get_project(project_id)
    if project is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")

    updated = repository.update_project(project, payload)
    return _build_project_response(updated)


@router.delete(
    "/{project_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete project",
    description="Delete one project and its activities.",
)
def delete_project(project_id: uuid.UUID, db: Session = Depends(get_db)) -> Response:
    repository = ProjectRepository(db)
    project = repository.get_project(project_id)
    if project is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")

    repository.delete_project(project)
    return Response(status_code=status.HTTP_204_NO_CONTENT)