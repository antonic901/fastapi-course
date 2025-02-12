"""Add OneToMany relation between item and user profile tables

Revision ID: aab5666a2930
Revises: 2848c8a832ed
Create Date: 2025-02-12 16:17:03.887906

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aab5666a2930'
down_revision: Union[str, None] = '2848c8a832ed'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('items', sa.Column('creator_id', sa.String(), nullable=False))
    op.create_foreign_key(None, 'items', 'userprofiles', ['creator_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'items', type_='foreignkey')
    op.drop_column('items', 'creator_id')
    # ### end Alembic commands ###
