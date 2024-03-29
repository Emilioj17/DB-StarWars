"""empty message

Revision ID: c1f0e22f0cf9
Revises: 
Create Date: 2021-07-01 12:56:01.328518

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c1f0e22f0cf9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('personas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.Column('altura', sa.String(length=100), nullable=False),
    sa.Column('masa', sa.String(length=100), nullable=False),
    sa.Column('descripcion', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nombre')
    )
    op.create_table('planetas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.Column('diametro', sa.String(length=100), nullable=False),
    sa.Column('poblacion', sa.String(length=100), nullable=False),
    sa.Column('descripcion', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nombre')
    )
    op.create_table('usuarios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('correo', sa.String(length=100), nullable=False),
    sa.Column('clave', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('correo')
    )
    op.create_table('personajes_favoritos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('usuario_id', sa.Integer(), nullable=False),
    sa.Column('personaje_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['personaje_id'], ['personas.id'], ),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuarios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('plentas_favoritos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('usuario_id', sa.Integer(), nullable=False),
    sa.Column('planeta_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['planeta_id'], ['planetas.id'], ),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuarios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('plentas_favoritos')
    op.drop_table('personajes_favoritos')
    op.drop_table('usuarios')
    op.drop_table('planetas')
    op.drop_table('personas')
    # ### end Alembic commands ###
