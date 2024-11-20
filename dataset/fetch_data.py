import requests
import json
import time

# API credentials
HEADERS = {
    "x-rapidapi-key": "aa40832688msh6a2e2d60f59d8b5p1929a4jsnc3a9a8a32708",
    "x-rapidapi-host": "streeteasy-api.p.rapidapi.com"
}

# Base URLs
SEARCH_URL = "https://streeteasy-api.p.rapidapi.com/rentals/search"
DETAIL_URL = "https://streeteasy-api.p.rapidapi.com/rentals/{}"

# Parameters for search API
QUERY_PARAMS = {
    "areas": "roosevelt-island,all-downtown,all-midtown,all-upper-east-side,all-upper-west-side,all-upper-manhattan",
    "maxPrice": "4000",
    "maxBeds": "1",
    "offset": "0"
}

# Fetch all listings
all_listings = []
while True:
    response = requests.get(SEARCH_URL, headers=HEADERS, params=QUERY_PARAMS)
    if response.status_code != 200:
        print("Error fetching listings:", response.text)
        break

    data = response.json()
    all_listings.extend(data["listings"])

    # Pagination handling
    if "nextOffset" in data["pagination"]:
        QUERY_PARAMS["offset"] = data["pagination"]["nextOffset"]
    else:
        break

    time.sleep(1)  # Avoid hitting API rate limits

# Fetch expanded details for each listing
detailed_listings = []
for listing in all_listings:
    listing_id = listing["id"]
    detailed_response = requests.get(DETAIL_URL.format(listing_id), headers=HEADERS)

    if detailed_response.status_code == 200:
        details = detailed_response.json()
        details["url"] = listing["url"] # Add URL from the search API
        detailed_listings.append(details)
        print(f"Fetched details for listing ID: {listing_id}")
    else:
        print(f"Failed to fetch details for listing ID: {listing_id}")

    time.sleep(1)  # Avoid hitting API rate limits

# Save combined data to JSON file
with open('detailed_listings.json', 'w') as file:
    json.dump(detailed_listings, file, indent=4)

print("Combined data with URLs saved to 'detailed_listings.json'")