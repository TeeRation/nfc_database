SELECT
    COUNT(*) AS closed_tasks_count
FROM task
WHERE status = 'done'
  AND DATE(closed_at) = DATE('now', 'localtime');