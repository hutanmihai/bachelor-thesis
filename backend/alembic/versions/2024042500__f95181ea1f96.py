"""empty message

Revision ID: f95181ea1f96
Revises:
Create Date: 2024-04-25 02:00:10.511859

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "f95181ea1f96"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("username", sa.VARCHAR(length=255), nullable=False),
        sa.Column("email", sa.VARCHAR(length=255), nullable=False),
        sa.Column("password", sa.VARCHAR(length=255), nullable=False),
        sa.Column("predictions", sa.INTEGER(), server_default="3", nullable=False),
        sa.Column("created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    op.create_table(
        "entry",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("user_id", sa.UUID(), nullable=False),
        sa.Column("manufacturer", sa.VARCHAR(length=255), nullable=False),
        sa.Column("model", sa.VARCHAR(length=255), nullable=False),
        sa.Column("fuel", sa.VARCHAR(length=255), nullable=False),
        sa.Column("chassis", sa.VARCHAR(length=255), nullable=False),
        sa.Column("sold_by", sa.VARCHAR(length=255), nullable=False),
        sa.Column("gearbox", sa.VARCHAR(length=255), nullable=False),
        sa.Column("km", sa.INTEGER(), nullable=False),
        sa.Column("power", sa.INTEGER(), nullable=False),
        sa.Column("engine", sa.INTEGER(), nullable=False),
        sa.Column("year", sa.INTEGER(), nullable=False),
        sa.Column("description", sa.TEXT(), nullable=False),
        sa.Column("image_url", sa.VARCHAR(length=255), nullable=False),
        sa.Column("prediction", sa.INTEGER(), nullable=False),
        sa.Column("created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("entry")
    op.drop_table("user")
    # ### end Alembic commands ###