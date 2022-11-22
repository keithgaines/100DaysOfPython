import requests
from bs4 import BeautifulSoup
import pandas

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')

all_h3 = soup.find_all(name='h3')
movies_ranked = []
for tag in all_h3:
    tag = tag.getText()
    movies_ranked.insert(0, tag)

df = pandas.DataFrame(data={'Top 100 Movies of All Time': movies_ranked})
df.to_csv('ranked movies list.csv', sep=',', index=False)
