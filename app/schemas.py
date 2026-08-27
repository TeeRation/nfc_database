from datetime import datetime

from pydantic import BaseModel, Field


class LocationResolveRequest(BaseModel):
    tag_id: str = Field(
        description="Идентификатор считанной NFC-метки",
        examples=["tag-1"],
    )


class LocationData(BaseModel):
    id: str = Field(
        description="Идентификатор местоположения",
        examples=["location-1"],
    )
    name: str = Field(
        description="Название местоположения",
        examples=["Кладовая 546"],
    )
    description: str | None = Field(
        description="Описание местоположения",
        examples=["Основная тестовая кладовая"],
    )
    is_active: int = Field(
        description="Признак активности местоположения: 1 — активно, 0 — неактивно",
        examples=[1],
    )


class LocationResolveResponse(BaseModel):
    tag_id: str = Field(
        description="Идентификатор распознанной NFC-метки",
        examples=["tag-1"],
    )
    entity_type: str = Field(
        description="Тип объекта, к которому привязана NFC-метка",
        examples=["location"],
    )
    location: LocationData


class TaskStartRequest(BaseModel):
    location_id: str = Field(
        description="Идентификатор текущего местоположения",
        examples=["location-1"],
    )
    employee_id: str = Field(
        description="Идентификатор сотрудника",
        examples=["employee-1"],
    )


class StartedTaskData(BaseModel):
    id: str = Field(
        description="Идентификатор задачи",
        examples=["task-1"],
    )
    title: str = Field(
        description="Название задачи",
        examples=["Проверить состояние шкафа"],
    )
    status: str = Field(
        description="Текущий статус задачи",
        examples=["in_progress"],
    )
    priority: str = Field(
        description="Приоритет задачи",
        examples=["medium"],
    )


class TaskStartResponse(BaseModel):
    location_id: str = Field(
        description="Идентификатор местоположения",
        examples=["location-1"],
    )
    employee_id: str = Field(
        description="Идентификатор сотрудника",
        examples=["employee-1"],
    )
    started_tasks_count: int = Field(
        description="Количество задач, переведённых в работу",
        examples=[1],
    )
    tasks: list[StartedTaskData] = Field(
        description="Список задач, переведённых в статус in_progress",
    )


class TaskCloseRequest(BaseModel):
    employee_id: str = Field(
        description="Идентификатор сотрудника, закрывающего задачу",
        examples=["employee-1"],
    )


class TaskCloseResponse(BaseModel):
    id: str = Field(
        description="Идентификатор закрытой задачи",
        examples=["task-1"],
    )
    title: str = Field(
        description="Название закрытой задачи",
        examples=["Проверить состояние шкафа"],
    )
    status: str = Field(
        description="Итоговый статус задачи",
        examples=["done"],
    )
    closed_by_employee_id: str = Field(
        description="Идентификатор сотрудника, закрывшего задачу",
        examples=["employee-1"],
    )
    closed_at: datetime = Field(
        description="Дата и время закрытия задачи",
    )


class TaskStatusResponse(BaseModel):
    task_id: str = Field(
        description="Идентификатор задачи",
        examples=["task-1"],
    )
    status: str = Field(
        description="Текущий статус задачи",
        examples=["in_progress"],
    )
    is_active: int = Field(
        description="Признак активности задачи: 1 — активна, 0 — неактивна",
        examples=[1],
    )