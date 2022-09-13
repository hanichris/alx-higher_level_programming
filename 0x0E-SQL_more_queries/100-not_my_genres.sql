-- List all the genres that are not linked to the show `Dexter`.
SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.id NOT IN(
	SELECT genre_id
	FROM tv_show_genres AS g INNER JOIN tv_shows AS s ON g.show_id = s.id	
	WHERE s.title = 'Dexter')
ORDER BY tv_genres.name;
