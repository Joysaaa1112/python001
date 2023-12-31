"""empty message

Revision ID: 9a0a1a44b283
Revises: e169d0ccda07
Create Date: 2023-07-10 18:27:25.013711

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a0a1a44b283'
down_revision = 'e169d0ccda07'
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
