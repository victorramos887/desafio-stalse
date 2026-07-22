from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.features.tickets.repository.tickets_repository import TicketRepository
from app.features.tickets.service.ticket_service import TicketService


router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"],
)


@router.get(
    "",
    status_code=status.HTTP_200_OK,
)
def get_tickets(
    db_session: Annotated[Session, Depends(get_db)],
):
    repository = TicketRepository(db_session)
    service = TicketService(repository)

    return service.get_tickets()

@router.get("/{ticket_id}", status_code=status.HTTP_200_OK)
def get_ticket_by_id(
    ticket_id: int,
    db_session: Annotated[Session, Depends(get_db)],
):
    repository = TicketRepository(db_session)
    service = TicketService(repository)

    return service.get_ticket_by_id(ticket_id)