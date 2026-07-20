PRAGMA foreign_keys = ON;

INSERT INTO work_type (
    id,
    name,
    code,
    description,
    is_active
)
VALUES
(
    'WORK-001',
    'Проверка пожарного шкафа',
    'FIRE_CHECK',
    'Плановая проверка состояния пожарного шкафа',
    1
),
(
    'WORK-002',
    'Осмотр помещения',
    'ROOM_CHECK',
    'Периодический осмотр помещения',
    1
),
(
    'WORK-003',
    'Инвентаризация оборудования',
    'DEVICE_INVENTORY',
    'Проверка наличия оборудования',
    1
);