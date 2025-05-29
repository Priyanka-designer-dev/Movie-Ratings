import streamlit as st
import sqlite3
import pandas as pd
import os

# File paths
sql_file = "movie_ratings_project.sql"
db_file = "movies.db"

# Remove existing DB to avoid duplicate table errors
if os.path.exists(db_file):
    os.remove(db_file)

# Check for SQL file
if not os.path.exists(sql_file):
    st.error("❌ Missing required SQL file.")
    st.stop()

# Create and populate SQLite DB
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

try:
    with open(sql_file, "r") as f:
        sql_script = f.read()
    cursor.executescript(sql_script)
    conn.commit()
except Exception as e:
    st.error(f"❌ SQL execution failed: {e}")
    st.stop()

st.title("🎬 Movie Ratings & Actor Insights")

# Load and display data
try:
    genres = pd.read_sql("SELECT * FROM genres", conn)
    movies = pd.read_sql("SELECT * FROM movies", conn)
    actors = pd.read_sql("SELECT * FROM actors", conn)
    movie_actors = pd.read_sql("SELECT * FROM movie_actors", conn)
    ratings = pd.read_sql("SELECT * FROM ratings", conn)
except Exception as e:
    st.error(f"❌ Failed to load data: {e}")
    st.stop()

st.subheader("🎭 Genres")
st.dataframe(genres)

st.subheader("🎞️ Movies")
st.dataframe(movies)

st.subheader("🌟 Actors")
st.dataframe(actors)

st.subheader("🎬 Castings")
st.dataframe(movie_actors)

st.subheader("⭐ Ratings")
st.dataframe(ratings)

# Summary
st.subheader("📊 Summary")
st.metric("Average Rating", f"{ratings['rating'].mean():.1f}")
st.metric("Total Movies", len(movies))
st.metric("Total Actors", len(actors))