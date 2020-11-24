import requests
from bs4 import BeautifulSoup as bs
import re

r = requests.get('https://keithgalli.github.io/web-scraping/example.html')

soup = bs(r.content)

# para = soup.find_all(string=re.compile('Some'))
#if you want to search for part of a string use regular exp (re.compile)
para = soup.find_all(string=('Some bold text'))
#print(para)

url = 'https://keithgalli.github.io/web-scraping/'
j = requests.get(url+'webpage.html')

sauce = bs(j.content)

# info = sauce.select("p")
# for i in info:
#     print(i,'\n')


# links = sauce.select('ul.socials a')
# for link in links:
#     print(link)
#     print()

# other_links = sauce.find('ul',class_='socials')
# actual_links = other_links.find_all('a')
# for i in actual_links:
#     print(i['href'])

# table_data = sauce.find('table','hockey-stats')

# table_links = table_data.select('td a')
# for i in table_links:
#     print(i['href'])

# acha = sauce.find_all(href=re.compile("acha-ii"))
# print(acha)
###############################################
#downloading an image
images = sauce.select('div.row div.column img')
image_url = images[0]['src']

full_url = url+image_url


image_data = requests.get(full_url).content
with open('myimage.jpg','wb') as pic:
    pic.write(image_data)

