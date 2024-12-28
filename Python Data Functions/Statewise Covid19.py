import http.client
import json
import pandas as pd

# Choose country ('US', 'India', 'Brazil')
country = "US"  # Change to 'India' or 'Brazil' as needed

# Set endpoint based on country
if country == "US":
    endpoint = "/v3/covid-19/states"
elif country == "India":
    endpoint = "/v3/covid-19/gov/India"
elif country == "Brazil":
    endpoint = "/v3/covid-19/brazil/uf"
else:
    raise ValueError("State-level data not available for this country.")

# Fetch data from Disease.sh API
conn = http.client.HTTPSConnection("disease.sh")
conn.request("GET", endpoint)
response = conn.getresponse()
data = response.read().decode('utf-8')
conn.close()

# Parse JSON response
covid_data = json.loads(data)

# Convert to DataFrame based on country
if country == "US":
    df = pd.DataFrame(covid_data)
    df['state'] = df['state']  # State names in US
elif country == "India":
    df = pd.DataFrame(covid_data['states'])  # India data is nested in 'states'
    df['state'] = df['state']  # State names in India
elif country == "Brazil":
    df = pd.DataFrame(covid_data)  # Direct list for Brazil
    df['state'] = df['state']

# Calculate death rate
df['death_rate'] = (df['deaths'] / df['cases']) * 100

# Display results
df.head()

# Export to CSV
#df.to_csv(f"{country}_statewise_covid19.csv", index=False)
#print(f"Data saved as {country}_statewise_covid19.csv")
