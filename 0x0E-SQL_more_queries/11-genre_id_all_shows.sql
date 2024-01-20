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
S_ELEC_T 
	title, genre_id
F_RO_M 
	tv_shows
L_EF_T JOIN
	tv_show_genres ON tv_shows.id = tv_show_genres.show_id
O_RDE_R BY
	title ASC, genre_id ASC;
 */
 