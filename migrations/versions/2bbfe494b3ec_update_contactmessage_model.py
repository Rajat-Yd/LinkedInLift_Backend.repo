"""Update ContactMessage model

Revision ID: 2bbfe494b3ec
Revises: 0d823ee81874
Create Date: 2024-11-27 16:55:01.316091

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2bbfe494b3ec'
down_revision = '0d823ee81874'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contact_message', schema=None) as batch_op:
        batch_op.alter_column('phone',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=15),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contact_message', schema=None) as batch_op:
        batch_op.alter_column('phone',
               existing_type=sa.String(length=15),
               type_=sa.INTEGER(),
               existing_nullable=False)

    # ### end Alembic commands ###
