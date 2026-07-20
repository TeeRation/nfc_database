PRAGMA foreign_keys = ON;

INSERT INTO work_type (
    id,
    name,
    code,
    description,
    nfc_tag_id,
    is_active
)
VALUES
(
    'WORK-001',
    'Проверка пожарного шкафа',
    'FIRE_CHECK',
    'Плановая проверка состояния пожарного шкафа',
    'TAG-006',
    1
),
(
    'WORK-002',
    'Осмотр помещения',
    'ROOM_CHECK',
    'Периодический осмотр помещения',
    NULL,
    1
),
(
    'WORK-003',
    'Инвентаризация оборудования',
    'DEVICE_INVENTORY',
    'Проверка наличия оборудования',
    NULL,
    1
);