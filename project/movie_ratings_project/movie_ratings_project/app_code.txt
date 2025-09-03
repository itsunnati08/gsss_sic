import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------
# Load Data
# ----------------------
movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")
users = pd.read_csv("users.csv")   # 👈 make sure users.csv exists

# Step 1: Merge ratings with movies
ratings_movies = pd.merge(ratings, movies, on="MovieID", how="inner")

# Step 2: Merge with users
merged = pd.merge(ratings_movies, users, on="UserID", how="inner")

# ----------------------
# Derived Columns
# ----------------------
merged["RatingCategory"] = merged["Rating"].apply(
    lambda x: "High" if x >= 4 else ("Medium" if x >= 3 else "Low")
)

# Count of Ratings per Movie
movie_rating_counts = (
    merged.pivot_table(index="Title", values="Rating", aggfunc="count")
    .reset_index()
    .rename(columns={"Rating": "RatingCount"})
)
movie_avg_ratings = (
    merged.pivot_table(index="Title", values="Rating", aggfunc="mean")
    .reset_index()
    .rename(columns={"Rating": "AvgRating"})
)
movie_rating_counts["IsPopular"] = movie_rating_counts["RatingCount"].apply(
    lambda x: "Yes" if x > 10 else "No"
)

# ----------------------
# Streamlit UI
# ----------------------
st.title("🎬 Movie Ratings Dataset Exploration with Pivot Tables")

# Dataset Preview
st.header("Dataset Preview")
with st.expander("Show Movies Dataset"):
    st.dataframe(movies)
with st.expander("Show Ratings Dataset"):
    st.dataframe(ratings)
with st.expander("Show Users Dataset"):
    st.dataframe(users)

# ----------------------
# Filters
# ----------------------
st.sidebar.header("🔎 Filters")

# Genre Filter
genres = movies["Genre"].unique().tolist()
selected_genre = st.sidebar.selectbox("Select Genre", ["All"] + genres)

# User Filter
users_list = merged["UserID"].unique().tolist()
selected_user = st.sidebar.selectbox("Select User", ["All"] + users_list)

# Rating Range Filter
min_rating, max_rating = st.sidebar.slider(
    "Select Rating Range", 1.0, 5.0, (1.0, 5.0)
)

filtered_data = merged.copy()

if selected_genre != "All":
    filtered_data = filtered_data[filtered_data["Genre"] == selected_genre]

if selected_user != "All":
    filtered_data = filtered_data[filtered_data["UserID"] == selected_user]

filtered_data = filtered_data[
    (filtered_data["Rating"] >= min_rating) & (filtered_data["Rating"] <= max_rating)
]

st.header("🎯 Filtered Dataset")
st.dataframe(filtered_data.head(20))

# ----------------------
# Interactive Insights
# ----------------------
st.header("📊 Interactive Insights")

st.subheader("Movies with Average Rating ≥ 4.0")
highly_rated = filtered_data.groupby("Title")["Rating"].mean().reset_index()
highly_rated = highly_rated[highly_rated["Rating"] >= 4.0]
st.dataframe(highly_rated)

# 🎥 1. Top 5 Movies by Ratings (Prettified with Matching Colors + Export + Table)
st.subheader("🎥 Top 5 Movies by Number of Ratings")

# Pivot table for Top 5
top5 = (
    merged.groupby("Title")["Rating"]
    .count()
    .sort_values(ascending=False)
    .head(5)
    .reset_index()
    .rename(columns={"Rating": "RatingCount"})
)

# Show Pivot Table
st.dataframe(top5)

# Export Option
if st.button("💾 Export Top 5 Movies by Ratings"):
    top5.to_csv("top5_movies_by_ratings.csv", index=False)
    st.success("✅ Exported as top5_movies_by_ratings.csv")

# Prettified Chart
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(
    x="RatingCount",
    y="Title",
    data=top5,
    ax=ax,
    palette="crest"   # 👈 consistent color scheme
)

# Add titles and labels
ax.set_title("⭐ Top 5 Most Rated Movies", fontsize=14, fontweight="bold")
ax.set_xlabel("Number of Ratings", fontsize=12)
ax.set_ylabel("Movie Title", fontsize=12)

# Annotate counts
for i, v in enumerate(top5["RatingCount"]):
    ax.text(v + 0.2, i, str(v), color="black", va="center", fontweight="bold")

st.pyplot(fig)


st.subheader("4. Highest & Lowest Rated Movies")
avg_ratings = filtered_data.groupby("Title")["Rating"].mean().reset_index()
if not avg_ratings.empty:
    highest = avg_ratings.sort_values(by="Rating", ascending=False).head(1)
    lowest = avg_ratings.sort_values(by="Rating", ascending=True).head(1)
    st.write("⭐ Highest Rated")
    st.dataframe(highest)
    st.write("⬇️ Lowest Rated")
    st.dataframe(lowest)
