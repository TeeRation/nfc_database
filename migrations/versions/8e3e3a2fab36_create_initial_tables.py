"""create initial tables

Revision ID: 8e3e3a2fab36
Revises:
Create Date: 2026-07-27 16:13:23.883828
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# Revision identifiers used by Alembic.
revision: str = "8e3e3a2fab36"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create the initial database schema."""

    op.create_table(
        "nfc_manufacturer",
        sa.Column(
            "id",
            sa.Text(),
            nullable=False,
        ),
        sa.Column(
            "name",
            sa.Text(),
            nullable=False,
        ),
        sa.Column(
            "description",
            sa.Text(),
            nullable=True,
        ),
        sa.Column(
            "is_active",
            sa.Integer(),
            nullable=False,
            server_default=sa.text("1"),
        ),
        sa.CheckConstraint(
            "is_active IN (0, 1)",
            name="check_nfc_manufacturer_is_active",
        ),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "nfc_tag",
        sa.Column(
            "id",
            sa.Text(),
            nullable=False,
        ),
        sa.Column(
            "entity_id",
            sa.Text(),
            nullable=False,
        ),
        sa.Column(
            "entity_type",
            sa.Text(),
            nullable=False,
        ),
        sa.Column(
            "manufacturer_id",
            sa.Text(),
            nullable=True,
        ),
        sa.Column(
            "is_active",
            sa.Integer(),
            nullable=False,
            server_default=sa.text("1"),
        ),
        sa.CheckConstraint(
            "entity_type IN "
            "('location', 'device', 'employee', 'work_type')",
            name="check_nfc_tag_entity_type",
        ),
        sa.CheckConstraint(
            "is_active IN (0, 1)",
            name="check_nfc_tag_is_active",
        ),
        sa.ForeignKeyConstraint(
            ["manufacturer_id"],
            ["nfc_manufacturer.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "employee",
        sa.Column(
            "id",
            sa.Text(),
            nullable=False,
        ),
        sa.Column(
            "full_name",
            sa.Text(),
            nullable=False,
        ),
        sa.Column(
            "personal_number",
            sa.Text(),
            nullable=False,
        ),
        sa.Column(
            "position",
            sa.Text(),
            nullable=True,
        ),
        sa.Column(
            "nfc_tag_id",
            sa.Text(),
            nullable=True,
        ),
        sa.Column(
            "is_active",
            sa.Integer(),
            nullable=False,
            server_default=sa.text("1"),
        ),
        sa.CheckConstraint(
            "is_active IN (0, 1)",
            name="check_employee_is_active",
        ),
        sa.ForeignKeyConstraint(
            ["nfc_tag_id"],
            ["nfc_tag.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("personal_number"),
    )

    op.create_table(
        "location",
        sa.Column(
            "id",
            sa.Text(),
            nullable=False,
        ),
        sa.Column(
            "name",
            sa.Text(),
            nullable=False,
        ),
        sa.Column(
            "description",
            sa.Text(),
            nullable=True,
        ),
        sa.Column(
            "nfc_tag_id",
            sa.Text(),
            nullable=True,
        ),
        sa.Column(
            "is_active",
            sa.Integer(),
            nullable=False,
            server_default=sa.text("1"),
        ),
        sa.CheckConstraint(
            "is_active IN (0, 1)",
            name="check_location_is_active",
        ),
        sa.ForeignKeyConstraint(
            ["nfc_tag_id"],
            ["nfc_tag.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "work_type",
        sa.Column(
            "id",
            sa.Text(),
            nullable=False,
        ),
        sa.Column(
            "name",
            sa.Text(),
            nullable=False,
        ),
        sa.Column(
            "code",
            sa.Text(),
            nullable=False,
        ),
        sa.Column(
            "description",
            sa.Text(),
            nullable=True,
        ),
        sa.Column(
            "nfc_tag_id",
            sa.Text(),
            nullable=True,
        ),
        sa.Column(
            "is_active",
            sa.Integer(),
            nullable=False,
            server_default=sa.text("1"),
        ),
        sa.CheckConstraint(
            "is_active IN (0, 1)",
            name="check_work_type_is_active",
        ),
        sa.ForeignKeyConstraint(
            ["nfc_tag_id"],
            ["nfc_tag.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("code"),
    )

    op.create_table(
        "device",
        sa.Column(
            "id",
            sa.Text(),
            nullable=False,
        ),
        sa.Column(
            "name",
            sa.Text(),
            nullable=False,
        ),
        sa.Column(
            "inventory_number",
            sa.Text(),
            nullable=False,
        ),
        sa.Column(
            "location_id",
            sa.Text(),
            nullable=True,
        ),
        sa.Column(
            "nfc_tag_id",
            sa.Text(),
            nullable=True,
        ),
        sa.Column(
            "is_active",
            sa.Integer(),
            nullable=False,
            server_default=sa.text("1"),
        ),
        sa.CheckConstraint(
            "is_active IN (0, 1)",
            name="check_device_is_active",
        ),
        sa.ForeignKeyConstraint(
            ["location_id"],
            ["location.id"],
        ),
        sa.ForeignKeyConstraint(
            ["nfc_tag_id"],
            ["nfc_tag.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("inventory_number"),
    )

    op.create_table(
        "task",
        sa.Column(
            "id",
            sa.Text(),
            nullable=False,
        ),
        sa.Column(
            "title",
            sa.Text(),
            nullable=False,
        ),
        sa.Column(
            "description",
            sa.Text(),
            nullable=True,
        ),
        sa.Column(
            "work_type_id",
            sa.Text(),
            nullable=False,
        ),
        sa.Column(
            "employee_id",
            sa.Text(),
            nullable=False,
        ),
        sa.Column(
            "location_id",
            sa.Text(),
            nullable=False,
        ),
        sa.Column(
            "device_id",
            sa.Text(),
            nullable=True,
        ),
        sa.Column(
            "planned_date",
            sa.Text(),
            nullable=True,
        ),
        sa.Column(
            "status",
            sa.Text(),
            nullable=False,
            server_default=sa.text("'planned'"),
        ),
        sa.Column(
            "priority",
            sa.Text(),
            nullable=False,
            server_default=sa.text("'medium'"),
        ),
        sa.Column(
            "closed_by_employee_id",
            sa.Text(),
            nullable=True,
        ),
        sa.Column(
            "closed_at",
            sa.DateTime(),
            nullable=True,
        ),
        sa.Column(
            "is_active",
            sa.Integer(),
            nullable=False,
            server_default=sa.text("1"),
        ),
        sa.CheckConstraint(
            "priority IN ('low', 'medium', 'high')",
            name="check_task_priority",
        ),
        sa.CheckConstraint(
            "status IN "
            "('planned', 'in_progress', 'done', 'cancelled')",
            name="check_task_status",
        ),
        sa.CheckConstraint(
            "is_active IN (0, 1)",
            name="check_task_is_active",
        ),
        sa.ForeignKeyConstraint(
            ["closed_by_employee_id"],
            ["employee.id"],
        ),
        sa.ForeignKeyConstraint(
            ["device_id"],
            ["device.id"],
        ),
        sa.ForeignKeyConstraint(
            ["employee_id"],
            ["employee.id"],
        ),
        sa.ForeignKeyConstraint(
            ["location_id"],
            ["location.id"],
        ),
        sa.ForeignKeyConstraint(
            ["work_type_id"],
            ["work_type.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    """Delete the initial database schema."""

    op.drop_table("task")
    op.drop_table("device")
    op.drop_table("work_type")
    op.drop_table("location")
    op.drop_table("employee")
    op.drop_table("nfc_tag")
    op.drop_table("nfc_manufacturer")