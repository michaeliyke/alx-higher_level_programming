-- lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT gen.name, SUM(r.rate) AS rating
FROM tv_genres AS gen
JOIN tv_show_genres AS sgen ON gen.id = sgen.genre_id
JOIN tv_shows AS shows ON shows.id = sgen.show_id
JOIN tv_show_ratings AS r ON r.show_id = shows.id
GROUP BY gen.name
ORDER BY rating DESC;
