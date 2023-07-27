-- Script that creates the MySQL server user user_0d_1

-- creating user if not exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- grant all privilages
GRANT ALL PRIVILAGES ON *.* TO 'user_0d_1'@'localhost';
