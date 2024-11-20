import os
import requests
from tqdm import tqdm # For progress bar
import json

# Load the JSON file
input_file = "detailed_listings_with_images.json"
output_dir = "images/"
os.makedirs(output_dir, exist_ok=True)

# Load data from JSON
with open(input_file, "r") as file:
    listings = json.load(file)

# Download images
for listing in tqdm(listings):
    image_url = listing.get("image_url")
    if image_url:
        try:
            response = requests.get(image_url, stream=True)
            if response.status_code == 200:
                image_path = os.path.join(output_dir, f"{listing['id']}.jpg")
                with open(image_path, "wb") as img_file:
                    for chunk in response.iter_content(1024):
                        img_file.write(chunk)
        except Exception as e:
            print(f"Failed to download image for listing {listing['id']}: {e}")
