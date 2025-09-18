import requests
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()
POLYGON_API_KEY = os.getenv("POLYGON_API_KEY")
LIMIT = 100
url = f'https://api.polygon.io/v3/reference/tickers?market=stocks&active=true&order=asc&limit={LIMIT}&sort=ticker&apiKey={POLYGON_API_KEY}'

tickers = []
while url:
    response = requests.get(url)
    data = response.json()
    # Check for error in response
    if 'results' not in data:
        print("Error:", data.get('status'), data.get('message', data))
        break
    tickers.extend(data['results'])
    url = data.get('next_url')
    if url:
        url += f'&apiKey={POLYGON_API_KEY}'

print(f"Total tickers fetched: {len(tickers)}")

df = pd.DataFrame(tickers)
df.to_csv('tickers.csv', index=False)
print("Data saved to tickers.csv")

