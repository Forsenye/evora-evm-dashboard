from fastapi import FastAPI

from app.routes.activity_routes import router as activity_router
from app.routes.project_routes import router as project_router

app = FastAPI(
    title="EVORA API",
    description="API REST para gestion de proyectos, actividades e indicadores EVM",
    docs_url="/swagger-ui",
    openapi_url="/api-docs.json",
)


@app.get(
    "/health",
    summary="Health check",
    description="Validate API availability.",
)
def health_check() -> dict[str, str]:
    return {"status": "ok", "service": "EVORA API"}


app.include_router(project_router)
app.include_router(activity_router)
