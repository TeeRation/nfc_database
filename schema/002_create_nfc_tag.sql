PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS nfc_tag (
    id TEXT PRIMARY KEY,
    entity_id TEXT NOT NULL,
    entity_type TEXT NOT NULL
        CHECK (
            entity_type IN (
                'location',
                'device',
                'employee',
                'work_type'
            )
        ),
    manufacturer_id TEXT,
    is_active INTEGER NOT NULL DEFAULT 1
        CHECK (is_active IN (0, 1)),

    FOREIGN KEY (manufacturer_id)
        REFERENCES nfc_manufacturer(id)
);