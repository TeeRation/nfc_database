PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS location (

    id TEXT PRIMARY KEY,

    name TEXT NOT NULL,
    description TEXT,

    nfc_tag_id TEXT,

    is_active INTEGER NOT NULL DEFAULT 1
        CHECK (is_active IN (0, 1)),

    FOREIGN KEY (nfc_tag_id)
        REFERENCES nfc_tag(id)

);