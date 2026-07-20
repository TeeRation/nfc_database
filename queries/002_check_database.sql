SELECT 'nfc_manufacturer' AS table_name, COUNT(*) AS records
FROM nfc_manufacturer

UNION ALL

SELECT 'nfc_tag', COUNT(*)
FROM nfc_tag

UNION ALL

SELECT 'work_type', COUNT(*)
FROM work_type

UNION ALL

SELECT 'employee', COUNT(*)
FROM employee

UNION ALL

SELECT 'location', COUNT(*)
FROM location

UNION ALL

SELECT 'device', COUNT(*)
FROM device

UNION ALL

SELECT 'task', COUNT(*)
FROM task;