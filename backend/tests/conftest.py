import uuid

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool

from app.core.database import Base, get_db
from app.main import app
from app.models.project import Project

TEST_DATABASE_URL = "sqlite+pysqlite:///:memory:"


def _build_test_session() -> Session:
    engine = create_engine(
        TEST_DATABASE_URL,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
        future=True,
    )
    Base.metadata.create_all(bind=engine)
    testing_session_local = sessionmaker(bind=engine, autocommit=False, autoflush=False)
    return testing_session_local()


@pytest.fixture()
def db_session() -> Session:
    db = _build_test_session()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def client(db_session: Session) -> TestClient:
    def _override_get_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = _override_get_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


@pytest.fixture()
def seeded_project(db_session: Session) -> Project:
    project = Project(
        id=uuid.uuid4(),
        name="Proyecto semilla",
        description="Proyecto para pruebas de integracion",
    )
    db_session.add(project)
    db_session.commit()
    db_session.refresh(project)
    return project
