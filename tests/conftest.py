import os

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base, get_db
from app.main import app
from app.models import (
    Employee,
    Location,
    NfcManufacturer,
    NfcTag,
    Task,
    WorkType,
)

TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL")

if TEST_DATABASE_URL is None:
    raise RuntimeError(
        "TEST_DATABASE_URL не найдена. "
        "Проверьте файл .env."
    )


test_engine = create_engine(
    TEST_DATABASE_URL,
    pool_pre_ping=True,
)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=test_engine,
)


@pytest.fixture(autouse=True)
def prepare_test_database():
    Base.metadata.drop_all(bind=test_engine)
    Base.metadata.create_all(bind=test_engine)

    yield

    Base.metadata.drop_all(bind=test_engine)


@pytest.fixture
def db():
    session = TestingSessionLocal()

    try:
        yield session
    finally:
        session.close()


@pytest.fixture
def client():
    def override_get_db():
        session = TestingSessionLocal()

        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()

@pytest.fixture
def manufacturer(db):
    manufacturer = NfcManufacturer(
        id="manufacturer-test",
        name="Тестовый производитель",
        description=None,
        is_active=1,
    )

    db.add(manufacturer)
    db.commit()

    return manufacturer


@pytest.fixture
def location_tag(db, manufacturer):
    tag = NfcTag(
        id="tag-test-1",
        entity_id="location-test-1",
        entity_type="location",
        manufacturer_id=manufacturer.id,
        is_active=1,
    )

    db.add(tag)
    db.commit()

    return tag


@pytest.fixture
def reserved_tag(db, manufacturer):
    tag = NfcTag(
        id="tag-test-2",
        entity_id=None,
        entity_type=None,
        manufacturer_id=manufacturer.id,
        is_active=1,
    )

    db.add(tag)
    db.commit()

    return tag


@pytest.fixture
def location(db, location_tag):
    location = Location(
        id="location-test-1",
        name="Тестовая локация",
        description="Локация для pytest",
        nfc_tag_id=location_tag.id,
        is_active=1,
    )

    db.add(location)
    db.commit()

    return location


@pytest.fixture
def employee(db):
    employee = Employee(
        id="employee-test",
        full_name="Тестовый сотрудник",
        personal_number="TEST-001",
        position="Техник",
        nfc_tag_id=None,
        is_active=1,
    )

    db.add(employee)
    db.commit()

    return employee


@pytest.fixture
def work_type(db):
    work_type = WorkType(
        id="work-type-test",
        name="Тестовая работа",
        code="TEST-WORK",
        description=None,
        nfc_tag_id=None,
        is_active=1,
    )

    db.add(work_type)
    db.commit()

    return work_type


@pytest.fixture
def task_dependencies(employee, location, work_type):
    return {
        "employee": employee,
        "location": location,
        "work_type": work_type,
    }


@pytest.fixture
def planned_task(db, task_dependencies):
    task = Task(
        id="task-test-1",
        title="Тестовая задача",
        description=None,
        work_type_id=task_dependencies["work_type"].id,
        employee_id=task_dependencies["employee"].id,
        location_id=task_dependencies["location"].id,
        device_id=None,
        planned_date=None,
        status="planned",
        priority="medium",
        closed_by_employee_id=None,
        closed_at=None,
        is_active=1,
    )

    db.add(task)
    db.commit()

    return task

@pytest.fixture
def in_progress_task(db, task_dependencies):
    task = Task(
        id="task-test-1",
        title="Тестовая задача",
        description=None,
        work_type_id=task_dependencies["work_type"].id,
        employee_id=task_dependencies["employee"].id,
        location_id=task_dependencies["location"].id,
        device_id=None,
        planned_date=None,
        status="in_progress",
        priority="medium",
        closed_by_employee_id=None,
        closed_at=None,
        is_active=1,
    )

    db.add(task)
    db.commit()

    return task