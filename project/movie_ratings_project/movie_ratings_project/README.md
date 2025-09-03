 Movie Ratings Dataset Exploration with Pivot Tables  

- Project Overview  
This project explores a **Movie Ratings dataset** using Python (Pandas)  
It demonstrates:  
- Data cleaning & preprocessing  
- Dataset merging (movies + ratings)  
- Pivot table analysis (user, movie, genre insights)  
- Derived columns (RatingCategory, IsPopular)  
- Export of results to CSV  
- An interactive Streamlit web app for exploration  
- Basic visualizations(bar charts, pie charts)  


---

📂 Project Structure
movie_ratings_project/
│
├── analysis.py # Data analysis with Pandas
├── app.py # Streamlit interactive app
├── movies.csv # Sample dataset (movies)
├── ratings.csv # Sample dataset (ratings)
├── movie_avg_ratings.csv # Exported pivot table (movies)
├── genre_avg_ratings.csv # Exported pivot table (genres)
├── user_avg_ratings.csv # Exported pivot table (users)
├── cleaned_movie_ratings.csv # Final cleaned + merged dataset
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

Getting Started  :-

1) Clone or Download the Project  
Unzip the project folder .  

2) Setup Virtual Environment  
Open cmd terminal inside the project folder and run:  

python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux

3) Install Dependencies
pip install -r requirements.txt

4) Run the Web App
streamlit run app.py

📊 Features

-Pivot Tables
Count of ratings per movie
Movies with avg rating ≥ 4.0
Users who rated more than 5 movies
Top 5 movies by ratings
Highest & lowest rated movies

-Derived Columns
RatingCategory → High / Medium / Low
IsPopular → Yes / No (based on rating count > 10)

-Exports
Pivot tables as CSV
Cleaned dataset as CSV
-Streamlit Web App
Filter by Genre & Rating Category
Interactive charts (Top 5 movies, Genre averages, Ratings distribution)
Downloadable results

🛠️ Technologies Used
Python 3.12
Pandas
Streamlit

~ Author
UNNATI MP
AI & Data Science Student|GSSSIETW.
