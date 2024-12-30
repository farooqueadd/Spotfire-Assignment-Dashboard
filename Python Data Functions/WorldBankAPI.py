import http.client
import json
import pandas as pd


# World Bank API parameters
country_code = Countryinput    # Change to any country code (e.g., 'US', 'BR')
indicators = {
    "GDP": "NY.GDP.MKTP.CD",                 # GDP (current US$)
    "Healthcare": "SH.XPD.CHEX.PC.CD",       # Current health expenditure per capita (US$)
    "Population": "SP.POP.TOTL",             # Total population
    "Unemployment": "SL.UEM.TOTL.ZS",
    "Inflation": "FP.CPI.TOTL.ZG"
}

# Fetch data from World Bank API
def fetch_world_bank_data(country, indicator):
    conn = http.client.HTTPSConnection("api.worldbank.org")
    endpoint = f"/v2/country/{country}/indicator/{indicator}?format=json&per_page=100"
    conn.request("GET", endpoint)
    response = conn.getresponse()
    data = response.read().decode('utf-8')
    conn.close()
    return json.loads(data)

# Collect data for all indicators
data_list = []
for key, indicator in indicators.items():
    response = fetch_world_bank_data(country_code, indicator)
    
    if len(response) > 1 and 'value' in response[1][0]:
        for entry in response[1]:
            data_list.append({
                "indicator": key,
                "year": entry['date'],
                "value": entry['value'],
                "country": entry['country']['value']
            })

# Convert to DataFrame
df = pd.DataFrame(data_list)

# Define empty DataFrame with explicit types if no data is returned
empty_df = pd.DataFrame({
    'indicator': pd.Series(dtype='string'),
    'year': pd.Series(dtype='string'),
    'value': pd.Series(dtype='float64'),
    'country': pd.Series(dtype='string'),
    'Healthcare': pd.Series(dtype='float64')
})

# Ensure DataFrame is not empty
df = df if len(df) > 0 else empty_df

# Pivot Data to Compare Indicators by Year
if not df.empty:
    pivoted = df.pivot(index=["year", "country"], columns="indicator", values="value").reset_index()
    pivot_df = pivoted[pivoted["year"].astype(int) > 2000]
else:
    pivot_df = empty_df

# Display DataFrame
#print(pivot_df.tail(10))

# Export to CSV (optional)
#pivot_df.to_csv(f"{country_code}_economic_indicators.csv", index=False)
#print(f"Data saved as {country_code}_economic_indicators.csv")
