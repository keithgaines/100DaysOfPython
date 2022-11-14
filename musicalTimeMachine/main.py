import requests
from bs4 import BeautifulSoup
import pandas

date = input('Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ')


URL = f'https://www.billboard.com/charts/hot-100/{date}'

response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')

song_names = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")
song_names = [song.get_text().strip('\n\t') for song in song_names]

print(song_names)