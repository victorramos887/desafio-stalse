from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.features.tickets.models.tickets_models import Ticket
from app.seeds.seed import seed_tickets


def test_seed_should_insert_tickets_in_empty_database(
    db_session: Session,
) -> None:
    inserted = seed_tickets(db_session)

    total = db_session.scalar(select(func.count()).select_from(Ticket))

    assert inserted == 100
    assert total == 100


def test_seed_should_not_duplicate_tickets(
    db_session: Session,
) -> None:
    first_inserted = seed_tickets(db_session)
    second_inserted = seed_tickets(db_session)

    total = db_session.scalar(select(func.count()).select_from(Ticket))

    assert first_inserted == 100
    assert second_inserted == 0
    assert total == 100
