from app.models import Employee, Location, Task, WorkType





def test_start_tasks_success(client, planned_task):
    response = client.post(
        "/api/tasks/start",
        json={
            "location_id": "location-test-1",
            "employee_id": "employee-test",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["started_tasks_count"] == 1
    assert data["tasks"][0]["id"] == "task-test-1"
    assert data["tasks"][0]["status"] == "in_progress"


def test_start_tasks_second_time_returns_zero(client, planned_task):
    first_response = client.post(
        "/api/tasks/start",
        json={
            "location_id": "location-test-1",
            "employee_id": "employee-test",
        },
    )

    assert first_response.status_code == 200

    second_response = client.post(
        "/api/tasks/start",
        json={
            "location_id": "location-test-1",
            "employee_id": "employee-test",
        },
    )

    assert second_response.status_code == 200
    assert second_response.json()["started_tasks_count"] == 0


def test_get_task_status(client, in_progress_task):
    response = client.get(
        "/api/tasks/task-test-1/status"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["task_id"] == "task-test-1"
    assert data["status"] == "in_progress"
    assert data["is_active"] == 1


def test_close_task_success(client, in_progress_task):
    response = client.post(
        "/api/tasks/task-test-1/close",
        json={
            "employee_id": "employee-test",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == "task-test-1"
    assert data["status"] == "done"
    assert data["closed_by_employee_id"] == "employee-test"
    assert data["closed_at"] is not None


def test_close_task_second_time_returns_400(
    client,
    in_progress_task,
):
    first_response = client.post(
        "/api/tasks/task-test-1/close",
        json={
            "employee_id": "employee-test",
        },
    )

    assert first_response.status_code == 200

    second_response = client.post(
        "/api/tasks/task-test-1/close",
        json={
            "employee_id": "employee-test",
        },
    )

    assert second_response.status_code == 400

    assert second_response.json() == {
        "detail": "Закрыть можно только задачу в статусе in_progress."
    }


def test_close_task_unknown_employee_returns_404(
    client,
    in_progress_task,
):
    response = client.post(
        "/api/tasks/task-test-1/close",
        json={
            "employee_id": "employee-999",
        },
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Сотрудник не найден."
    }


def test_get_unknown_task_status_returns_404(client):
    response = client.get(
        "/api/tasks/task-999/status"
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Задача не найдена."
    }