__author__ = 'luoys'
import urllib2
from bs4 import BeautifulSoup as bs


resp = urllib2.urlopen('https://movie.douban.com/cinema/nowplaying/chengdu/')
html_data = resp.read().decode('utf-8')
soup = bs(html_data, 'html.parser')

nowplaying_movie = soup.find_all('div', id='nowplaying')

nowplaying_movie_list = nowplaying_movie[0].find_all('li', class_='list-item')