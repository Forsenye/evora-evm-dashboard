import uuid

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories.project_repository import ProjectRepository
from app.schemas.project_schema import ProjectCreate, ProjectResponse, ProjectUpdate

router = APIRouter(prefix="/api/v1/projects", tags=["projects"])


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
