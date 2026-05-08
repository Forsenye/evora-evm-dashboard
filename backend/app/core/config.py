import os

from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "EVORA API"
    database_url: str = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg2://postgres:postgres@localhost:5432/evora",
    )


settings = Settings()
