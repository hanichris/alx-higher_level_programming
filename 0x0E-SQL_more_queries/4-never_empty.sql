-- Create a new table if it doesn't exist with the attributes `id` and `name`.
-- The `id` attribute has a default value of 1.
CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT 1,
	name VARCHAR(256)
	);
