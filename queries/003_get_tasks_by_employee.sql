SELECT
    t.id AS task_id,
    t.title,
    t.description,
    wt.name AS work_type,
    e.id AS employee_id,
    e.full_name AS employee_name,
    l.name AS location_name,
    d.name AS device_name,
    t.planned_date,
    t.status,
    t.priority
FROM task AS t
INNER JOIN employee AS e
    ON e.id = t.employee_id
INNER JOIN work_type AS wt
    ON wt.id = t.work_type_id
LEFT JOIN location AS l
    ON l.id = t.location_id
LEFT JOIN device AS d
    ON d.id = t.device_id
WHERE e.full_name = :employee_full_name
  AND DATE(t.planned_date) = DATE(:task_date)
  AND t.is_active = 1
ORDER BY
    CASE t.priority
        WHEN 'high' THEN 1
        WHEN 'medium' THEN 2
        WHEN 'low' THEN 3
        ELSE 4
    END,
    t.id;