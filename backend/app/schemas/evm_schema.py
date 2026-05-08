from pydantic import BaseModel, Field


class EvmInput(BaseModel):
    bac: float = Field(gt=0)
    planned_progress: float = Field(ge=0, le=100)
    actual_progress: float = Field(ge=0, le=100)
    actual_cost: float = Field(ge=0)


class ActivityIndicators(BaseModel):
    pv: float
    ev: float
    cv: float
    sv: float
    cpi: float | None
    spi: float | None
    eac: float | None
    vac: float | None
    cpi_status: str
    spi_status: str


class ProjectSummary(BaseModel):
    activity_count: int
    total_bac: float
    total_pv: float
    total_ev: float
    total_ac: float
    total_cv: float
    total_sv: float
    total_eac: float | None
    total_vac: float | None
    cpi: float | None
    spi: float | None
    cpi_status: str
    spi_status: str
