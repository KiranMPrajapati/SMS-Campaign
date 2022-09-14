"""empty message

Revision ID: 2e2fe1b6091e
Revises: 0ea2e5b2f7cf
Create Date: 2018-08-14 11:16:27.260221

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e2fe1b6091e'
down_revision = '0ea2e5b2f7cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('campaign', sa.Column('message', sa.String(), nullable=True))
    op.add_column('campaign', sa.Column('title', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('campaign', 'title')
    op.drop_column('campaign', 'message')
    # ### end Alembic commands ###
