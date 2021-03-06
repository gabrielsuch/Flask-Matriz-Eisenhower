"""alteração da tabela tasks_categories

Revision ID: c4a1fb244efc
Revises: 4c5846fc9824
Create Date: 2022-04-14 21:08:07.175023

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c4a1fb244efc'
down_revision = '4c5846fc9824'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tasks_categories_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('task_id', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
    sa.ForeignKeyConstraint(['task_id'], ['tasks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('tasks_categories')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tasks_categories',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('task_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('category_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], name='tasks_categories_category_id_fkey'),
    sa.ForeignKeyConstraint(['task_id'], ['tasks.id'], name='tasks_categories_task_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='tasks_categories_pkey')
    )
    op.drop_table('tasks_categories_table')
    # ### end Alembic commands ###
