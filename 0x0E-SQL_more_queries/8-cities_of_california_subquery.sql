-- subquery
-- subquery
SELECT cities.id, name 
FROM cities 
WHERE state_id = (SELECT id FROM states where name = "California") ORDER BY cities.id ASC;
