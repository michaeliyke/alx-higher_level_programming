-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT 
	genres.name AS name, shows.title AS title
FROM
tv_shows AS shows
INNER JOIN
	tv_show_genres AS show_genres ON shows.id = show_genres.show_id
INNER JOIN
	tv_genres AS genres
WHERE
	shows.title = "Dexter"
ORDER BY name ASC;
