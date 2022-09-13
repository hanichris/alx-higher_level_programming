-- Create a new database and table if their don't exist.
-- The table has two attributes: id and name.
-- The id attribute should be an integer, unique, auto-generated, a primary key for
-- the table and it can't be null.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
	id INT UNIQUE NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id)
	);
