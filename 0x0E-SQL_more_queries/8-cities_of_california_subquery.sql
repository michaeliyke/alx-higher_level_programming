-- list all the cities of California that can be found in the hbtn_0d_usa db.
-- use the right db
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
