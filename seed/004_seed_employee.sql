PRAGMA foreign_keys = ON;

INSERT INTO employee (
    id,
    full_name,
    personal_number,
    position,
    nfc_tag_id,
    is_active
)
VALUES
(
    'EMP-001',
    'Иванов Иван Иванович',
    '100001',
    'Инженер',
    'TAG-004',
    1
),
(
    'EMP-002',
    'Петров Петр Петрович',
    '100002',
    'Электромонтер',
    NULL,
    1
),
(
    'EMP-003',
    'Сидоров Сергей Сергеевич',
    '100003',
    'Мастер участка',
    NULL,
    1
);