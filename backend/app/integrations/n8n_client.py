import logging

import httpx2

logger = logging.getLogger(__name__)


class N8nClient:
    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url

    def notify_ticket_updated(self, ticket_id: int, status: str) -> None:
        try:
            response = httpx2.post(
                self.webhook_url,
                json={
                    "ticket_id": ticket_id,
                    "status": status,
                },
                timeout=5.0,
            )
            response.raise_for_status()

        except httpx2.HTTPError:
            logger.exception(
                "Failed to notify n8n about ticket %s",
                ticket_id,
            )
