-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- List all columns to be printed
SELECT genres.name AS genre,
	COUNT(shows.title) AS number_of_shows
FROM -- S_ELEC_Ts all of tv_shows for checking
	tv_shows AS shows
	INNER JOIN -- J_OI_Ns result with the tv_show_genres to obtain genre_id (a foreign key)
	tv_show_genres AS show_genres ON show_genres.show_id = shows.id
	INNER JOIN -- J_OI_Ns result with tv_genres using the newly obtined genre_id
	tv_genres AS genres ON genres.id = show_genres.genre_id
GROUP BY -- G_ROU_P by one of the non-agregated coluns
	genre
ORDER BY -- O_DE_R as directed
	number_of_shows DESC;
