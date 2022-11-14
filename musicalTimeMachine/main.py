import requests
from bs4 import BeautifulSoup
import spotipy
import os
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth


date = input('Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ')


URL = f'https://www.billboard.com/charts/hot-100/{date}'

response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')

song_tags = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")
artists_tags_list = soup.findAll(name="span", class_="a-no-trucate")

song_list_1 = [tag.getText().replace("\n", "") for tag in song_tags]
song_list_2 = [song.replace("\t", "") for song in song_list_1]


artist_list_1 = [tag.getText().replace("\n", "") for tag in artists_tags_list]
artist_list_2 = [artist.replace("\t", "") for artist in artist_list_1]

song_artist_list = dict(zip(artist_list_2, song_list_2))

load_dotenv('./.env.txt')

client_ID = os.environ['SPOTIFY_CLIENT_ID']
client_secret = os.environ['SPOTIFY_CLIENT_SECRET']
redirect_uri = os.environ['REDIRECT_URI']

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope='playlist-modify-private',
        redirect_uri=redirect_uri,
        client_id=client_ID,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)


user_id = sp.current_user()["id"]
spotify_song_uris = []
for key, value in song_artist_list.items():
    spotify_result = sp.search(q=f"artist:{key} track:{value}", type="track")
    try:
        song_uri = spotify_result['tracks']['items'][0]['uri']
        spotify_song_uris.append(song_uri)
    except IndexError:
        print(f"{value} doesn't exist in Spotify. Skipped.")

print(len(spotify_song_uris))

my_playlist = sp.user_playlist_create(
    user=f"{user_id}",
    name=f"Billboard Top Tracks {date}",
    public=False,
    description="Top 100")

playlist_id = my_playlist['id']

sp.user_playlist_add_tracks(user_id, playlist_id, spotify_song_uris, position=None)