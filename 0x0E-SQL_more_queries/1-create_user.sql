-- Create a new user on the MySQL server.
-- The created user has all the privileges on the server.
-- The created user's password is set to `user_0d_1_pwd`
-- If the user already exists, the script doesn't fail.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
