-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
-- uses a databse to lists all rows in a table corresponding to all rows in another
-- tv_shows table contains only one record where title = Dexter
SELECT 
	genres.name AS name
FROM
tv_shows AS shows
INNER JOIN
	tv_show_genres AS show_genres ON shows.id = show_genres.show_id
INNER JOIN
	tv_genres AS genres ON genres.id = show_genres.genre_id
WHERE
	shows.title = "Dexter"
ORDER BY name ASC;
