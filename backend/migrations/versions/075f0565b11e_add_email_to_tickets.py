"""Add email column to tickets table

Revision ID: 075f0565b11e
Revises: 659488837d08
Create Date: 2026-07-24 11:03:22.113170

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '075f0565b11e'
down_revision: Union[str, Sequence[str], None] = '659488837d08'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('tickets', sa.Column('email', sa.String(length=100), nullable=True))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('tickets', 'email')
