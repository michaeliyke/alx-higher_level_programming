-- imported dump.sql for below task
-- lists all shows contained in the database hbtn_0d_tvshows
SELECT 
	-- COALESCE returns the first non-NULL of all
	-- its arguments. Used for setting default value
	title, COALESCE(genre_id, NULL) AS genre_id
FROM 
	tv_shows
LEFT JOIN
	tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY
	title ASC, genre_id ASC;

/* FOR THE RECORD: BELOW CODE ACHIEVS SAME
SELECT 
	title, genre_id
FROM 
	tv_shows
LEFT JOIN
	tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY
	title ASC, genre_id ASC;
 */