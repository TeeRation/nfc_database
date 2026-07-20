PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS device (

    id TEXT PRIMARY KEY,

    name TEXT NOT NULL,
    inventory_number TEXT NOT NULL UNIQUE,

    location_id TEXT NOT NULL,
    nfc_tag_id TEXT,

    is_active INTEGER NOT NULL DEFAULT 1
        CHECK (is_active IN (0, 1)),

    FOREIGN KEY (location_id)
        REFERENCES location(id),

    FOREIGN KEY (nfc_tag_id)
        REFERENCES nfc_tag(id)

);