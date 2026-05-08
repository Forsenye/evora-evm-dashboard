from pydantic import BaseModel, Field


class EvmInput(BaseModel):
    bac: float = Field(ge=0)
    planned_progress: float = Field(ge=0, le=100)
    actual_progress: float = Field(ge=0, le=100)
    actual_cost: float = Field(ge=0)


class EvmStatus(BaseModel):
    cpi_status: str
    spi_status: str


class ActivityEvmIndicators(BaseModel):
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
    status: EvmStatus


class ProjectEvmSummary(BaseModel):
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
    status: EvmStatus


class ProjectEvmDashboardSummary(BaseModel):
    bac: float
    pv: float
    ev: float
    ac: float
    cv: float
    sv: float
    cpi: float | None
    spi: float | None
    eac: float | None
    vac: float | None
    cost_status: str
    schedule_status: str


class ActivityWithEvmResponse(BaseModel):
    id: str
    name: str
    bac: float
    planned_progress: float
    actual_progress: float
    actual_cost: float
    evm: ProjectEvmDashboardSummary


class ProjectEvmSummaryResponse(BaseModel):
    project_id: str
    project_name: str
    total_activities: int
    summary: ProjectEvmDashboardSummary
    activities: list[ActivityWithEvmResponse]
    status: str | None = None


# Backward-compatible aliases for existing imports.
ActivityIndicators = ActivityEvmIndicators
ProjectSummary = ProjectEvmSummary
