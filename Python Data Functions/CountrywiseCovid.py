import http.client
import json
import pandas as pd

# List of countries to fetch data for
countries =  [ "India", 
    "USA", 
    "Brazil", 
    "Germany", 
    "Japan", 
    "South Africa",
    "Saudi Arabia" ]

# Function to fetch COVID-19 data for a specific country
def fetch_country_data(country):
    conn = http.client.HTTPSConnection("disease.sh")
    endpoint = f"/v3/covid-19/countries/{country.replace(' ', '%20')}"
    conn.request("GET", endpoint)
    response = conn.getresponse()
    data = response.read().decode('utf-8')
    conn.close()
    return json.loads(data)

# Collect data for each country
data_list = []
for country in countries:
    data = fetch_country_data(country)
    data_list.append({
        "country": data.get('country', 'N/A'),
        "cases": data.get('cases', 0),
        "deaths": data.get('deaths', 0),
        "recovered": data.get('recovered', 0),
        "vaccinated": data.get('population', 0),  # Use population as a proxy for vaccination
        "population": data.get('population', 0)
    })

# Convert to DataFrame
df = pd.DataFrame(data_list)

# Calculate death rate and vaccination rate
df['death_rate'] = (df['deaths'] / df['cases']) * 100
df['vaccination_rate'] = (df['vaccinated'] / df['population']) * 100

# Display DataFrame
#print(df)

# Export to CSV (optional)
#df.to_csv("covid19_country_specific.csv", index=False)
