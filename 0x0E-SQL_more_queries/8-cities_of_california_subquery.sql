-- list all the cities of California that can be found in the hbtn_0d_usa db.
-- Display all cities in California from the states and cities tables
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
	