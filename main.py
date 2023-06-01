import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests
import io
import time
import base64
from PIL import Image
# Spotify API credentials
CLIENT_ID = '50bad18bf2d447bf83634b92d0f45629'
CLIENT_SECRET = 'a465652d61304df68ffcdca31d9c99fb'

# Initialize the Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


# Load and display an image

# Load and display an image
image_url = "https://raw.githubusercontent.com/Camroc007/PowerHour/main/external_files/prhr.png"
response = requests.get(image_url)
image = Image.open(io.BytesIO(response.content))

st.image(image, caption="MINI POWER HOUR brought to you by Big Mac and Chips", use_column_width=True)
#st.write("A shot glass should be placed in front of each player. You’ll also need at least a dozen or more beer cans handy. Other drinks, on the other hand, can also be used. \n In Power Hour, players will need to take a shot every 30 seconds. Therefore you will want to avoid stronger beverages. Players can leave at any time, and if they do not take a shot within the time limit, they will be eliminated.") 
st.markdown("<h2 style='text-align: center; font-size: 18px;'>A shot glass should be placed in front of each player. You’ll also need at least a dozen or more beer cans handy. Other drinks, on the other hand, can also be used. \n In Power Hour, players will need to take a half shot basically every 30 seconds. Therefore you will want to avoid stronger beverages. Players can leave at any time, and if they do not take a half shot by the time the song ends, they will be eliminated.</h2>", unsafe_allow_html=True)
import streamlit as st

# YouTube video URL
youtube_url = "https://www.youtube.com/watch?v=PrkcHiDLRDg"

# Extract the video ID from the URL
video_id = youtube_url.split("=")[-1]

# CSS styling for centering the video
centered_style = """
    display: flex;
    justify-content: center;
"""

# Embed the YouTube video with autoplay and centering
iframe_html = f"""
    <div style="{centered_style}">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/{video_id}?autoplay=1" frameborder="0" allowfullscreen></iframe>
    </div>
"""
st.markdown(iframe_html, unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; font-size: 18px;'>Pre-Loaded Playlists: Contact the developer for playlist addition</h2>", unsafe_allow_html=True)
        
def play_song(song):
    # Check if the preview URL is available
    if 'preview_url' in song and song['preview_url'] is not None:
        audio_html = f'<audio src="{song["preview_url"]}" controls autoplay></audio>'
        st.write(audio_html, unsafe_allow_html=True)
        time.sleep(31)
        # Play custom audio
        custom_audio_url = "https://raw.githubusercontent.com/Camroc007/PowerHour/main/external_files/test.mp3"
        response = requests.get(custom_audio_url)
        audio_data = response.content

        base64_audio = base64.b64encode(audio_data).decode("utf-8")
        audio_html = f'<audio src="data:audio/mp3;base64,{base64_audio}" controls autoplay></audio>'
        st.write(audio_html, unsafe_allow_html=True)

        # Display the name of the song
        st.write(f"Completed song - {song['name']} by {song['artists'][0]['name']}")
        time.sleep(3)
    else:
        st.write(f"No preview available for this song: {song['name']} by {song['artists'][0]['name']}")


    # Wait for 30 seconds before transitioning to the next song
    

    

import streamlit as st
from PIL import Image

# Define the image paths and URLs
image_paths = {
    "Housewarming": "https://raw.githubusercontent.com/Camroc007/PowerHour/main/external_files/Housewarming.PNG",
    "Mad Cool 2023": "https://raw.githubusercontent.com/Camroc007/PowerHour/main/external_files/mad_cool.PNG",
}

image_urls = {
    "Housewarming": "https://open.spotify.com/playlist/3NsbNebjUjBiQUYUWNgUge?si=52210acf15aa4590",
    "Mad Cool 2023": "https://open.spotify.com/playlist/4WDK9vUmvKv5t1zVXRF2FK?si=499a2ab294c64b50",
}

# Initialize playlist_uri variable
playlist_uri = None

# Display the clickable images in a horizontal layout
columns = st.columns(len(image_paths))
for i, (image_name, image_path) in enumerate(image_paths.items()):
    column = columns[i % len(columns)]
    if column.button(image_name):
        playlist_uri = image_urls[image_name]
        st.write(f"Selected playlist URI: {playlist_uri}")
    image = Image.open(requests.get(image_path, stream=True).raw)
    column.image(image)
# Allow the user to enter their own playlist URI
playlist_uri_input = st.text_input("Or Enter your Spotify playlist URL:")
if playlist_uri_input:
    playlist_uri = playlist_uri_input
    st.write(f"Entered playlist URI: {playlist_uri}")

if playlist_uri:
    # Fetch the playlist tracks from Spotify
    results = sp.playlist_tracks(playlist_uri)
    tracks = results['items']

    # Iterate over the playlist tracks
    for i, track in enumerate(tracks):
        track_uri = track['track']['uri']
        song = sp.track(track_uri)

        # Check if the song has a preview URL
        if 'preview_url' in song:
            play_song(song)
