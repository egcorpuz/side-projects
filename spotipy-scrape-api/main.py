import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "22bf09ba115843208737facfccc9526c"
CLIENT_SECRET = "d3792ee7638c409cbfdf75422583b5dc"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri="http://example.com",
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path="token.txt",
        username="Gian Corpuz",
    )
)
user_id = sp.current_user()["id"]
print(user_id)
user_input_date = input("Which year do you want to travel to?\n"
                        "Type the date in YYYY-MM-DD format:\n")

URL = f"https://www.billboard.com/charts/hot-100/{user_input_date}/"

response = requests.get(url=URL)
soup = BeautifulSoup(response.text, "html.parser")
top_songs_100 = soup.select("li ul li h3")
songs_text = [song.getText().strip() for song in top_songs_100]
print(songs_text)

song_uris = []
year = user_input_date.split("-")[0]
for song in songs_text:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{user_input_date} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
print("it is done")