from sqlalchemy import select
from sqlalchemy.orm import Session

from app.features.tickets.models import Ticket


def test_should_save_and_find_ticket(db_session: Session):
    ticket = Ticket(customer_name="John Doe", channel="email")
    db_session.add(ticket)
    db_session.commit()

    stmt = select(Ticket).where(Ticket.id == ticket.id)
    result = db_session.execute(stmt).scalar_one_or_none()

    assert result is not None
    assert result.customer_name == "John Doe"
    assert result.channel == "email"