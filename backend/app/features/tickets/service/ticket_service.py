

from fastapi.params import Depends

from app.features.tickets.repository.tickets_repository import TicketRepository


class TicketService:
    
    def __init__(self, repository: TicketRepository = Depends(TicketRepository)):
        self.repository = repository
        
    def get_tickets(self):
        return self.repository.get_tickets()

    def get_ticket_by_id(self, ticket_id: int):
        ticket = self.repository.get_ticket_by_id(ticket_id)
        if not ticket:
            raise ValueError(f"Ticket with ID {ticket_id} not found.")
        return ticket