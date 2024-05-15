"""Add expires_at to tokens

Revision ID: e02e20007806
Revises: 3785b2b65395
Create Date: 2024-05-15 17:15:10.950500

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e02e20007806'
down_revision: Union[str, None] = '3785b2b65395'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_items_id'), 'items', ['id'], unique=False)
    op.add_column('tokens', sa.Column('expires_at', sa.DateTime(), nullable=False))
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_column('tokens', 'expires_at')
    op.drop_index(op.f('ix_items_id'), table_name='items')
    # ### end Alembic commands ###
