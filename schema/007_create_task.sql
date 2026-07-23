PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS task (

    id TEXT PRIMARY KEY,

    title TEXT NOT NULL,
    description TEXT,

    work_type_id TEXT NOT NULL,
    employee_id TEXT,
    location_id TEXT,
    device_id TEXT,
    closed_by_employee_id TEXT,

    planned_date TEXT,
    status TEXT NOT NULL,
    priority TEXT NOT NULL,
    closed_at TEXT,

    is_active INTEGER NOT NULL DEFAULT 1
        CHECK (is_active IN (0, 1)),

    CHECK (
        status IN (
            'planned',
            'in_progress',
            'done',
            'cancelled'
        )
    ),

    CHECK (
        priority IN (
            'low',
            'medium',
            'high'
        )
    ),

    FOREIGN KEY (work_type_id)
        REFERENCES work_type(id),

    FOREIGN KEY (employee_id)
        REFERENCES employee(id),

    FOREIGN KEY (location_id)
        REFERENCES location(id),

    FOREIGN KEY (device_id)
    REFERENCES device(id),

FOREIGN KEY (closed_by_employee_id)
    REFERENCES employee(id)

);