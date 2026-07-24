from fastapi.testclient import TestClient
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.features.tickets.models.tickets_models import Ticket


def test_should_save_and_find_ticket(db_session: Session):
    ticket = Ticket(customer_name="John Doe", channel="email")
    db_session.add(ticket)
    db_session.commit()

    stmt = select(Ticket).where(Ticket.id == ticket.id)
    result = db_session.execute(stmt).scalar_one_or_none()

    assert result is not None
    assert result.customer_name == "John Doe"
    assert result.channel == "email"


def test_should_select_ticket_by_id(db_session: Session):
    ticket = Ticket(customer_name="Jane Smith", channel="phone")
    db_session.add(ticket)
    db_session.commit()

    stmt = select(Ticket).where(Ticket.id == ticket.id)
    result = db_session.execute(stmt).scalar_one_or_none()

    assert result is not None
    assert result.customer_name == "Jane Smith"
    assert result.channel == "phone"


def test_get_tickets_returns_saved_tickets(
    client: TestClient,
    db_session: Session,
) -> None:
    tickets = [
        Ticket(
            customer_name="Maria Silva",
            channel="email",
            status="open",
            priority="high",
        ),
        Ticket(
            customer_name="João Souza",
            channel="whatsapp",
            status="closed",
            priority="low",
        ),
    ]

    db_session.add_all(tickets)
    db_session.commit()

    response = client.get("/tickets")

    assert response.status_code == 200

    data = response.json()

    assert len(data["items"]) == 2
    assert data["page"] == 1
    assert data["page_size"] == 10
    assert data["total_items"] == 2
    assert data["total_pages"] == 1
