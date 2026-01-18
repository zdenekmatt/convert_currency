# funkce.py
import requests
import os

API_URL = "https://api.apilayer.com/exchangerates_data/convert"
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise RuntimeError("API_KEY is not set")

def convert_currency(amount, currency_from, currency_to):
    my_params = {
        "from": currency_from,
        "to": currency_to,
        "amount": amount
    }

    my_headers = {
        "apikey": API_KEY
    }

    response = requests.get(
        API_URL,
        params=my_params,
        headers=my_headers,
        timeout=5
    )
    response.raise_for_status()

    data = response.json()

    result = data.get("result")
    if result is None:
        raise ValueError("Invalid API response")

    return result
