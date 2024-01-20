-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT 
	shows.title AS title,
	genres.name AS name
FROM
tv_shows AS shows
LEFT JOIN
	tv_show_genres AS show_genres ON shows.id = show_genres.show_id
LEFT JOIN
	tv_genres AS genres ON genres.id = show_genres.genre_id
ORDER BY
	title ASC, name ASC;
