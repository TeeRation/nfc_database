PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS nfc_manufacturer (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    is_active INTEGER NOT NULL DEFAULT 1
        CHECK (is_active IN (0, 1))
);