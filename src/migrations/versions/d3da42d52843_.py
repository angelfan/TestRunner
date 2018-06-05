"""empty message
Revision ID: d3da42d52843
Revises: ef3d382f1d81
Create Date: 2018-05-24 16:45:08.812421
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3da42d52843'
down_revision = 'ef3d382f1d81'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('autotest_result', 'report_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('autotest_result', sa.Column('report_id', sa.BOOLEAN(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
