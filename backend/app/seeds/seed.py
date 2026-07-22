import json
from pathlib import Path

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.features.tickets.models.tickets_models import Ticket

SEED_FILE_PATH = Path(__file__).parent / "tickets.json"


def seed_tickets(session: Session) -> int:
    existing_tickets = session.execute(select(Ticket)).scalars().all()

    if existing_tickets:
        return 0
    with open(SEED_FILE_PATH, encoding="utf-8") as file:
        tickets_data = json.load(file)

    tickets_to_seed = [Ticket(**ticket) for ticket in tickets_data]

    session.add_all(tickets_to_seed)
    session.commit()

    return len(tickets_to_seed)


if __name__ == "__main__":
    with SessionLocal() as session:
        inserted = seed_tickets(session)

    print(f"{inserted} tickets inseridos.")
