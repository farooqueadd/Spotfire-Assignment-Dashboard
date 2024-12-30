import http.client
import json
import pandas as pd

endpoints = {
    "US": "/v3/covid-19/states",
    "India": "/v3/covid-19/gov/India"
}

# Fetch data for each country
def fetch_statewise_data(endpoint):
    conn = http.client.HTTPSConnection("disease.sh")
    conn.request("GET", endpoint)
    response = conn.getresponse()
    
    if response.status != 200:
        print(f"Error: {response.status} - {response.reason} for {endpoint}")
        return None
    
    data = response.read().decode('utf-8')
    conn.close()
    
    if not data or data == "":
        print(f"No data returned for {endpoint}")
        return None
    
    try:
        return json.loads(data)
    except json.JSONDecodeError:
        print(f"Failed to decode JSON for {endpoint}")
        return None

combined_data = []

for country, endpoint in endpoints.items():
    covid_data = fetch_statewise_data(endpoint)
    
    if covid_data is None:
        print(f"Skipping {country} due to API issues.")
        continue
    
    # Print raw response for debugging (optional)
    # print(f"\nRaw Response for {country}:")
    # print(json.dumps(covid_data, indent=2)[:500])

    # Convert to DataFrame based on country
    if country == "US":
        df = pd.DataFrame(covid_data)
        df['state'] = df['state']
        df['country'] = country
    
    elif country == "India":
        df = pd.DataFrame(covid_data['states'])
        df['state'] = df['state']
        df['country'] = country
    """elif country == "Canada":
        if 'provinces' in covid_data:
            df = pd.DataFrame(covid_data['provinces'])
            df['state'] = df['province']
        else:
            # Fallback to single country-level data
            df = pd.DataFrame([covid_data])
            df['state'] = 'Total'
    
    elif country == "UK":
        if 'provinces' in covid_data:
            df = pd.DataFrame(covid_data['provinces'])
            df['state'] = df['province']
        else:
            df = pd.DataFrame([covid_data])
            df['state'] = 'Total' """   
    # Add country name as a column
    
    #df['country_name'] = covid_data.get('country', country)
    
    # Calculate death rate (prevent divide by zero)
    df['death_rate'] = (df['deaths'] / df['cases'].replace(0, 1)) * 100
    
    combined_data.append(df)

# Combine DataFrames
df = pd.concat(combined_data, ignore_index=True)


#print("\nData saved as combined_statewise_covid19.csv")
