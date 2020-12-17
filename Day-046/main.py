from bs4 import BeautifulSoup
import requests
import datetime
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

SPOTIFY_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
SPOTIFY_SECRET_KEY = os.environ.get("SPOTIFY_SECRET_KEY")
SPOTIFY_REDIRECT_URI = "http://localhost:8888/callback/"
SPOTIFY_ENDPOINT = f"https://api.spotify.com/v1/users/{SPOTIFY_CLIENT_ID}/playlists"


# Ask user for date
def validate(user_answer):
    try:
        datetime.datetime.strptime(user_answer, "%Y-%m-%d")
        return user_answer
    except ValueError:
        print("Incorrect data format, should be YYYY-MM-DD")


date = None
while date is None:
    date = validate(input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: "))


# Scrape Billboard for top 100 from specific date
res = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}/")
res.raise_for_status()
website = res.text

soup = BeautifulSoup(website, "html.parser")
song_titles = soup.find_all("span", {"class": "chart-element__information__song"})
songs = [song_title.get_text() for song_title in song_titles]


# Authenticate the app on Spotify
scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                               client_secret=SPOTIFY_SECRET_KEY,
                                               redirect_uri=SPOTIFY_REDIRECT_URI,
                                               scope=scope))

results = sp.current_user()
user_id = results["id"]


# Create song list
song_list = []
year = date.split("-")[0]

for song in songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_list.append(uri)
    except IndexError:
        pass


# Create new private playlist
playlist = sp.user_playlist_create(user=user_id,
                                   name=f"{date} Billboard 100",
                                   public=False,
                                   description=f"Playlist with songs from {date}.")


# Add each found song to playlist
sp.playlist_add_items(playlist_id=playlist["id"],
                      items=song_list)
