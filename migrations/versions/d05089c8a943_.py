"""empty message

Revision ID: d05089c8a943
Revises: 
Create Date: 2023-02-01 14:45:12.031618

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd05089c8a943'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurant', schema=None) as batch_op:
        batch_op.alter_column('item_rating',
               existing_type=sa.NUMERIC(precision=1, scale=1),
               type_=sa.DECIMAL(precision=6, scale=2),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurant', schema=None) as batch_op:
        batch_op.alter_column('item_rating',
               existing_type=sa.DECIMAL(precision=6, scale=2),
               type_=sa.NUMERIC(precision=1, scale=1),
               existing_nullable=True)

    # ### end Alembic commands ###
