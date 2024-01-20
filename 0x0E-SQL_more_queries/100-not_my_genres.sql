-- uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
USE hbtn_0d_usa;
SELECT
	genres.name
FROM
	tv_genres AS genres
WHERE
	genres.name NOT IN (
		SELECT
			genres.name
		FROM
			tv_shows AS shows
		LEFT JOIN
			tv_show_genres AS show_genres ON shows.id = show_genres.show_id
		LEFT JOIN
			tv_genres AS genres ON genres.id = show_genres.genre_id
		WHERE
			shows.title = "Dexter"
	)
ORDER BY genres.name ASC;
