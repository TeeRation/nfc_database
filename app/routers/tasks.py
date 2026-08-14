from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session
from datetime import datetime

from app.database import get_db
from app.models import Employee, Location, Task
from app.schemas import (
    StartedTaskData,
    TaskCloseRequest,
    TaskCloseResponse,
    TaskStartRequest,
    TaskStartResponse,
    TaskStatusResponse,
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

@router.post(
    "/{task_id}/close",
    response_model=TaskCloseResponse,
)
def close_task(
    task_id: str,
    request: TaskCloseRequest,
    db: Session = Depends(get_db),
) -> TaskCloseResponse:
    task = db.get(Task, task_id)

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Задача не найдена.",
        )

    if task.is_active != 1:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Задача неактивна.",
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

    if task.employee_id != request.employee_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Задача назначена другому сотруднику.",
        )

    if task.status != "in_progress":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Закрыть можно только задачу в статусе in_progress.",
        )

    task.status = "done"
    task.closed_by_employee_id = request.employee_id
    task.closed_at = datetime.now()

    db.commit()
    db.refresh(task)

    return TaskCloseResponse(
        id=task.id,
        title=task.title,
        status=task.status,
        closed_by_employee_id=task.closed_by_employee_id,
        closed_at=task.closed_at,
    )

@router.get(
    "/{task_id}/status",
    response_model=TaskStatusResponse,
)
def get_task_status(
    task_id: str,
    db: Session = Depends(get_db),
) -> TaskStatusResponse:
    task = db.get(Task, task_id)

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Задача не найдена.",
        )

    return TaskStatusResponse(
        task_id=task.id,
        status=task.status,
        is_active=task.is_active,
    )