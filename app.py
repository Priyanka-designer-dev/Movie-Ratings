import streamlit as st
import sqlite3
import pandas as pd
import os

# File path
sql_file = "movie_ratings_project.sql"

# Check if SQL file exists
if not os.path.exists(sql_file):
    st.error(f"❌ Missing required file: {sql_file}")
    st.stop()

# Create SQLite database
conn = sqlite3.connect("movies.db")
cursor = conn.cursor()

# Read and execute SQL script
try:
    with open(sql_file, "r") as f:
        sql_script = f.read()
    cursor.executescript(sql_script)
    conn.commit()
except Exception as e:
    st.error(f"❌ SQL execution failed: {e}")
    st.stop()

st.title("🎬 Movie Ratings & Actor Insights")

# Genres
st.subheader("🎭 Genres")
genres = pd.read_sql("SELECT * FROM genres", conn)
st.dataframe(genres)

# Movies
st.subheader("🎞️ Movies")
movies = pd.read_sql("SELECT * FROM movies", conn)
st.dataframe(movies)

# Actors
st.subheader("🌟 Actors")
actors = pd.read_sql("SELECT * FROM actors", conn)
st.dataframe(actors)

# Movie-Actor Relationships
st.subheader("🎬 Castings")
movie_actors = pd.read_sql("SELECT * FROM movie_actors", conn)
st.dataframe(movie_actors)

# Ratings
st.subheader("⭐ Ratings")
ratings = pd.read_sql("SELECT * FROM ratings", conn)
st.dataframe(ratings)

# Summary Metrics
st.subheader("📊 Summary")
avg_rating = ratings["rating"].mean()
total_movies = movies.shape[0]
total_actors = actors.shape[0]

st.metric("Average Rating", f"{avg_rating:.1f}")
st.metric("Total Movies", total_movies)
st.metric("Total Actors", total_actors)