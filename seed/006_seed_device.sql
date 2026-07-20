PRAGMA foreign_keys = ON;

INSERT INTO device (
    id,
    name,
    inventory_number,
    location_id,
    nfc_tag_id,
    is_active
)
VALUES
(
    'DEV-001',
    'Пожарный шкаф №1',
    'INV-100001',
    'LOC-001',
    'TAG-005',
    1
),
(
    'DEV-002',
    'Коммутатор Cisco',
    'INV-100002',
    'LOC-002',
    NULL,
    1
),
(
    'DEV-003',
    'Ноутбук инженера',
    'INV-100003',
    'LOC-003',
    NULL,
    1
);