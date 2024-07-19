"""CURRENCY CONVERTER"""

import requests

API_KEY = 'fca_live_kRXbhrYCVoGaafro0SDik1iwu7hlHt68YhH3mSyb'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD","CAD","EUR","AUD",]

def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except Exception as e:
        print(e)
        return None
data = convert_currency("CAD")
print(data)
