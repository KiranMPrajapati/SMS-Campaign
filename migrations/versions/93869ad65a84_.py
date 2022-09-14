"""empty message

Revision ID: 93869ad65a84
Revises: 89dc24db0e79
Create Date: 2018-08-14 11:09:30.113972

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93869ad65a84'
down_revision = '89dc24db0e79'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('contact', 'number')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contact', sa.Column('number', sa.VARCHAR(length=10), autoincrement=False, nullable=True))
    # ### end Alembic commands ###