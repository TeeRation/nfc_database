PRAGMA foreign_keys = ON;

INSERT INTO task (
    id,
    title,
    description,

    work_type_id,
    employee_id,
    location_id,
    device_id,

    planned_date,
    status,
    priority,

    is_active
)
VALUES
(
    'TASK-001',
    'Проверить пожарный шкаф',
    'Плановая проверка пожарного шкафа №1',

    'WORK-001',
    'EMP-001',
    'LOC-001',
    'DEV-001',

    '2026-07-21',
    'planned',
    'high',

    1
),

(
    'TASK-002',
    'Осмотр серверной',
    'Плановый осмотр серверного помещения',

    'WORK-002',
    'EMP-002',
    'LOC-002',
    NULL,

    '2026-07-22',
    'in_progress',
    'medium',

    1
),

(
    'TASK-003',
    'Инвентаризация ноутбука',
    'Проверка наличия оборудования',

    'WORK-003',
    'EMP-003',
    'LOC-003',
    'DEV-003',

    '2026-07-25',
    'planned',
    'low',

    1
);