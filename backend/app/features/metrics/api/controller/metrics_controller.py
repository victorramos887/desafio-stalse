from fastapi import APIRouter
from app.features.metrics.service.service import ServiceMetrics

router = APIRouter(prefix="/metrics", tags=["Metrics"])


@router.get("/")
async def get_metrics() -> dict:
    service = ServiceMetrics
    
    return service.get_metrics()