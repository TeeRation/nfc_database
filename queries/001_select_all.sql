SELECT
    t.id,
    t.title,
    wt.name AS work_type,
    e.full_name AS employee,
    l.name AS location,
    d.name AS device,
    t.planned_date,
    t.status,
    t.priority,
    t.closed_at
FROM task t
LEFT JOIN work_type wt
    ON wt.id = t.work_type_id
LEFT JOIN employee e
    ON e.id = t.employee_id
LEFT JOIN location l
    ON l.id = t.location_id
LEFT JOIN device d
    ON d.id = t.device_id
ORDER BY
    t.planned_date,
    t.id;