CREATE TABLE genres (
    genre_id INT PRIMARY KEY,
    genre_name VARCHAR(50)
);

INSERT INTO genres VALUES
(1, 'Action'), (2, 'Drama'), (3, 'Comedy'), (4, 'Sci-Fi');

CREATE TABLE movies (
    movie_id INT PRIMARY KEY,
    title VARCHAR(100),
    release_year INT,
    genre_id INT,
    FOREIGN KEY (genre_id) REFERENCES genres(genre_id)
);

INSERT INTO movies VALUES
(1, 'Interstellar', 2014, 4),
(2, 'The Dark Knight', 2008, 1),
(3, 'The Godfather', 1972, 2),
(4, 'Superbad', 2007, 3);

CREATE TABLE actors (
    actor_id INT PRIMARY KEY,
    name VARCHAR(100)
);

INSERT INTO actors VALUES
(1, 'Leonardo DiCaprio'),
(2, 'Christian Bale'),
(3, 'Al Pacino'),
(4, 'Jonah Hill');

CREATE TABLE movie_actors (
    movie_id INT,
    actor_id INT,
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id),
    FOREIGN KEY (actor_id) REFERENCES actors(actor_id)
);

INSERT INTO movie_actors VALUES
(1, 1), (2, 2), (3, 3), (4, 4), (2, 1);

CREATE TABLE ratings (
    rating_id INT PRIMARY KEY,
    movie_id INT,
    user_id INT,
    rating DECIMAL(2,1),
    review_date DATE,
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id)
);

INSERT INTO ratings VALUES
(1, 1, 101, 9.0, '2020-01-01'),
(2, 2, 102, 9.5, '2020-01-02'),
(3, 3, 103, 9.2, '2020-01-03'),
(4, 4, 104, 7.5, '2020-01-04'),
(5, 2, 105, 9.1, '2020-01-05'),
(6, 1, 106, 8.7, '2020-02-01');