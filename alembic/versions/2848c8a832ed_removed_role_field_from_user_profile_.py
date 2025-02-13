"""Removed role field from user profile table

Revision ID: 2848c8a832ed
Revises: 1c5422ac3254
Create Date: 2025-02-12 12:12:07.990619

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '2848c8a832ed'
down_revision: Union[str, None] = '1c5422ac3254'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

userrole_enum = sa.Enum('NORMAL', 'ADMIN', 'SUPER_ADMIN', name='userrole')

def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('userprofiles', 'role')
    userrole_enum.drop(op.get_bind(), checkfirst=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    userrole_enum.create(op.get_bind(), checkfirst=True)
    op.add_column('userprofiles', sa.Column('role', postgresql.ENUM('NORMAL', 'ADMIN', 'SUPER_ADMIN', name='userrole'), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
