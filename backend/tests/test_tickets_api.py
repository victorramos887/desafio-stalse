from fastapi.testclient import TestClient


def test_get_tickets(client: TestClient) -> None:
    response = client.get("/tickets")

    assert response.status_code == 200
    assert isinstance(response.json(), list)