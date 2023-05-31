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
image_url = "data:image/jpeg;base64,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"
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
        custom_audio_path = r"C:\Users\cmckenna\Downloads\test.mp3"  # Replace with the path to your custom audio file

        with open(custom_audio_path, "rb") as f:
            audio_data = f.read()
            base64_audio = base64.b64encode(audio_data).decode("utf-8")
            audio_html = f'<audio src="data:audio/mp3;base64,{base64_audio}" controls autoplay></audio>'
            st.write(audio_html, unsafe_allow_html=True)

        # Display the name of the song
        st.write(f"Completed song - {song['name']} by {song['artists'][0]['name']}")
        time.sleep(3)
    else:
        st.write(f"No preview available for this song:{song['name']} by {song['artists'][0]['name']}")

    # Wait for 30 seconds before transitioning to the next song
    

    

import streamlit as st
from PIL import Image

# Define the image URLs
image_urls = {
    "Housewarming": "https://github.com/Camroc007/PowerHour/blob/main/images/Housewarming.PNG",
    "Mad Cool 2023": "https://github.com/Camroc007/PowerHour/blob/main/images/mad_cool.PNG",
}

# Initialize playlist_uri variable
playlist_uri = None

# Display the clickable images in a horizontal layout
columns = st.columns(len(image_urls))
for image_name, image_url in image_urls.items():
    column = columns[image_name]
    if column.button(image_name):
        playlist_uri = image_urls[image_name]
        st.write(f"Selected playlist URI: {playlist_uri}")
    response = requests.get(image_url, stream=True)
    image = Image.open(io.BytesIO(response.content))
    column.image(image)

# Allow the user to enter their own playlist URI
playlist_uri_input = st.text_input("Or enter your Spotify playlist URL:")
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
