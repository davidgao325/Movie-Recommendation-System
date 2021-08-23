# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 13:59:36 2021

@author: david
"""
import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from time import sleep
from random import randint



import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

from time import sleep
from random import randint

headers = {"Accept-Language": "en-US,en;q=0.5"}

names = []
genres = []
directors = []
actors = []
years = []
time = []
ratings = []
metascores = []
votes = []
US_gross = []

pages = np.arange(1, 1001, 50)

for page in pages: 

  page = requests.get("https://www.imdb.com/search/title/?groups=top_1000&start=" + str(page) + "&ref_=adv_nxt", headers=headers)

  soup = BeautifulSoup(page.text, 'html.parser')
  sleep(randint(2,10))
  movie_div = soup.find_all('div', class_='lister-item mode-advanced')
  for container in movie_div:
      name = container.h3.a.text
      names.append(name)
      genre = container.p.find('span', class_='genre').get_text().strip()
      genres.append(genre)
      year = container.h3.find('span', class_='lister-item-year').text
      years.append(year)
      director = container.find('p', class_='').find_all('a')[0].text
      directors.append(director)
      actors.append([a.text for a in container.find('p', class_='').find_all('a')[1:]])
      runtime = container.p.find('span', class_='runtime').text if container.p.find('span', class_='runtime').text else '-'
      time.append(runtime)
      rating = float(container.strong.text)
      ratings.append(rating)
      m_score = container.find('span', class_='metascore').text if container.find('span', class_='metascore') else '-'
      metascores.append(m_score)
      nv = container.find_all('span', attrs={'name':'nv'})
      vote = nv[0].text
      votes.append(vote)
      grosses = nv[1].text if len(nv) > 1 else '-'
      US_gross.append(grosses)

movies = pd.DataFrame({
'movie': names,
'year': years,
'genres': genres,
'directors': directors,
'actors': actors,
'timeMin': time,
'ratings': ratings,
'metascore': metascores,
'votes': votes,
'us_grossMillions': US_gross,
})

movies.to_csv('movies.csv')

