import os
import re

def rename_videos(directory):
    # Pattern to match the current filename format
    pattern = re.compile(r'Bluey \(2018\) - (S\d+E\d+) - (.+?) \(\d+p .+\)')

    # Loop through all files in the directory
    for filename in os.listdir(directory):
        # Check if the filename matches the pattern
        match = pattern.match(filename)
        if match:
            # Extract the season/episode and title from the filename
            new_filename = f"{match.group(1)} - {match.group(2)}{os.path.splitext(filename)[1]}"  # Preserve the original file extension
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_filename)

            # Rename the file
            os.rename(old_file, new_file)
            print(f"Renamed: {filename} -> {new_filename}")
        else:
            print(f"Skipped: {filename} (does not match pattern)")

# Directory containing the video files
for season_x in range(1,4):
    video_directory = rf"C:\Users\HP\OneDrive\Videos\Bluey Season {season_x}"

    # Call the rename function
    rename_videos(video_directory)
