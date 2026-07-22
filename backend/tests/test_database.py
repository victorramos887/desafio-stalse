from sqlalchemy import text
from sqlalchemy.orm import Session


def test_database_connection(db_session: Session) -> None:
    result = db_session.execute(text("SELECT 1"))
    assert result.scalar() == 1