else:
    st.warning("No data available after filtering!")

# ----------------------
# Export Option
# ----------------------
st.header("📂 Export Results")
if st.button("Export Filtered Data to CSV"):
    filtered_data.to_csv("filtered_movie_ratings.csv", index=False)
    st.success("✅ Exported as filtered_movie_ratings.csv")
# ----------------------

# 📊 Pivot Tables & Graphs (Steps 10–13)

# 🎥 10. Average Rating per Movie
st.subheader("🎥 Average Rating per Movie")
pivot_movie_avg = merged.pivot_table(index="Title", values="Rating", aggfunc="mean").reset_index()
st.dataframe(pivot_movie_avg)

if st.button("💾 Export Avg Rating per Movie"):
    pivot_movie_avg.to_csv("movie_avg_ratings.csv", index=False)
    st.success("✅ Exported as movie_avg_ratings.csv")

st.bar_chart(pivot_movie_avg.set_index("Title"))

# 🎭 11. Average Rating per Genre
st.subheader("🎭 Average Rating per Genre")
pivot_genre_avg = merged.pivot_table(index="Genre", values="Rating", aggfunc="mean").reset_index()
st.dataframe(pivot_genre_avg)

if st.button("💾 Export Avg Rating per Genre"):
    pivot_genre_avg.to_csv("genre_avg_ratings.csv", index=False)
    st.success("✅ Exported as genre_avg_ratings.csv")

fig_g, ax_g = plt.subplots()
sns.barplot(x="Rating", y="Genre", data=pivot_genre_avg, ax=ax_g, palette="viridis")
st.pyplot(fig_g)

# 👤 12. Average Rating per User
st.subheader("👤 Average Rating per User")
pivot_user_avg = merged.pivot_table(index="UserID", values="Rating", aggfunc="mean").reset_index()
st.dataframe(pivot_user_avg)

if st.button("💾 Export Avg Rating per User"):
    pivot_user_avg.to_csv("user_avg_ratings.csv", index=False)
    st.success("✅ Exported as user_avg_ratings.csv")

st.line_chart(pivot_user_avg.set_index("UserID"))

# ⭐ 13. Count of Ratings per Movie (Most Rated)
st.subheader("⭐ Count of Ratings per Movie (Most Rated)")
pivot_movie_count = (
    merged.pivot_table(index="Title", values="Rating", aggfunc="count")
    .reset_index()
    .rename(columns={"Rating": "RatingCount"})
)
st.dataframe(pivot_movie_count.sort_values(by="RatingCount", ascending=False))

if st.button("💾 Export Count of Ratings per Movie"):
    pivot_movie_count.to_csv("movie_rating_counts.csv", index=False)
    st.success("✅ Exported as movie_rating_counts.csv")

fig_c, ax_c = plt.subplots()
sns.barplot(
    x="RatingCount",
    y="Title",
    data=pivot_movie_count.sort_values(by="RatingCount", ascending=False).head(10),
    ax=ax_c,
    palette="mako"
)
st.pyplot(fig_c)

# ----------------------
# Visual Insights
# ----------------------
# 🥧 Ratings Distribution (Prettified)
st.subheader("🥧 Ratings Distribution (High / Medium / Low)")

rating_dist = merged["RatingCategory"].value_counts()

# Show as a table too
st.dataframe(rating_dist.reset_index().rename(columns={"index": "Category", "RatingCategory": "Count"}))

# Export Option
if st.button("💾 Export Ratings Distribution"):
    rating_dist.to_csv("ratings_distribution.csv")
    st.success("✅ Exported as ratings_distribution.csv")

#  Pie Chart
fig1, ax1 = plt.subplots(figsize=(6, 6))
colors = sns.color_palette("crest", len(rating_dist))  # 👈 matching color scheme

ax1.pie(
    rating_dist,
    labels=rating_dist.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=colors,
    wedgeprops={"edgecolor": "white"}
)

ax1.set_title("📊 Ratings Distribution", fontsize=14, fontweight="bold")
ax1.axis("equal")  # Equal aspect ratio ensures pie is drawn as a circle

st.pyplot(fig1)
# ----------------------
# 📂 Step 21: Export Cleaned & Merged Dataset
# ----------------------
st.header("🧹 Export Cleaned & Merged Dataset")

# Show a preview
st.dataframe(merged.head(20))

# Export option
if st.button("💾 Export Cleaned Movie Ratings Dataset"):
    merged.to_csv("cleaned_movie_ratings.csv", index=False)
    st.success("✅ Exported as cleaned_movie_ratings.csv")
