import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_cryptos(limit=10):
    api_key = os.getenv("COINCAP_API_KEY")
    url = f"https://rest.coincap.io/v3/assets?limit={limit}&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    return data["data"]
