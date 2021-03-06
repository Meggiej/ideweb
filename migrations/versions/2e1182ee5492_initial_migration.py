"""Initial Migration

Revision ID: 2e1182ee5492
Revises: None
Create Date: 2016-02-12 01:39:48.871140

"""

# revision identifiers, used by Alembic.
revision = '2e1182ee5492'
down_revision = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cde_job',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('job_id', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('text', sa.String(), nullable=True),
    sa.Column('file', sa.String(), nullable=True),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('result', postgresql.JSONB(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cde_job')
    ### end Alembic commands ###
