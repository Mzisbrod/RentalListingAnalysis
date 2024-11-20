import json

import requests
import os

# API key
api_key = os.getenv("GOOGLE_API_KEY")
# print(f"API Key: {api_key}")

# Load files
input_file = "detailed_listings.json"
output_file = "detailed_listings_with_images.json"

def get_streetview_image_url(lat, lng, api_key):
    """ Generate Google Street View image URL for given latitude and longitude """
    base_url = "https://maps.googleapis.com/maps/api/streetview"
    params = {
        "location": f"{lat},{lng}",
        "size": "600x400",
        "key": api_key,
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.url
    else:
        print(f"Failed to fetch image for {lat}, {lng}: {response.status_code}")
        return None

# Main processing
with open(input_file, "r") as file:
    listings = json.load(file)

for listing in listings:
    lat = listing.get("latitude")
    lng = listing.get("longitude")
    if lat and lng:
        image_url = get_streetview_image_url(lat, lng, api_key)
        listing["image_url"] = image_url # Add image URL to the listing

# Save the updated listings
with open(output_file, "w") as file:
    json.dump(listings, file, indent=4)

print(f"Updated listings with images saved to {output_file}")





# Example coordinates
# latitude = 40.748817
# longitude = -73.985428


# # Street View API URL
# url = f"https://maps.googleapis.com/maps/api/streetview?location={latitude},{longitude}&size=600x400&key={api_key}"
#
# # Fetch the Street View image
# response = requests.get(url)
#
# # Save the image locally
# if response.status_code == 200:
#     with open("streetview_image.jpg", "wb") as file:
#         file.write(response.content)
#     print("Street View image saved as 'streetview_image.jpg'")
# else:
#     print(f"Error: {response.status_code}")
