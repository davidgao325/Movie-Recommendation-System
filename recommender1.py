# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 13:13:10 2021

@author: david
"""
import pandas as pd
# Recommend movies to users based on popularity, assuming the user has not watched any movies yet
# Create a weighted rating to get an accurate score of a movie based on the number of votes it received
df = pd.read_csv('cleaned_data.csv')
m = df['votes'].quantile(0.90)
C = df['ratings'].mean()
q_movies = df.copy().loc[df['votes'] >= m]
q_movies.shape

def weighted_rating(x, m=m, C=C):
    v = x['votes']
    R = x['ratings']
    # Calculation based on the IMDB formula
    return (v/(v+m) * R) + (m/(m+v) * C)
q_movies['score'] = q_movies.apply(weighted_rating, axis=1)
q_movies = q_movies.sort_values('score', ascending=False)

#Print the top 15 movies
q_movies[['movie', 'votes', 'ratings', 'score']].head(20)
