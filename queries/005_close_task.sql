PRAGMA foreign_keys = ON;

BEGIN TRANSACTION;

UPDATE task
SET
    status = 'done',
    closed_by_employee_id = :closed_by_employee_id,
    closed_at = DATETIME('now', 'localtime')
WHERE id = :task_id

COMMIT;

SELECT
    t.id AS task_id,
    t.title,
    t.status,

    assigned.id AS assigned_employee_id,
    assigned.full_name AS assigned_employee_name,

    closed_by.id AS closed_by_employee_id,
    closed_by.full_name AS closed_by_employee_name,

    t.closed_at
FROM task AS t
LEFT JOIN employee AS assigned
    ON assigned.id = t.employee_id
LEFT JOIN employee AS closed_by
    ON closed_by.id = t.closed_by_employee_id
WHERE t.id = :task_id;