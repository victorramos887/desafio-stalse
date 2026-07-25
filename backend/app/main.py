from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import get_settings
from app.core.database import SessionLocal
from app.features.metrics.api.controller.metrics_controller import (
    router as metrics_router,
)
from app.features.tickets.api.controller.tickets_controller import (
    router as tickets_router,
)
from prometheus_fastapi_instrumentator import Instrumentator

from app.seeds.seed import seed_tickets

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    with SessionLocal() as session:
        inserted = seed_tickets(session)
        print(f"Inserted {inserted} tickets into the database.")

    yield
    print("Application shutdown complete.")


app = FastAPI(title=settings.app_name, version=settings.app_version, lifespan=lifespan)

Instrumentator().instrument(app).expose(
    app,
    endpoint="/metrics/prometheus",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.frontend_cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tickets_router)
app.include_router(metrics_router)


@app.get("/health")
async def health_check():
    return {"message": "Hello, World!", "status": "ok"}
