# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 11:38:28 2021

@author: david
"""
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
# Recommend movies to users based on the types of genres they have watched in the past
df = pd.read_csv('cleaned_data.csv')
df['genres'] = df['genres'].fillna('')
tfidf = TfidfVectorizer(stop_words='english')
genres_matrix = tfidf.fit_transform(df['genres'])

similarity_matrix = linear_kernel(genres_matrix,genres_matrix)

mapping = pd.Series(df.index, index = df['movie'])

def recommend_movies_based_on_genre(movie):
    movie_index = mapping[movie]
    similarity_score = list(enumerate(similarity_matrix[movie_index]))
    similarity_score = sorted(similarity_score, key=lambda x: x[1], reverse=True)
    similarity_score = similarity_score[1:15]
    movie_indices = [i[0] for i in similarity_score]
    return(df['movie'].iloc[movie_indices])

recommend_movies_based_on_genre('12 Angry Men')



