-- Create a new table if it doesn't exist with the attributes id and name.
-- The id attribute should be unique for every entry and default to a value of 1
CREATE TABLE IF NOT EXISTS unique_id (
	id INT UNIQUE DEFAULT 1,
	name VARCHAR(256)
	);
