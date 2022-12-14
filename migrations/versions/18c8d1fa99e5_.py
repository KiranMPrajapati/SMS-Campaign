"""empty message

Revision ID: 18c8d1fa99e5
Revises: a17619886ea0
Create Date: 2018-08-17 16:43:05.798978

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '18c8d1fa99e5'
down_revision = 'a17619886ea0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('campaign', 'created')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('campaign', sa.Column('created', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
