-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows
SELECT
	title
FROM
	tv_shows AS shows
LEFT JOIN
	tv_show_genres AS show_genres ON shows.id = show_genres.genre_id
WHERE
	show_genres.genre_id != (
		SELECT
			id
		FROM
			tv_genres AS genres
		WHERE genres.name = "Comedy"
	)
GROUP BY title
ORDER BY title ASC;
