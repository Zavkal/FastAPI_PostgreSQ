"""'number'

Revision ID: a714d4f37e70
Revises: 5a5d821d2d2c
Create Date: 2023-09-12 16:19:50.901149

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a714d4f37e70'
down_revision: Union[str, None] = '5a5d821d2d2c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users", sa.Column("number", sa.String, primary_key=True, nullable=False))


def downgrade() -> None:
    op.drop_column("users", "number")
