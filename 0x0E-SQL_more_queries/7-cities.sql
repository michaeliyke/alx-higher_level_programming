-- script that creates the database hbtn_0d_usa and the table cities
-- (in the database hbtn_0d_usa) on your MySQL server.
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;

-- switch to the new db
USE `hbtn_0d_usa`;

-- cities tabl;e
CREATE TABLE IF NOT EXISTS `cities` (
	id INT AUTO_INCREMENT PRIMARY KEY,
	state_id INT,
	name VARCHAR(256) NOT NULL,
	UNIQUE(id),
	FOREIGN KEY (state_id) REFERENCES states(id)
);
