import requests
import pandas as pd
import os

# Replace with your actual API key from RAWG
API_KEY = "268a990058a7499696662f045eb06d0f"

# Correct RAWG API endpoint for games
url = "https://api.rawg.io/api/games"

# Define parameters for the API request
params = {
    "key": API_KEY,
    "page_size": 40  # Adjust the number of games per request as needed
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

# Prepare a list to store processed game data
games_list = []

# Define a sample mapping from genre to mood.
# You can customize this mapping as needed.
genre_to_mood = {
    "Action": "excited",
    "Adventure": "happy",
    "Puzzle": "thoughtful",
    "RPG": "immersive",
    "Shooter": "intense",
    "Sports": "energetic",
    "Strategy": "focused",
    # Extend or modify the mapping as required.
}

# Process each game entry from the API response
for game in data.get("results", []):
    game_id = game.get("id")
    name = game.get("name")
    
    # Retrieve the first genre if available; otherwise use "Unknown"
    if game.get("genres"):
        genre = game["genres"][0].get("name", "Unknown")
    else:
        genre = "Unknown"
    
    # Map the genre to a mood using the dictionary; default to "neutral" if not found
    mood = genre_to_mood.get(genre, "neutral")
    
    games_list.append({
        "id": game_id,
        "name": name,
        "genre": genre,
        "mood": mood
    })

# Convert the list of game dictionaries to a Pandas DataFrame
df = pd.DataFrame(games_list)

# Ensure the target directory exists before saving the CSV
target_dir = "app/suggestions/data"
os.makedirs(target_dir, exist_ok=True)

# Define the path for the CSV file and save the DataFrame
csv_path = os.path.join(target_dir, "games_data.csv")
df.to_csv(csv_path, index=False)

print(f"CSV saved as {csv_path}")
