from app.features.metrics.service.service import ServiceMetrics


def test_calculate_ticket_metrics() -> None:
    tickets = [
        {
            "channel": "email",
            "status": "open",
            "priority": "high",
        },
        {
            "channel": "email",
            "status": "closed",
            "priority": "low",
        },
        {
            "channel": "whatsapp",
            "status": "open",
            "priority": "high",
        },
    ]

    metrics = ServiceMetrics.get_metrics(tickets)

    assert metrics["total"] == 3
    assert metrics["by_status"] == {
        "open": 2,
        "closed": 1,
    }
    assert metrics["by_priority"] == {
        "high": 2,
        "low": 1,
    }
    assert metrics["by_channel"] == {
        "email": 2,
        "whatsapp": 1,
    }