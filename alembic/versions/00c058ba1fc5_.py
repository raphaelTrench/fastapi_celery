"""empty message

Revision ID: 00c058ba1fc5
Revises: f33ddaa2f713
Create Date: 2022-10-17 21:32:41.769883

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = '00c058ba1fc5'
down_revision = 'f33ddaa2f713'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=128), nullable=False),
    sa.Column('email', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
