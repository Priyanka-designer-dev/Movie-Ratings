
# 🎬 Movie Ratings & Actor Insights

## 🧩 Project Overview
This SQL-based data analysis project focuses on a movie database to derive insights about genres, ratings, and actors. It simulates how platforms like IMDb or Netflix manage and analyze user-generated rating data.

## 📁 Database Structure
- **genres**: Genre classifications
- **movies**: Film metadata
- **actors**: Actor information
- **movie_actors**: Many-to-many relationship between movies and actors
- **ratings**: User-submitted reviews and ratings

## 🔍 Use Cases
- Determine top-rated genres
- Analyze actor collaboration frequency
- Track changes in genre popularity over time
- Identify top-performing movies with significant user feedback

## 🛠️ SQL Concepts Used
- INNER JOIN
- GROUP BY and HAVING
- Window Functions (optional for trends)
- Aggregates (AVG, COUNT)
- Subqueries

## 📈 Example Queries
- Top-rated movies with more than 50 reviews
- Yearly average ratings per genre
- Actor with most movies
- Most consistent genres over time

## 🚀 How to Run
1. Run the `movie_ratings_project.sql` file to create schema and sample data.
2. Use any SQL interface (MySQL Workbench, pgAdmin, DBeaver) to run the analysis queries.
