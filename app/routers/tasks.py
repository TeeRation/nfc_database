from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Employee, Location, Task
from app.schemas import (
    StartedTaskData,
    TaskStartRequest,
    TaskStartResponse,
)


router = APIRouter(
    prefix="/api/tasks",
    tags=["Tasks"],
)


@router.post(
    "/start",
    response_model=TaskStartResponse,
)
def start_tasks(
    request: TaskStartRequest,
    db: Session = Depends(get_db),
) -> TaskStartResponse:
    location = db.get(Location, request.location_id)

    if location is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Местоположение не найдено.",
        )

    if location.is_active != 1:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Местоположение неактивно.",
        )

    employee = db.get(Employee, request.employee_id)

    if employee is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Сотрудник не найден.",
        )

    if employee.is_active != 1:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Сотрудник неактивен.",
        )

    tasks = db.scalars(
        select(Task).where(
            Task.location_id == request.location_id,
            Task.employee_id == request.employee_id,
            Task.status == "planned",
            Task.is_active == 1,
        )
    ).all()

    for task in tasks:
        task.status = "in_progress"

    db.commit()

    return TaskStartResponse(
        location_id=request.location_id,
        employee_id=request.employee_id,
        started_tasks_count=len(tasks),
        tasks=[
            StartedTaskData(
                id=task.id,
                title=task.title,
                status=task.status,
                priority=task.priority,
            )
            for task in tasks
        ],
    )