"""rename address

Revision ID: 11339945f330
Revises: 6b6885a74cd5
Create Date: 2024-06-26 10:43:54.966912

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11339945f330'
down_revision = '6b6885a74cd5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'address',  new_column_name='location')
    # ### end Alembic commands ###

    
def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
   op.alter_column('departments', 'location',  new_column_name='address')
    # ### end Alembic commands ###
