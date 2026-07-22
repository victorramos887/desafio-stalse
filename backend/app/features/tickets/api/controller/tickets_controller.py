from fastapi import APIRouter, Depends, status
from app.features.tickets.service.ticket_service import TicketService

router = APIRouter(prefix="/tickets", tags=["Tickets"])

@router.get(
    "/",
    status_code = status.HTTP_200_OK,
    dependencies=[Depends(TicketService)]
)
async def get_tickets(
    service: TicketService = Depends(TicketService)
):
    return service.get_tickets()