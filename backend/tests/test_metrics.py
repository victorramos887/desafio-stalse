from unittest.mock import MagicMock

from app.features.metrics.service.service import ServiceMetrics


def test_calculate_ticket_metrics() -> None:
    # Mock the get_all_tickets method to return a list of tickets
    mock_tickets = [
        {"status": "open", "priority": "high", "channel": "email"},
        {"status": "closed", "priority": "low", "channel": "whatsapp"},
        {"status": "in_progress", "priority": "medium", "channel": "chat"},
        {"status": "open", "priority": "high", "channel": "email"},
    ]
    ServiceMetrics.get_all_tickets = MagicMock(return_value=mock_tickets)
    metrics = ServiceMetrics.get_metrics()

    assert metrics["total"] == 4
    assert metrics["by_status"] == {
        "open": 2,
        "closed": 1,
        "in_progress": 1,
    }
    assert metrics["by_priority"] == {
        "high": 2,
        "low": 1,
        "medium": 1,
    }
    assert metrics["by_channel"] == {
        "email": 2,
        "phone": 1,
        "chat": 1,
    }
