import streamlit as st
import sqlite3
import pandas as pd
import os

# Use in-memory DB (auto resets on each run)
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# Load SQL schema
sql_file = "movie_ratings_project.sql"
if not os.path.exists(sql_file):
    st.error("❌ SQL file missing.")
    st.stop()

try:
    with open(sql_file, "r") as f:
        sql_script = f.read()
    cursor.executescript(sql_script)
    conn.commit()
except Exception as e:
    st.error(f"SQL load failed: {e}")
    st.stop()

st.title("🎬 Movie Ratings & Actor Insights")

try:
    genres = pd.read_sql("SELECT * FROM genres", conn)
    movies = pd.read_sql("SELECT * FROM movies", conn)
    actors = pd.read_sql("SELECT * FROM actors", conn)
    movie_actors = pd.read_sql("SELECT * FROM movie_actors", conn)
    ratings = pd.read_sql("SELECT * FROM ratings", conn)
except Exception as e:
    st.error(f"Data loading failed: {e}")
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

st.subheader("📊 Summary")
st.metric("Average Rating", f"{ratings['rating'].mean():.1f}")
st.metric("Total Movies", len(movies))
st.metric("Total Actors", len(actors))
