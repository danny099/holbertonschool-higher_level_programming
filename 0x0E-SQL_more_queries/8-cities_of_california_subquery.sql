-- create a subquery for a list cities by state
-- create a subquery for a list cities by state
SELECT cities.id, cities.name 
FROM cities 
WHERE state_id = (SELECT id FROM states WHERE name = "California") ORDER BY cities.id ASC;
