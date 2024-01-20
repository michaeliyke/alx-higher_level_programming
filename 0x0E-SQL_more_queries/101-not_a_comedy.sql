-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows
SELECT title
FROM tv_shows
WHERE title NOT IN (
	SELECT title
	FROM tv_shows AS ts
	JOIN tv_show_genres As sg ON ts.id = sg.show_id
	JOIN tv_genres AS g ON g.id = sg.genre_id
	WHERE g.name = 'Comedy'
)
GROUP BY title
ORDER BY title ASC;
