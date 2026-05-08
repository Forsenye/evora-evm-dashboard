import uuid

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.activity import Activity
from app.schemas.activity_schema import ActivityCreate, ActivityUpdate


class ActivityRepository:
    def __init__(self, db: Session):
        self.db = db

    def list_by_project(self, project_id: uuid.UUID) -> list[Activity]:
        statement = (
            select(Activity)
            .where(Activity.project_id == project_id)
            .order_by(Activity.created_at.asc())
        )
        return list(self.db.scalars(statement).all())

    def get_activity(self, activity_id: uuid.UUID) -> Activity | None:
        statement = select(Activity).where(Activity.id == activity_id)
        return self.db.scalars(statement).first()

    def create_activity(self, project_id: uuid.UUID, payload: ActivityCreate) -> Activity:
        activity = Activity(project_id=project_id, **payload.model_dump())
        self.db.add(activity)
        self.db.commit()
        self.db.refresh(activity)
        return activity

    def update_activity(self, activity: Activity, payload: ActivityUpdate) -> Activity:
        for field, value in payload.model_dump(exclude_unset=True).items():
            setattr(activity, field, value)

        self.db.commit()
        self.db.refresh(activity)
        return activity

    def delete_activity(self, activity: Activity) -> None:
        self.db.delete(activity)
        self.db.commit()
