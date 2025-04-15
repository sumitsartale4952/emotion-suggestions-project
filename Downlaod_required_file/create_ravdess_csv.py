import os
import csv

# Define the mapping from emotion code to emotion label.
emotion_mapping = {
    "01": "neutral",
    "02": "calm",
    "03": "happy",
    "04": "sad",
    "05": "angry",
    "06": "fearful",
    "07": "disgust",
    "08": "surprised"
}

# Set the directory where your RAVDESS files are stored.
# Adjust this path if your files are in a different location.
ravdess_dir = os.path.join("data", "Audio_data")

# Define the output CSV file path.
output_csv = os.path.join("data", "audio_data.csv")

# Open the CSV file for writing.
with open(output_csv, mode="w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    # Write header row.
    writer.writerow(["file", "label"])

    # Walk through the RAVDESS directory (including subdirectories). 
    for root, dirs, files in os.walk(ravdess_dir):
        for file in files:
            if file.lower().endswith(".wav"):
                filepath = os.path.join(root, file)
                # Split the filename by '-' to extract parts.
                parts = file.split('-')
                if len(parts) >= 3:
                    # The third part is the emotion code.
                    emotion_code = parts[2]
                    emotion = emotion_mapping.get(emotion_code, "unknown")
                    # Write the row: file path and corresponding emotion.
                    writer.writerow([filepath, emotion])
                else:
                    print(f"Filename {file} does not follow the expected format.")

print(f"CSV file created at: {os.path.abspath(output_csv)}")
