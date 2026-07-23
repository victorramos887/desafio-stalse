from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.features.tickets.api.schemas.tickets_schemas import SchemaPostTicket, TicketEventCreate
from app.features.tickets.repository.tickets_repository import TicketRepository
from app.features.tickets.service.exceptions.tickets_exception import (
    TicketNotFoundException,
)
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

    try:
        return service.get_ticket_by_id(ticket_id)
    except TicketNotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e


@router.patch("/{ticket_id}", status_code=status.HTTP_200_OK)
def update_ticket(
    ticket_id: int,
    ticket_data: dict,
    db_session: Annotated[Session, Depends(get_db)],
):
    repository = TicketRepository(db_session)
    service = TicketService(repository)

    try:
        return service.update_ticket(ticket_id, ticket_data)
    except TicketNotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e


@router.post("", status_code=status.HTTP_201_CREATED)
def create_ticket(
    ticket_data: SchemaPostTicket,
    db_session: Annotated[Session, Depends(get_db)],
):
    repository = TicketRepository(db_session)
    service = TicketService(repository)

    return service.create_ticket(ticket_data.model_dump())


@router.post("/ticket-events", status_code=status.HTTP_200_OK)
def create_ticket_event(
    ticket_event_data: TicketEventCreate,
):    
    return ticket_event_data
