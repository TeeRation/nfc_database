PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS employee (

    id TEXT PRIMARY KEY,

    full_name TEXT NOT NULL,
    personal_number TEXT NOT NULL UNIQUE,
    position TEXT,

    nfc_tag_id TEXT,

    is_active INTEGER NOT NULL DEFAULT 1
        CHECK (is_active IN (0, 1)),

    FOREIGN KEY (nfc_tag_id)
        REFERENCES nfc_tag(id)

);
