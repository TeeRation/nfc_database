from datetime import datetime

from sqlalchemy import select

from app.database import SessionLocal
from app.models import (
    Device,
    Employee,
    Location,
    NfcManufacturer,
    NfcTag,
    Task,
    WorkType,
)


def seed_database() -> None:
    db = SessionLocal()

    try:
        existing_manufacturer = db.scalar(
            select(NfcManufacturer).where(
                NfcManufacturer.id == "manufacturer-1"
            )
        )

        if existing_manufacturer is not None:
            print(
                "Seed marker manufacturer-1 already exists. "
                "Seeding skipped."
    )
            return

        manufacturer = NfcManufacturer(
            id="manufacturer-1",
            name="ООО Никитин",
            description="Производитель тестовых NFC-меток",
            is_active=1,
        )

        location_tag = NfcTag(
            id="tag-1",
            entity_id="location-1",
            entity_type="location",
            manufacturer_id="manufacturer-1",
            is_active=1,
        )

        reserve_tag_2 = NfcTag(
            id="tag-2",
            entity_id=None,
            entity_type=None,
            manufacturer_id="manufacturer-1",
            is_active=1,
        )

        reserve_tag_3 = NfcTag(
            id="tag-3",
            entity_id=None,
            entity_type=None,
            manufacturer_id="manufacturer-1",
            is_active=1,
        )

        location = Location(
            id="location-1",
            name="Кладовая 546",
            description="Основная тестовая кладовая",
            nfc_tag_id="tag-1",
            is_active=1,
        )

        employee = Employee(
            id="employee-1",
            full_name="Иванов Иван Иванович",
            personal_number="EMP-001",
            position="Техник",
            nfc_tag_id=None,
            is_active=1,
        )

        work_type = WorkType(
            id="work-type-1",
            name="Техническое обслуживание",
            code="MAINTENANCE",
            description="Плановые работы по обслуживанию оборудования",
            nfc_tag_id=None,
            is_active=1,
        )

        device = Device(
            id="device-1",
            name="Шкаф",
            inventory_number="DEV-001",
            location_id="location-1",
            nfc_tag_id=None,
            is_active=1,
        )

        task_planned = Task(
            id="task-1",
            title="Проверить состояние шкафа",
            description="Осмотреть шкаф и проверить его состояние",
            work_type_id="work-type-1",
            employee_id="employee-1",
            location_id="location-1",
            device_id="device-1",
            planned_date="2026-07-30",
            status="planned",
            priority="medium",
            closed_by_employee_id=None,
            closed_at=None,
            is_active=1,
        )

        task_in_progress = Task(
            id="task-2",
            title="Провести обслуживание оборудования",
            description="Выполнить плановое техническое обслуживание",
            work_type_id="work-type-1",
            employee_id="employee-1",
            location_id="location-1",
            device_id="device-1",
            planned_date="2026-07-30",
            status="in_progress",
            priority="high",
            closed_by_employee_id=None,
            closed_at=None,
            is_active=1,
        )

        task_done = Task(
            id="task-3",
            title="Проверить NFC-метку кладовой",
            description="Проверка чтения и состояния NFC-метки",
            work_type_id="work-type-1",
            employee_id="employee-1",
            location_id="location-1",
            device_id=None,
            planned_date="2026-07-30",
            status="done",
            priority="low",
            closed_by_employee_id="employee-1",
            closed_at=datetime.now(),
            is_active=1,
        )

        db.add(manufacturer)
        db.flush()

        db.add_all(
            [
                location_tag,
                reserve_tag_2,
                reserve_tag_3,
            ]
        )
        db.flush()

        db.add_all(
            [
                location,
                employee,
                work_type,
            ]
        )
        db.flush()

        db.add(device)
        db.flush()

        db.add_all(
            [
                task_planned,
                task_in_progress,
                task_done,
            ]
        )

        db.commit()
        print("Test data inserted successfully.")

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


if __name__ == "__main__":
    seed_database()