import pandas as pd

# Step 1 – Load Data
movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")

# Step 2 – Data Cleaning
# (check and drop missing values if any)
movies.dropna(inplace=True)
ratings.dropna(inplace=True)

# Step 3 – Merge Datasets
merged = pd.merge(ratings, movies, on="MovieID", how="left")

# ------------------ Step 4 – Pivot Table Analysis ------------------

# 13. Count of ratings per movie
ratings_count = merged.pivot_table(index="Title", values="Rating", aggfunc="count").sort_values("Rating", ascending=False)
print("\n13. Count of ratings per movie:\n", ratings_count)

# 14. Movies with average rating ≥ 4.0
highly_rated_movies = merged.groupby("Title")["Rating"].mean().reset_index()
highly_rated_movies = highly_rated_movies[highly_rated_movies["Rating"] >= 4.0]
print("\n14. Movies with avg rating ≥ 4.0:\n", highly_rated_movies)

# 15. Users who rated more than 5 movies
user_rating_counts = merged.groupby("UserID")["MovieID"].count().reset_index()
active_users = user_rating_counts[user_rating_counts["MovieID"] > 5]
print("\n15. Users who rated more than 5 movies:\n", active_users)

# 16. Top 5 movies by number of ratings
top5_movies = ratings_count.head(5)
print("\n16. Top 5 movies by number of ratings:\n", top5_movies)

# 17. Movies with highest and lowest average ratings
avg_ratings = merged.groupby("Title")["Rating"].mean().reset_index()
highest_rated = avg_ratings.loc[avg_ratings["Rating"].idxmax()]
lowest_rated = avg_ratings.loc[avg_ratings["Rating"].idxmin()]
print("\n17. Highest rated movie:\n", highest_rated)
print("17. Lowest rated movie:\n", lowest_rated)

# ------------------ Step 6 – Derived Columns ------------------

# 18. Add RatingCategory
merged["RatingCategory"] = merged["Rating"].apply(
    lambda x: "High" if x >= 4 else ("Medium" if 3 <= x < 4 else "Low")
)

# 19. Add IsPopular (movie with >10 ratings)
movie_counts = merged.groupby("MovieID")["Rating"].transform("count")
merged["IsPopular"] = movie_counts.apply(lambda x: "Yes" if x > 10 else "No")

# ------------------ Step 7 – Export Results ------------------

# 20. Export pivot tables
movie_avg_ratings = merged.groupby("Title")["Rating"].mean().reset_index()
genre_avg_ratings = merged.groupby("Genre")["Rating"].mean().reset_index()
user_avg_ratings = merged.groupby("UserID")["Rating"].mean().reset_index()

movie_avg_ratings.to_csv("movie_avg_ratings.csv", index=False)
genre_avg_ratings.to_csv("genre_avg_ratings.csv", index=False)
user_avg_ratings.to_csv("user_avg_ratings.csv", index=False)

# 21. Export cleaned and merged dataset
merged.to_csv("cleaned_movie_ratings.csv", index=False)

print("\n✅ Export completed! CSV files generated in your folder.")
# Export results as HTML tables so webpage can display them
movie_avg_ratings.to_html("movie_avg_ratings.html", index=False)
genre_avg_ratings.to_html("genre_avg_ratings.html", index=False)
user_avg_ratings.to_html("user_avg_ratings.html", index=False)
