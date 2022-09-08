-- List all records that don't contain a null value in the `name` column
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
