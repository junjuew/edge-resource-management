"""add datastat

Revision ID: 712b1042ea3c
Revises: d741ee0ea4a9
Create Date: 2019-05-13 16:03:35.837462

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '712b1042ea3c'
down_revision = 'd741ee0ea4a9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('DataStat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('app', sa.String(length=512), nullable=False),
    sa.Column('trace', sa.String(length=512), nullable=False),
    sa.Column('value', sa.String(length=8192), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('DataStat')
    # ### end Alembic commands ###
