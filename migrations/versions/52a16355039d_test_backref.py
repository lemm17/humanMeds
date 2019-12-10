"""test backref

Revision ID: 52a16355039d
Revises: 734191fd6e9c
Create Date: 2019-12-09 15:12:48.380341

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52a16355039d'
down_revision = '734191fd6e9c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('dialog', sa.Column('user_first', sa.Integer(), nullable=False))
    op.add_column('dialog', sa.Column('user_second', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'dialog', 'user', ['user_second'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'dialog', 'user', ['user_first'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'dialog', type_='foreignkey')
    op.drop_constraint(None, 'dialog', type_='foreignkey')
    op.drop_column('dialog', 'user_second')
    op.drop_column('dialog', 'user_first')
    # ### end Alembic commands ###