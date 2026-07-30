from sqlalchemy import (
    CheckConstraint,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    Text,
)

from app.database import Base


class NfcManufacturer(Base):
    __tablename__ = "nfc_manufacturer"

    id = Column(Text, primary_key=True)
    name = Column(Text, nullable=False)
    description = Column(Text, nullable=True)
    is_active = Column(Integer, nullable=False, default=1)

    __table_args__ = (
        CheckConstraint(
            "is_active IN (0, 1)",
            name="check_nfc_manufacturer_is_active",
        ),
    )


class NfcTag(Base):
    __tablename__ = "nfc_tag"

    id = Column(Text, primary_key=True)
    entity_id = Column(Text, nullable=True)
    entity_type = Column(Text, nullable=True)

    manufacturer_id = Column(
        Text,
        ForeignKey("nfc_manufacturer.id"),
        nullable=True,
    )

    is_active = Column(Integer, nullable=False, default=1)

    __table_args__ = (
        CheckConstraint(
            "(entity_type IS NULL AND entity_id IS NULL) OR "
            "(entity_type IN "
            "('location', 'device', 'employee', 'work_type') "
            "AND entity_id IS NOT NULL)",
            name="check_nfc_tag_entity_type",
        ),
        CheckConstraint(
            "is_active IN (0, 1)",
            name="check_nfc_tag_is_active",
        ),
    )


class WorkType(Base):
    __tablename__ = "work_type"

    id = Column(Text, primary_key=True)
    name = Column(Text, nullable=False)
    code = Column(Text, nullable=False, unique=True)
    description = Column(Text, nullable=True)

    nfc_tag_id = Column(
        Text,
        ForeignKey("nfc_tag.id"),
        nullable=True,
    )

    is_active = Column(Integer, nullable=False, default=1)

    __table_args__ = (
        CheckConstraint(
            "is_active IN (0, 1)",
            name="check_work_type_is_active",
        ),
    )


class Employee(Base):
    __tablename__ = "employee"

    id = Column(Text, primary_key=True)
    full_name = Column(Text, nullable=False)
    personal_number = Column(Text, nullable=False, unique=True)
    position = Column(Text, nullable=True)

    nfc_tag_id = Column(
        Text,
        ForeignKey("nfc_tag.id"),
        nullable=True,
    )

    is_active = Column(Integer, nullable=False, default=1)

    __table_args__ = (
        CheckConstraint(
            "is_active IN (0, 1)",
            name="check_employee_is_active",
        ),
    )


class Location(Base):
    __tablename__ = "location"

    id = Column(Text, primary_key=True)
    name = Column(Text, nullable=False)
    description = Column(Text, nullable=True)

    nfc_tag_id = Column(
        Text,
        ForeignKey("nfc_tag.id"),
        nullable=True,
    )

    is_active = Column(Integer, nullable=False, default=1)

    __table_args__ = (
        CheckConstraint(
            "is_active IN (0, 1)",
            name="check_location_is_active",
        ),
    )


class Device(Base):
    __tablename__ = "device"

    id = Column(Text, primary_key=True)
    name = Column(Text, nullable=False)
    inventory_number = Column(Text, nullable=False, unique=True)

    location_id = Column(
        Text,
        ForeignKey("location.id"),
        nullable=True,
    )

    nfc_tag_id = Column(
        Text,
        ForeignKey("nfc_tag.id"),
        nullable=True,
    )

    is_active = Column(Integer, nullable=False, default=1)

    __table_args__ = (
        CheckConstraint(
            "is_active IN (0, 1)",
            name="check_device_is_active",
        ),
    )


class Task(Base):
    __tablename__ = "task"

    id = Column(Text, primary_key=True)
    title = Column(Text, nullable=False)
    description = Column(Text, nullable=True)

    work_type_id = Column(
        Text,
        ForeignKey("work_type.id"),
        nullable=False,
    )

    employee_id = Column(
        Text,
        ForeignKey("employee.id"),
        nullable=False,
    )

    location_id = Column(
        Text,
        ForeignKey("location.id"),
        nullable=False,
    )

    device_id = Column(
        Text,
        ForeignKey("device.id"),
        nullable=True,
    )

    planned_date = Column(Text, nullable=True)
    status = Column(Text, nullable=False, default="planned")
    priority = Column(Text, nullable=False, default="medium")

    closed_by_employee_id = Column(
        Text,
        ForeignKey("employee.id"),
        nullable=True,
    )

    closed_at = Column(DateTime, nullable=True)
    is_active = Column(Integer, nullable=False, default=1)

    __table_args__ = (
        CheckConstraint(
            "status IN ('planned', 'in_progress', 'done', 'cancelled')",
            name="check_task_status",
        ),
        CheckConstraint(
            "priority IN ('low', 'medium', 'high')",
            name="check_task_priority",
        ),
        CheckConstraint(
            "is_active IN (0, 1)",
            name="check_task_is_active",
        ),
    )