from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.core.config import get_settings
from app.features.tickets.api.controller.tickets_controller import router as tickets_router
from app.core.database import SessionLocal
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

app.include_router(tickets_router)

@app.get("/health")
async def health_check():
    return {"message": "Hello, World!", "status": "ok"}