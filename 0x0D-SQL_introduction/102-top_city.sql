-- average temperature in agust and july only top 3
-- average temperature in agust and july only top 3
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month = 7 or month = 8 GROuP BY city ORDER BY avg_temp DESC LIMIT 3;
