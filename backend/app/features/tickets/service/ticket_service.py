from app.features.tickets.repository.tickets_repository import TicketRepository
from app.features.tickets.service.exceptions.tickets_exception import (
    TicketNotFoundException,
)


class TicketService:
    def __init__(self, repository: TicketRepository):
        self.repository = repository
        self.ticket_not_found_exception = TicketNotFoundException

    def get_tickets(self):
        return self.repository.get_tickets()

    def get_ticket_by_id(self, ticket_id: int):
        ticket = self.repository.get_ticket_by_id(ticket_id)
        if not ticket:
            raise self.ticket_not_found_exception(ticket_id)
        return ticket

    def update_ticket(self, ticket_id: int, ticket_data: dict):
        ticket = self.repository.get_ticket_by_id(ticket_id)
        if not ticket:
            raise self.ticket_not_found_exception(ticket_id)
        return self.repository.update_ticket(ticket, ticket_data)

    def create_ticket(self, ticket_data: dict):
        ticket = self.repository.create_ticket(ticket_data)
        return ticket
