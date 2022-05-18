"""empty message

Revision ID: ec3ae4de8792
Revises: 
Create Date: 2022-05-18 18:54:16.966769

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec3ae4de8792'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('kline',
    sa.Column('Symbol', sa.VARCHAR(length=20), nullable=False),
    sa.Column('exchange', sa.VARCHAR(length=10), nullable=False),
    sa.Column('timeframe', sa.VARCHAR(length=3), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=False),
    sa.Column('open', sa.NUMERIC(precision=20, scale=8), nullable=False),
    sa.Column('close', sa.NUMERIC(precision=20, scale=8), nullable=False),
    sa.Column('high', sa.NUMERIC(precision=20, scale=8), nullable=False),
    sa.Column('low', sa.NUMERIC(precision=20, scale=8), nullable=False),
    sa.Column('volume', sa.NUMERIC(precision=20, scale=8), nullable=True),
    sa.Column('amount', sa.NUMERIC(precision=20, scale=8), nullable=True),
    sa.PrimaryKeyConstraint('start_time')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('kline')
    # ### end Alembic commands ###
