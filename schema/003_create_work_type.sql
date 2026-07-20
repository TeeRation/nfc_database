PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS work_type (
    id TEXT PRIMARY KEY,

    name TEXT NOT NULL,
    code TEXT NOT NULL UNIQUE,
    description TEXT,

    nfc_tag_id TEXT,

    is_active INTEGER NOT NULL DEFAULT 1
        CHECK (is_active IN (0, 1)),

    FOREIGN KEY (nfc_tag_id)
        REFERENCES nfc_tag(id)
);