import uuid

from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from app.models.project import Project
from app.schemas.project_schema import ProjectCreate, ProjectUpdate


class ProjectRepository:
    def __init__(self, db: Session):
        self.db = db

    def list_projects(self) -> list[Project]:
        statement = (
            select(Project)
            .options(selectinload(Project.activities))
            .order_by(Project.created_at.desc())
        )
        return list(self.db.scalars(statement).all())

    def get_project(self, project_id: uuid.UUID) -> Project | None:
        statement = (
            select(Project)
            .options(selectinload(Project.activities))
            .where(Project.id == project_id)
        )
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