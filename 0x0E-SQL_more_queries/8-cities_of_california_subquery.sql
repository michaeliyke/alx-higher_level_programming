-- list all the cities of California that can be found in the hbtn_0d_usa db.
-- use the right db
USE `hbtn_0d_usa`;

-- Display all cities in California
SELECT
	id,
	name
FROM
	`cities`
WHERE
	state_id = (
		SELECT
			id AS state_id
		FROM
			`states`
		WHERE
			name = 'California'
	)
ORDER BY
	id ASC;
	