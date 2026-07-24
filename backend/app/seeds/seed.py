import json
from datetime import datetime
from pathlib import Path

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.features.tickets.models.tickets_models import Ticket

SEED_FILE_PATH = Path(__file__).parent / "tickets.json"


def _parse_iso_datetime(value: str) -> datetime:
    # Support ISO8601 strings ending with Z (UTC) from the seed file.
    if value.endswith("Z"):
        value = value.replace("Z", "+00:00")
    return datetime.fromisoformat(value)


def seed_tickets(session: Session) -> int:
    existing_tickets = session.execute(select(Ticket)).scalars().all()

    if existing_tickets:
        return 0
    with open(SEED_FILE_PATH, encoding="utf-8") as file:
        tickets_data = json.load(file)

    for ticket in tickets_data:
        created_at = ticket.get("created_at")
        updated_at = ticket.get("updated_at")

        if isinstance(created_at, str):
            ticket["created_at"] = _parse_iso_datetime(created_at)
        if isinstance(updated_at, str):
            ticket["updated_at"] = _parse_iso_datetime(updated_at)

    tickets_to_seed = [Ticket(**ticket) for ticket in tickets_data]

    session.add_all(tickets_to_seed)
    session.commit()

    return len(tickets_to_seed)


if __name__ == "__main__":
    with SessionLocal() as session:
        inserted = seed_tickets(session)

    print(f"{inserted} tickets inseridos.")
