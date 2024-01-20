-- lists all Comedy shows in the database hbtn_0d_tvshows
-- uses a databse to lists all rows in a table corresponding to all rows in another
-- The tv_genres table contains only one record where name = Comedy
SELECT 
	shows.title AS title
FROM
tv_shows AS shows
INNER JOIN
	tv_show_genres AS show_genres ON shows.id = show_genres.show_id
INNER JOIN
	tv_genres AS genres ON genres.id = show_genres.genre_id
WHERE
	genres.name = "Comedy"
ORDER BY title ASC;
