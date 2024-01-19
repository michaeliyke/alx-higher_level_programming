-- script that lists all the cities of California that can be found in 
-- the database hbtn_0d_usa.
-- use the right db
USE `hbtn_0d_usa`;

-- Display all cities in California
SELECT id, name
FROM `cities`
WHERE state_id = (
	SELECT id FROM `states` 
	WHERE name = "California"
	);