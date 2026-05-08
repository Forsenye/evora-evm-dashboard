from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.activity_routes import router as activity_router
from app.routes.project_routes import router as project_router

app = FastAPI(
    title="EVORA API",
    description="API REST para gestion de proyectos, actividades e indicadores EVM",
    docs_url="/swagger-ui",
    openapi_url="/api-docs.json",
)

# Allows the local Vite frontend to consume the EVORA API during MVP validation.
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:5174",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
