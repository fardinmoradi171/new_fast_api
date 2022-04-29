"""add password

Revision ID: 980a52944f73
Revises: 7649fdcc2960
Create Date: 2022-04-22 23:58:44.974180

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '980a52944f73'
down_revision = '7649fdcc2960'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.String(length=50), nullable=True, min_length=8))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password')
    # ### end Alembic commands ###
