from app.features.tickets.models.tickets_models import Ticket


class TicketRepository:
    def __init__(self, db_session):
        self.db_session = db_session
    
    def get_tickets(self, status: str = None, priority: str = None):
        query = self.db_session.query(Ticket)
        
        if status:
            query = query.filter(Ticket.status == status)
        if priority:
            query = query.filter(Ticket.priority == priority)
        
        return query.all()
    

    def get_ticket_by_id(self, ticket_id: int):
        return self.db_session.query(Ticket).filter(Ticket.id == ticket_id).first()