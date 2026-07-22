from fastapi.testclient import TestClient
from pytest import Session
from app.features.tickets.models.tickets_models import Ticket

def test_get_tickets_returns_saved_tickets(
    client: TestClient,
    db_session: Session,
) -> None:
    db_session.add_all(
        [
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
    )
    db_session.commit()

    response = client.get("/tickets")

    assert response.status_code == 200

    data = response.json()
    tickets_by_customer = {
        ticket["customer_name"]: ticket
        for ticket in data
    }

    assert len(data) == 2

    assert tickets_by_customer["Maria Silva"]["status"] == "open"
    assert tickets_by_customer["Maria Silva"]["priority"] == "high"

    assert tickets_by_customer["João Souza"]["status"] == "closed"
    assert tickets_by_customer["João Souza"]["channel"] == "whatsapp"
    
def test_get_tickets_by_id(
    client: TestClient,
    db_session: Session,
) -> None:
    ticket = Ticket(
        customer_name="Carlos Pereira",
        channel="email",
        status="open",
        priority="medium",
    )
    db_session.add(ticket)
    db_session.commit()

    response = client.get(f"/tickets/{ticket.id}")

    assert response.status_code == 200

    data = response.json()
    assert data["customer_name"] == "Carlos Pereira"
    assert data["channel"] == "email"
    assert data["status"] == "open"
    assert data["priority"] == "medium"