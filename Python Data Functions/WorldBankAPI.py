import http.client
import json
import pandas as pd

# World Bank API parameters
country_code = "IN"  # Change to any country code (e.g., 'US', 'BR')
indicators = {
    "GDP": "NY.GDP.MKTP.CD",                 # GDP (current US$)
    "Healthcare": "SH.XPD.CHEX.PC.CD",       # Current health expenditure per capita (US$)
    "Population": "SP.POP.TOTL"  ,            # Total population
    "Unemployement":"SL.UEM.TOTL.ZS",
    "iNFLATION":"FP.CPI.TOTL.ZG"
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
    
    if len(response) > 1:
        for entry in response[1]:
            data_list.append({
                "indicator": key,
                "year": entry['date'],
                "value": entry['value'],
                "country": entry['country']['value']
            })

# Convert to DataFrame
df = pd.DataFrame(data_list)
#df.head()
# Pivot Data to Compare Indicators by Year
pivot_df = df.pivot(index=["year", "country"], columns="indicator", values="value").reset_index()

# Display first few rows
pivot_df.tail(10)

# Export to CSV (optional)
#pivot_df.to_csv(f"{country_code}_economic_indicators.csv", index=False)
