-- List all the cities in the database by using the JOIN clause
SELECT cities.id, cities.name, states.name
FROM cities INNER JOIN states
ON cities.state_id = states.id;
