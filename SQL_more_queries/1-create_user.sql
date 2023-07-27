-- Script that creates the MySQL server user user_0d_1

--CREATING USER
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- GRANTING PRIVILEGES
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- APPLYING CHANGES INMEDIATELY
FLUSH PRIVILEGES;
