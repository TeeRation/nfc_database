from pydantic import BaseModel


class LocationResolveRequest(BaseModel):
    tag_id: str


class LocationData(BaseModel):
    id: str
    name: str
    description: str | None
    is_active: int


class LocationResolveResponse(BaseModel):
    tag_id: str
    entity_type: str
    location: LocationData

class TaskStartRequest(BaseModel):
    location_id: str
    employee_id: str


class StartedTaskData(BaseModel):
    id: str
    title: str
    status: str
    priority: str


class TaskStartResponse(BaseModel):
    location_id: str
    employee_id: str
    started_tasks_count: int
    tasks: list[StartedTaskData]