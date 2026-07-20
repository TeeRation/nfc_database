PRAGMA foreign_keys = ON;

INSERT INTO location (
    id,
    name,
    description,
    nfc_tag_id,
    is_active
)
VALUES
(
    'LOC-001',
    'Склад №1',
    'Основной склад оборудования',
    'TAG-003',
    1
),
(
    'LOC-002',
    'Серверная',
    'Помещение серверного оборудования',
    NULL,
    1
),
(
    'LOC-003',
    'Кабинет инженеров',
    'Рабочее помещение инженерного отдела',
    NULL,
    1
);