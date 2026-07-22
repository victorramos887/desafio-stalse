

from fastapi.params import Depends

from app.features.tickets.repository.tickets_repository import TicketRepository
from app.features.tickets.service.exceptions.tickets_exception import TicketNotFoundException

class TicketService:
    
    def __init__(self, repository: TicketRepository = Depends(TicketRepository)):
        self.repository = repository
        self.ticket_not_found_exception = TicketNotFoundException
        
    def get_tickets(self):
        return self.repository.get_tickets()

    def get_ticket_by_id(self, ticket_id: int):
        ticket = self.repository.get_ticket_by_id(ticket_id)
        if not ticket:
            raise self.ticket_not_found_exception(ticket_id)
        return ticket