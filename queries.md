Make sure you download the starter code and run the following:

```sh
  psql < movies.sql
  psql movies_db
```

In markdown, you can place a code block inside of three backticks (```) followed by the syntax highlighting you want, for example

\```sql

SELECT \* FROM users;

\```

Using the `movies_db` database, write the correct SQL queries for each of these tasks:

1.  The title of every movie.
```select title from movies;```
2.  All information on the G-rated movies.
``` select \* from movies where rating = 'G'; ```
3.  The title and release year of every movie, ordered with the
    oldest movie first.
``` select title, release_year from movies order by release_year asc;  ```
4.  All information on the 5 longest movies.
``` select \* from movies limit 5; ```
5.  A query that returns the columns of `rating` and `total`, tabulating the
    total number of G, PG, PG-13, and R-rated movies.
``` select rating, count(\*) as total from movies group by rating; ```
6.  A table with columns of `release_year` and `average_runtime`,
    tabulating the average runtime by year for every movie in the database. The data should be in reverse chronological order (i.e. the most recent year should be first).
``` select release_year, avg(runtime) as average_runtime from movies group by release_year order by release_year desc; ```
7.  The movie title and studio name for every movie in the
    database.
``` select movies.title, studios.name from movies join studios on studios.id = movies.studio_id; ```
8.  The star first name, star last name, and movie title for every
    matching movie and star pair in the database.
``` select stars.first_name, stars.last_name, movies.title from movies join roles on movies.id = roles.movie_id join stars on stars.id = roles.star_id; ```
9.  The first and last names of every star who has been in a G-rated movie. The first and last name should appear only once for each star, even if they are in several G-rated movies. *IMPORTANT NOTE*: it's possible that there can be two *different* actors with the same name, so make sure your solution accounts for that.
``` select stars.first_name, stars.last_name from movies join roles on movies.id = roles.movie_id join stars on stars.id = roles.star_id where movies.rating = 'G' group by stars.id; ```
10. The first and last names of every star along with the number
    of movies they have been in, in descending order by the number of movies. (Similar to #9, make sure
    that two different actors with the same name are considered separately).
``` select stars.first_name, stars.last_name, count(*) from movies join roles on movies.id = roles.movie_id join stars on stars.id = roles.star_id group by stars.id; ```
### The rest of these are bonuses

11. The title of every movie along with the number of stars in
    that movie, in descending order by the number of stars.
``` select movies.title, count(*) from movies join roles on movies.id = roles.movie_id join stars on stars.id = roles.star_id group by movies.title; ```
12. The first name, last name, and average runtime of the five
    stars whose movies have the longest average.
``` select stars.first_name, stars.last_name, round(avg(movies.runtime),1) as average_runtime from movies join roles on movies.id = roles.movie_id join stars on stars.id = roles.star_id group by stars.id order by average_runtime desc; ```
13. The first name, last name, and average runtime of the five
    stars whose movies have the longest average, among stars who have more than one movie in the database.
``` select stars.first_name, stars.last_name, round(avg(movies.runtime),1) as average_runtime from movies join roles on movies.id = roles.movie_id join stars on stars.id = roles.star_id where stars.id in (select stars.id from stars join roles on roles.star_id = stars.id join movies on movies.id = roles.movie_id group by stars.id having count(*) > 1) group by stars.id order by average_runtime desc limit 5; ```
14. The titles of all movies that don't feature any stars in our
    database.
```  ```
15. The first and last names of all stars that don't appear in any movies in our database.
```  ```
16. The first names, last names, and titles corresponding to every
    role in the database, along with every movie title that doesn't have a star, and the first and last names of every star not in a movie.
```  ```