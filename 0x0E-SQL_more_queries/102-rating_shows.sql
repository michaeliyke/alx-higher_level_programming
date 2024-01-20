--  lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT shows.title, SUM(rating.rate) AS rating
FROM tv_shows AS shows
LEFT JOIN tv_show_ratings AS rating ON shows.id = rating.show_id
GROUP BY shows.title
ORDER BY rating DESC;
