# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 15:49:45 2021

@author: david
"""
import pandas as pd

df = pd.read_csv('movies.csv')
# Remove any unecessary punctuation and coonvert some data types into integers for analysis and model building later on
df['genres'] = df['genres'].str.replace(',','')
df['us_grossMillions'] = df['us_grossMillions'].str.replace('$','')
df['us_grossMillions'] = df['us_grossMillions'].str.replace('M','')
df['votes'] = df['votes'].str.replace(',','')
df['votes'] = df['votes'].astype(int)
df['year'] = df['year'].str.extract('(\d+)').astype(int)
df['timeMin'] = df['timeMin'].str.replace('min','')
df['timeMin'] = df['timeMin'].astype(int)
df['us_grossMillions'] = pd.to_numeric(df['us_grossMillions'], errors='coerce')
df.to_csv("cleaned_data.csv")
