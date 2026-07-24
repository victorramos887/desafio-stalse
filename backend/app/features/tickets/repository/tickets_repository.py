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

    def get_tickets_paginated(
        self,
        page: int,
        page_size: int,
        status: str = None,
        priority: str = None,
    ):
        query = self.db_session.query(Ticket)

        if status:
            query = query.filter(Ticket.status == status)
        if priority:
            query = query.filter(Ticket.priority == priority)

        total_items = query.count()
        items = (
            query.order_by(Ticket.id.asc())
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )

        return items, total_items

    def get_ticket_by_id(self, ticket_id: int):
        return self.db_session.query(Ticket).filter(Ticket.id == ticket_id).first()

    def update_ticket(self, ticket: Ticket, ticket_data: dict):

        for key, value in ticket_data.items():
            setattr(ticket, key, value)

        self.db_session.commit()
        return ticket

    def create_ticket(self, ticket_data: dict):
        ticket = Ticket(**ticket_data)
        self.db_session.add(ticket)
        self.db_session.commit()
        return ticket
