import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from app.schemas.evm_schema import ProjectSummary


class ProjectBase(BaseModel):
    name: str = Field(min_length=1, max_length=150)
    description: str | None = Field(default=None, max_length=1000)


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=150)
    description: str | None = Field(default=None, max_length=1000)


class ProjectResponse(ProjectBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    summary: ProjectSummary

    model_config = ConfigDict(from_attributes=True)
