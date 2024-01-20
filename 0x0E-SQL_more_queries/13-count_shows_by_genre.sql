-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT
	genres.name AS genre,
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

/*
	Here, there are three tables to work with, tv_shows, tv_show_genres, and tv_genres.
	shows - id, title, etc
	tv_show_genres - show_id, genre_id, etc
	tv_genres - id, name, etc

	I need to print show genre names from tv_genres, and count how of such shows from
	tv_shows. So I make tv_show_genres be the middle man since it has information from
	both sides.

	S_elec_t all tv_shows
	join it directly with the tv_show_genres (they have show_id in common)
	join the result with the tv_gengres (they have genre_id in common through tv_show_genres)
	group by genre since it is among non-aggregated values
	finally order by number_of_shows as required
*/
