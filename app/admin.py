from sqladmin import Admin, ModelView

from app.database import engine
from app.models import (
    Device,
    Employee,
    Location,
    NfcManufacturer,
    NfcTag,
    Task,
    WorkType,
)


class NfcManufacturerAdmin(ModelView, model=NfcManufacturer):
    name = "Производитель NFC-меток"
    name_plural = "Производители NFC-меток"

    column_list = [
        NfcManufacturer.id,
        NfcManufacturer.name,
        NfcManufacturer.description,
        NfcManufacturer.is_active,
    ]


class NfcTagAdmin(ModelView, model=NfcTag):
    name = "NFC-метка"
    name_plural = "NFC-метки"

    column_list = [
        NfcTag.id,
        NfcTag.entity_id,
        NfcTag.entity_type,
        NfcTag.manufacturer_id,
        NfcTag.is_active,
    ]


class WorkTypeAdmin(ModelView, model=WorkType):
    name = "Вид работы"
    name_plural = "Виды работ"

    column_list = [
        WorkType.id,
        WorkType.name,
        WorkType.code,
        WorkType.description,
        WorkType.nfc_tag_id,
        WorkType.is_active,
    ]


class EmployeeAdmin(ModelView, model=Employee):
    name = "Сотрудник"
    name_plural = "Сотрудники"

    column_list = [
        Employee.id,
        Employee.full_name,
        Employee.personal_number,
        Employee.position,
        Employee.nfc_tag_id,
        Employee.is_active,
    ]


class LocationAdmin(ModelView, model=Location):
    name = "Локация"
    name_plural = "Локации"

    column_list = [
        Location.id,
        Location.name,
        Location.description,
        Location.nfc_tag_id,
        Location.is_active,
    ]


class DeviceAdmin(ModelView, model=Device):
    name = "Устройство"
    name_plural = "Устройства"

    column_list = [
        Device.id,
        Device.name,
        Device.inventory_number,
        Device.location_id,
        Device.nfc_tag_id,
        Device.is_active,
    ]


class TaskAdmin(ModelView, model=Task):
    name = "Задача"
    name_plural = "Задачи"

    column_list = [
        Task.id,
        Task.title,
        Task.work_type_id,
        Task.employee_id,
        Task.location_id,
        Task.device_id,
        Task.planned_date,
        Task.status,
        Task.priority,
        Task.closed_by_employee_id,
        Task.closed_at,
        Task.is_active,
    ]


def setup_admin(app) -> Admin:
    admin = Admin(
        app=app,
        engine=engine,
        title="NFC Database Admin",
    )

    admin.add_view(NfcManufacturerAdmin)
    admin.add_view(NfcTagAdmin)
    admin.add_view(WorkTypeAdmin)
    admin.add_view(EmployeeAdmin)
    admin.add_view(LocationAdmin)
    admin.add_view(DeviceAdmin)
    admin.add_view(TaskAdmin)

    return admin