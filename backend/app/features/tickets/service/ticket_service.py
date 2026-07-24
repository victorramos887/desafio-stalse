from app.features.tickets.repository.tickets_repository import TicketRepository
from app.features.tickets.service.exceptions.tickets_exception import (
    TicketNotFoundException,
)
from app.integrations.n8n_client import N8nClient
from app.core.config import get_settings

settings = get_settings()

class TicketService:
    def __init__(self, repository: TicketRepository):
        self.repository = repository
        self.ticket_not_found_exception = TicketNotFoundException
        self.integration_client = N8nClient(webhook_url=settings.n8n_webhook_url)

    def get_tickets(self, page: int, page_size: int):
        items, total_items = self.repository.get_tickets_paginated(
            page=page,
            page_size=page_size,
        )

        total_pages = (total_items + page_size - 1) // page_size if total_items else 0

        return {
            "items": items,
            "page": page,
            "page_size": page_size,
            "total_items": total_items,
            "total_pages": total_pages,
        }

    def get_ticket_by_id(self, ticket_id: int):
        ticket = self.repository.get_ticket_by_id(ticket_id)
        if not ticket:
            raise self.ticket_not_found_exception(ticket_id)
        return ticket

    def update_ticket(self, ticket_id: int, ticket_data: dict):
        ticket = self.repository.get_ticket_by_id(ticket_id)
        if not ticket:
            raise self.ticket_not_found_exception(ticket_id)
        updated_ticket = self.repository.update_ticket(ticket, ticket_data)
        self.integration_client.notify_ticket_updated(ticket_id, updated_ticket.status)
        return updated_ticket

    def create_ticket(self, ticket_data: dict):
        ticket = self.repository.create_ticket(ticket_data)
        self.integration_client.notify_ticket_updated(ticket.id, ticket.status)
        return ticket
