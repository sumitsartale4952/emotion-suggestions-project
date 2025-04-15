import requests
import pandas as pd
import os

# Replace with your actual Last.fm API key
API_KEY = "08aa399305b24426122732788fe19f5c"
url = "http://ws.audioscrobbler.com/2.0/"

# Define parameters for the API request to fetch top tracks
params = {
    "method": "chart.gettoptracks",
    "api_key": API_KEY,
    "format": "json",
    "limit": 40  # Number of tracks to fetch; adjust as needed
}

# Make the API request
response = requests.get(url, params=params)

# Debug: Print status code, content type, and response text
print("Status Code:", response.status_code)
print("Content-Type:", response.headers.get("Content-Type"))
print("Response Text:", response.text)

# Check if the response was successful (HTTP 200)
if response.status_code != 200:
    raise Exception(f"Error fetching data: HTTP {response.status_code}")

# Check if the response content is empty or only whitespace
if not response.text.strip():
    raise Exception("Error: Empty response")

# Attempt to decode the JSON response
try:
    data = response.json()
except Exception as e:
    raise Exception(f"Error decoding JSON: {e}\nResponse Text was: {response.text}")

print("JSON Data successfully retrieved.")

# Extract the list of tracks from the response.
# The JSON structure from chart.gettoptracks is typically: {"tracks": {"track": [ ... ] } }
tracks = data.get("tracks", {}).get("track", [])
if not tracks:
    raise Exception("No track data found in JSON response.")

# Prepare a list to store processed music data
music_list = []

# Define a list of sample genres to simulate genre information.
genres = ["Pop", "Rock", "Electronic", "Indie", "Hip-Hop"]

# Define a mapping from genre to mood.
genre_to_mood = {
    "Pop": "happy",
    "Rock": "energetic",
    "Electronic": "excited",
    "Indie": "chill",
    "Hip-Hop": "confident",
    "Unknown": "neutral"
}

# Process each track entry from the API response
for i, track in enumerate(tracks):
    track_name = track.get("name")
    artist_name = track.get("artist", {}).get("name")
    # Use the track's MusicBrainz ID (mbid) if available; otherwise, use the index as an ID.
    track_id = track.get("mbid") if track.get("mbid") else str(i)
    
    # For demonstration, assign a genre by cycling through the predefined genres list.
    genre = genres[i % len(genres)]
    # Map the genre to a mood using our dictionary.
    mood = genre_to_mood.get(genre, "neutral")
    
    music_list.append({
        "id": track_id,
        "title": track_name,
        "artist": artist_name,
        "genre": genre,
        "mood": mood
    })

# Convert the list of music dictionaries to a Pandas DataFrame
df = pd.DataFrame(music_list)

# Ensure the target directory exists before saving the CSV
target_dir = "app/suggestions/data"
os.makedirs(target_dir, exist_ok=True)

# Define the path for the CSV file and save the DataFrame
csv_path = os.path.join(target_dir, "music_data.csv")
df.to_csv(csv_path, index=False)

print(f"CSV saved as {csv_path}")
