-- average temperature
-- average temperature
SELECT city, AVG(value) AS avg_temp FROM temperatures GROuP BY city ORDER BY avg_temp DESC;
