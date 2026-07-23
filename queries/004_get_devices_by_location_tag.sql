SELECT
    nt.id AS nfc_tag_id,
    l.id AS location_id,
    l.name AS location_name,
    l.description AS location_description,
    d.id AS device_id,
    d.name AS device_name,
    d.inventory_number,
    CASE
    WHEN d.is_active = 1 THEN 'Активно'
    ELSE 'Неактивно'
END AS device_status
FROM nfc_tag AS nt
INNER JOIN location AS l
    ON l.nfc_tag_id = nt.id
INNER JOIN device AS d
    ON d.location_id = l.id
WHERE nt.id = :nfc_tag_id
  AND nt.is_active = 1
  AND l.is_active = 1
  AND d.is_active = 1
ORDER BY
    d.name,
    d.inventory_number;