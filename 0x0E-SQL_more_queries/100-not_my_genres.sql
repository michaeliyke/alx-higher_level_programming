-- switch to the db
USE hbtn_0d_usa;

-- uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT
	name
FROM
	tv_genres
WHERE
	name NOT IN (
		SELECT
			name
		FROM
			tv_genres AS genres
		LEFT JOIN
			tv_show_genres AS show_genres ON genres.id = show_genres.genre_id
		LEFT JOIN
			tv_shows AS shows ON shows.id = show_genres.show_id
		WHERE
			shows.title = 'Dexter'
	)
GROUP BY name
ORDER BY name ASC;
