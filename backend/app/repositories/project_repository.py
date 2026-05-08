import uuid

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.project import Project
from app.schemas.project_schema import ProjectCreate, ProjectUpdate


class ProjectRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_projects(self) -> list[Project]:
        statement = select(Project).order_by(Project.created_at.desc())
        return list(self.db.scalars(statement).all())

    def get_project_by_id(self, project_id: uuid.UUID) -> Project | None:
        statement = select(Project).where(Project.id == project_id)
        return self.db.scalars(statement).first()

    def create_project(self, payload: ProjectCreate) -> Project:
        project = Project(**payload.model_dump())
        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)
        return project

    def update_project(self, project: Project, payload: ProjectUpdate) -> Project:
        for field, value in payload.model_dump(exclude_unset=True).items():
            setattr(project, field, value)

        self.db.commit()
        self.db.refresh(project)
        return project

    def delete_project(self, project: Project) -> None:
        self.db.delete(project)
        self.db.commit()

    # Backward-compatible aliases for existing code paths.
    def list_projects(self) -> list[Project]:
        return self.get_projects()

    def get_project(self, project_id: uuid.UUID) -> Project | None:
        return self.get_project_by_id(project_id)
