# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 17:35:40 2024

@author: Jason van den Heever 
"""

import pandas as pd
df=pd.read_csv("movie_dataset.csv")


#Removal of Index Column
df.reset_index(drop=True, inplace=True)


#Choosing to drop as filling 122 values would skew the statistical data 
df.dropna(inplace=True)
df=df.reset_index(drop=True)

#removal of spaces in column titles
df.rename(columns={'Runtime (Minutes)': 'Runtime_(Minutes)'}, inplace=True)
df.rename(columns={'Revenue (Millions)': 'Revenue_(Millions)'}, inplace=True)

# Seperation of Genre and Actors
df["Genre"] = df["Genre"].str.split(",")
df["Actors"] = df["Actors"].str.split(",")



"""
          Q1
"""
# Maximum values
maxValues = df[['Rating', 'Revenue_(Millions)']].max()

# Movie with maximum rating
maxRatingMovie = df[df['Rating'] == maxValues['Rating']]['Title'].values[0]

# Print movie title
print(f"Movie with the maximum rating: {maxRatingMovie}")

"""
        Q2
"""

# Calculate ave revenue
averageRevenue = df['Revenue_(Millions)'].mean()

# Print 
print(f"Average revenue of all movies: ${averageRevenue:.2f} million")

"""
        Q3
"""

# Filter movies from 2015 to 2017
filtered_df = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]

# Average revenue for filtered movies
averageRevenue = filtered_df['Revenue_(Millions)'].mean()

# Print 
print(f"Average revenue of movies from 2015 to 2017: ${averageRevenue:.2f} million")

"""
        Q4
"""

# Count movies (2016)
num_movies_2016 = df[df['Year'] == 2016].shape[0]

# Print 
print(f"Number of movies released in 2016: {num_movies_2016}")

"""
        Q5
"""

# No of movies by Christopher Nolan
nolan_movies = df['Director'].value_counts()['Christopher Nolan']

# Print 
print(f"Number of movies directed by Christopher Nolan: {nolan_movies}")

"""
        Q6
"""

# Filter movies rating >= 8.0
high_rated_movies = df[df['Rating'] >= 8.0]

# Number of movies
num_high_rated_movies = high_rated_movies.shape[0]

# Print 
print(f"Number of movies with rating >= 8.0: {num_high_rated_movies}")

"""
        Q7
"""

# Filter by Christopher Nolan
nolan_movies = df.query("Director == 'Christopher Nolan'")

# Median rating
median_rating = nolan_movies['Rating'].median()

# Print 
print(f"Median rating of movies directed by Christopher Nolan: {median_rating}")

"""
        Q8
"""

# Group by year and calculate average rating
avg_ratings = df.groupby('Year')['Rating'].mean()

# Find year with the highest average rating
highest_rated_year = avg_ratings.idxmax()

# Print
print(f"Year with the highest average rating: {highest_rated_year}")


"""
        Q9
"""

# Movie Count for each year
movies_2006 = df[df['Year'] == 2006]['Title'].count()
movies_2016 = df[df['Year'] == 2016]['Title'].count()

# Percentage increase
percentage_increase = ((movies_2016 - movies_2006) / movies_2006) * 100

# Print 
print(f"Percentage increase in movies between 2006 and 2016: {percentage_increase:.2f}%")

"""
        Q10
"""

import pandas as pd
from collections import Counter

actor_counts = Counter()
for actor_list in df["Actors"]:
    actor_counts.update(actor_list)

most_popular_actors = actor_counts.most_common(5) 

genre_counts = Counter()
for genre_list in df["Genre"]:
    genre_counts.update(genre_list)
most_popular_genres = genre_counts.most_common(5) 

print("Most popular actors:", most_popular_actors)
print("Most popular genres:", most_popular_genres)


"""
        Q11
"""

df_exploded = df.explode("Genre")
number_of_unique_genres = df_exploded["Genre"].nunique()
print("Number of unique genres:", number_of_unique_genres)



"""
        Q12
"""

# Count the occurrences of each genre
genre_counts = Counter()
for genre_list in df["Genre"]:
    genre_counts.update(genre_list)

# Group genre by total revenue
genre_revenue = df.groupby('Genre')['Revenue_(Millions)'].sum()

# Top 5 genres by revenue
top_genres_by_revenue = genre_revenue.nlargest(5)
print("Top 5 genres by revenue:")
for genre, revenue in top_genres_by_revenue.items():
    print(genre, "Revenue:", revenue)
    
    df_exploded = df.explode('Genre')
    avg_metascore_per_genre = df_exploded.groupby('Genre')['Metascore'].mean()

# Print the average Metascore per genre
print(avg_metascore_per_genre)

df['Runtime_to_Revenue_Ratio'] = df['Runtime_(Minutes)'] / df['Revenue_(Millions)']

