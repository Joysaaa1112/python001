"""empty message

Revision ID: e169d0ccda07
Revises: ead4efb1ac79
Create Date: 2023-07-10 18:26:39.383658

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e169d0ccda07'
down_revision = 'ead4efb1ac79'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=100), nullable=False, comment='用户名'),
    sa.Column('password', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('avatar', sa.String(length=100), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###