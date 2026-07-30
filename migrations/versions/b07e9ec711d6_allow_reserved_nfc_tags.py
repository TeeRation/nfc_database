"""allow_reserved_nfc_tags

Revision ID: b07e9ec711d6
Revises: 8e3e3a2fab36
Create Date: 2026-07-30 14:08:25.211990
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "b07e9ec711d6"
down_revision: Union[str, Sequence[str], None] = "8e3e3a2fab36"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Allow NFC tags to remain unassigned and stored in reserve."""

    op.drop_constraint(
        "check_nfc_tag_entity_type",
        "nfc_tag",
        type_="check",
    )

    op.alter_column(
        "nfc_tag",
        "entity_id",
        existing_type=sa.Text(),
        nullable=True,
    )

    op.alter_column(
        "nfc_tag",
        "entity_type",
        existing_type=sa.Text(),
        nullable=True,
    )

    op.create_check_constraint(
        "check_nfc_tag_entity_type",
        "nfc_tag",
        """
        (
            entity_type IS NULL
            AND entity_id IS NULL
        )
        OR
        (
            entity_type IN (
                'location',
                'device',
                'employee',
                'work_type'
            )
            AND entity_id IS NOT NULL
        )
        """,
    )


def downgrade() -> None:
    """Restore the requirement that every NFC tag is assigned."""

    op.drop_constraint(
        "check_nfc_tag_entity_type",
        "nfc_tag",
        type_="check",
    )

    op.execute(
        """
        DELETE FROM nfc_tag
        WHERE entity_type IS NULL
           OR entity_id IS NULL
        """
    )

    op.alter_column(
        "nfc_tag",
        "entity_type",
        existing_type=sa.Text(),
        nullable=False,
    )

    op.alter_column(
        "nfc_tag",
        "entity_id",
        existing_type=sa.Text(),
        nullable=False,
    )

    op.create_check_constraint(
        "check_nfc_tag_entity_type",
        "nfc_tag",
        """
        entity_type IN (
            'location',
            'device',
            'employee',
            'work_type'
        )
        """,
    )