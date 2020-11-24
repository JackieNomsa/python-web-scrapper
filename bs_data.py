import requests
from bs4 import BeautifulSoup as bs
import re

url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'

#get url using requests
r = requests.get(url)

#fetch data using bs4
soup = bs(r.content)

#fetch each table row from the soup content
table_data = soup.select('tbody.lister-list > tr')

#empty list for data storage
movies = []

#function for data format
def format_movies(data_):
    
    list_movies = data_.select('td.titleColumn')
    ratings = data_.select('td.imdbRating')
    all_links = data_.select('td.titleColumn > a')

    all_actors = all_links[0].attrs
    if 'title' in all_actors:
        actors = all_actors['title']
    else:
        actors = ''
        
    movie = list_movies[0].text.split()
    rating = ratings[0].text.strip('\n')
    year = movie[-1]
    name = ' '.join(movie[1:-1])

    #append to list as a dict
    movies.append({
        'Name': name,
        'Actors': actors,
        'Year': year,
        'Ratings': float(rating)

    })

    return movies


for i in list(table_data):
    format_movies(i)

all_the_movies = movies
