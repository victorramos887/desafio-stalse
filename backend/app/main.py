from fastapi import FastAPI

from app.core.config import get_settings
from app.features.tickets.api.controller.tickets_controller import router as tickets_router


settings = get_settings()

app = FastAPI(title=settings.app_name, version=settings.app_version)

app.include_router(tickets_router)


@app.get("/health")
async def health_check():
    return {"message": "Hello, World!", "status": "ok"}