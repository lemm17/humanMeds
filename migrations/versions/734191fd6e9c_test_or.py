"""test 'or'

Revision ID: 734191fd6e9c
Revises: 4c7140d02124
Create Date: 2019-12-06 00:06:23.417694

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '734191fd6e9c'
down_revision = '4c7140d02124'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('association_messages_id_sender_fkey', 'association_messages', type_='foreignkey')
    op.drop_column('association_messages', 'id_sender')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('association_messages', sa.Column('id_sender', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('association_messages_id_sender_fkey', 'association_messages', 'user', ['id_sender'], ['id'])
    # ### end Alembic commands ###
