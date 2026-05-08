import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, field_validator


class ActivityBase(BaseModel):
    name: str = Field(min_length=1, max_length=150)
    bac: float = Field(gt=0)
    planned_progress: float = Field(ge=0, le=100)
    actual_progress: float = Field(ge=0, le=100)
    actual_cost: float = Field(ge=0)

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        normalized = value.strip()
        if not normalized:
            raise ValueError("Activity name must not be empty")
        return normalized


class ActivityCreate(ActivityBase):
    pass


class ActivityUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=150)
    bac: float | None = Field(default=None, gt=0)
    planned_progress: float | None = Field(default=None, ge=0, le=100)
    actual_progress: float | None = Field(default=None, ge=0, le=100)
    actual_cost: float | None = Field(default=None, ge=0)

    @field_validator("name")
    @classmethod
    def validate_optional_name(cls, value: str | None) -> str | None:
        if value is None:
            return None
        normalized = value.strip()
        if not normalized:
            raise ValueError("Activity name must not be empty")
        return normalized


class ActivityResponse(ActivityBase):
    id: uuid.UUID
    project_id: uuid.UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ActivityEvmData(BaseModel):
    pv: float
    ev: float
    cv: float
    sv: float
    cpi: float | None
    spi: float | None
    eac: float | None
    vac: float | None
    cost_status: str
    schedule_status: str


class ActivityWithEvmResponse(ActivityResponse):
    evm: ActivityEvmData
