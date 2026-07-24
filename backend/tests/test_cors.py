from fastapi.testclient import TestClient


def test_cors_preflight_allows_frontend_origin(client: TestClient):
    response = client.options(
        "/tickets",
        headers={
            "Origin": "http://localhost:3000",
            "Access-Control-Request-Method": "GET",
        },
    )

    assert response.status_code == 200
    assert response.headers["access-control-allow-origin"] == "http://localhost:3000"
