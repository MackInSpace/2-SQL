"""create customers

Revision ID: 6f7b23187360
Revises: 
Create Date: 2025-08-11 19:55:17.163892

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6f7b23187360'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.execute(
        """
        CREATE TABLE customers(
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL
        );
        """
    )


def downgrade():
    op.execute(
        """
        DROP TABLE customers;
        """
    )
