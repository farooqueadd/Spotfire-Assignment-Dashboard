import http.client
import json
import urllib.parse  # For URL encoding
import pandas as pd

# Define the state and amenity to fetch data for
state_name = "California"  # Change this for different states
amenities = ["hospital", "clinic", "pharmacy"]

# Build Overpass query
query = f"""
[out:json];
area[name="{state_name}"]->.searchArea;
(
  node["amenity"="{amenities[0]}"](area.searchArea);
  node["amenity"="{amenities[1]}"](area.searchArea);
  node["amenity"="{amenities[2]}"](area.searchArea);
);
out body;
"""

# URL encode the query to handle special characters
encoded_query = urllib.parse.quote(query)

# Set up http.client connection
conn = http.client.HTTPSConnection("overpass-api.de")

# Send the request to Overpass API
conn.request("GET", f"/api/interpreter?data={encoded_query}")
response = conn.getresponse()
data = response.read().decode('utf-8')

# Parse JSON response
osm_data = json.loads(data)

# Extract relevant fields for DataFrame
elements = osm_data.get('elements', [])
facilities = []

for element in elements:
    facilities.append({
        'id': element.get('id'),
        'lat': element.get('lat'),
        'lon': element.get('lon'),
        'name': element.get('tags', {}).get('name', 'N/A'),
        'amenity': element.get('tags', {}).get('amenity', 'N/A'),
        'address': element.get('tags', {}).get('addr:street', 'N/A'),
        'city': element.get('tags', {}).get('addr:city', 'N/A'),
        'state': state_name,
        'phone': element.get('tags', {}).get('phone', 'N/A')
    })

# Convert to Pandas DataFrame
df = pd.DataFrame(facilities)

# Display first few rows
df.head()

# Export to CSV (optional)
df.to_csv(f"{state_name}_healthcare_facilities.csv", index=False)