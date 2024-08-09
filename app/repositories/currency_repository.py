import requests


class CurrencyRepository:
    def __init__(self, api_token: str, base_url: str):
        self.api_token = api_token
        self.base_url = base_url

    def get_exchange_rate(self, from_currency: str, to_currency: str) -> float:
        query = f"{self.base_url}?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={self.api_token}"
        response = requests.get(query)
        response.raise_for_status()
        data = response.json()
        return float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
