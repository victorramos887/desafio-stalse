

from fastapi.params import Depends

from app.features.tickets.repository.tickets_repository import TicketRepository


class TicketService:
    
    def __init__(self, repository: TicketRepository = Depends(TicketRepository)):
        self.repository = repository
        
    def get_tickets(self):
        return self.repository.get_tickets()
