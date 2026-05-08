import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from app.schemas.evm_schema import ActivityIndicators


class ActivityBase(BaseModel):
    name: str = Field(min_length=1, max_length=200)
    bac: float = Field(gt=0)
    planned_progress: float = Field(ge=0, le=100)
    actual_progress: float = Field(ge=0, le=100)
    actual_cost: float = Field(ge=0)


class ActivityCreate(ActivityBase):
    pass


class ActivityUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=200)
    bac: float | None = Field(default=None, gt=0)
    planned_progress: float | None = Field(default=None, ge=0, le=100)
    actual_progress: float | None = Field(default=None, ge=0, le=100)
    actual_cost: float | None = Field(default=None, ge=0)


class ActivityResponse(ActivityBase):
    id: uuid.UUID
    project_id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    indicators: ActivityIndicators

    model_config = ConfigDict(from_attributes=True)
