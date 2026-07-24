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
    tickets_by_customer = {ticket["customer_name"]: ticket for ticket in data["items"]}

    assert len(data["items"]) == 2
    assert data["page"] == 1
    assert data["page_size"] == 10
    assert data["total_items"] == 2
    assert data["total_pages"] == 1

    assert tickets_by_customer["Maria Silva"]["status"] == "open"
    assert tickets_by_customer["Maria Silva"]["priority"] == "high"

    assert tickets_by_customer["João Souza"]["status"] == "closed"
    assert tickets_by_customer["João Souza"]["channel"] == "whatsapp"


def test_get_tickets_with_custom_pagination(
    client: TestClient,
    db_session: Session,
) -> None:
    db_session.add_all(
        [
            Ticket(customer_name=f"Cliente {index}", channel="email")
            for index in range(1, 13)
        ]
    )
    db_session.commit()

    response = client.get("/tickets?page=2&page_size=5")

    assert response.status_code == 200

    data = response.json()

    assert data["page"] == 2
    assert data["page_size"] == 5
    assert data["total_items"] == 12
    assert data["total_pages"] == 3
    assert len(data["items"]) == 5


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


def test_get_tickets_by_id_not_found(
    client: TestClient,
) -> None:
    response = client.get("/tickets/9999")  # Assuming 9999 is a non-existent ticket ID

    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Ticket with ID 9999 not found."


def test_patch_ticket_status(
    client: TestClient,
    db_session: Session,
) -> None:
    ticket = Ticket(
        customer_name="Ana Costa",
        channel="chat",
        status="open",
        priority="low",
    )
    db_session.add(ticket)
    db_session.commit()

    response = client.patch(f"/tickets/{ticket.id}", json={"status": "closed"})

    assert response.status_code == 200

    data = response.json()
    assert data["status"] == "closed"


def test_delete_tikect_status(
    client: TestClient,
    db_session: Session,
) -> None:
    ticket = Ticket(
        customer_name="Pedro Lima",
        channel="phone",
        status="open",
        priority="high",
    )
    db_session.add(ticket)
    db_session.commit()

    response = client.patch(f"/tickets/{ticket.id}", json={"status": "deleted"})

    assert response.status_code == 200

    data = response.json()
    assert data["status"] == "deleted"


def test_post_ticket(
    client: TestClient,
    db_session: Session,
) -> None:
    ticket_data = {
        "customer_name": "Lucas Almeida",
        "channel": "email",
        "status": "open",
        "priority": "medium",
    }

    response = client.post("/tickets", json=ticket_data)

    assert response.status_code == 201

    data = response.json()
    assert data["customer_name"] == "Lucas Almeida"
    assert data["channel"] == "email"
    assert data["status"] == "open"
    assert data["priority"] == "medium"
