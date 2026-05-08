from __future__ import annotations

import uuid
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint, DateTime, Float, ForeignKey, String, Uuid, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base

if TYPE_CHECKING:
    from app.models.project import Project


class Activity(Base):
    __tablename__ = "activities"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    project_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey("projects.id", ondelete="CASCADE"),
        nullable=False,
    )
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    bac: Mapped[float] = mapped_column(Float, nullable=False)
    planned_progress: Mapped[float] = mapped_column(Float, nullable=False)
    actual_progress: Mapped[float] = mapped_column(Float, nullable=False)
    actual_cost: Mapped[float] = mapped_column(Float, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )

    project: Mapped[Project] = relationship("Project", back_populates="activities")

    __table_args__ = (
        CheckConstraint("bac > 0", name="ck_activities_bac_positive"),
        CheckConstraint(
            "planned_progress >= 0 AND planned_progress <= 100",
            name="ck_activities_planned_progress_range",
        ),
        CheckConstraint(
            "actual_progress >= 0 AND actual_progress <= 100",
            name="ck_activities_actual_progress_range",
        ),
        CheckConstraint("actual_cost >= 0", name="ck_activities_actual_cost_nonnegative"),
    )