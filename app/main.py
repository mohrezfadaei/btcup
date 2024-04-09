import asyncio
from os import environ
from time import time

from influxdb_client.client.influxdb_client_async import InfluxDBClientAsync
from requests import request

STOCK_URL = environ.get("BTCUP_STOCK_URL")
API_TOKEN = environ.get("BTCUP_API_TOKEN")

INFLUX_URL = environ.get("BTCUP_INFLUX_URL", "http://influxdb:8086")
INFLUX_SECRET = environ.get("BTCUP_INFLUX_SECRET", "secret")
INFLUX_ORG = environ.get("BTCUP_INFLUX_ORG", "admin")


def get_data() -> float:
    query = f"{STOCK_URL}?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey={API_TOKEN}"
    response = request("GET", query)
    data = response.json()
    rate = float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
    return rate


def as_influxdb(currncy_rate: float, measurement_name: str = "currency_data") -> str:
    currncy_rate = str(float)
    timestamp = str(int(time.time() * 1e9))
    return f"{measurement_name},btc rate={currncy_rate} {timestamp}"


async def write_data(currency_data: str):
    try:
        async with InfluxDBClientAsync(
            INFLUX_URL, token=INFLUX_SECRET, org=INFLUX_ORG
        ) as c:
            print(str(currency_data))
            await c.write_api().write("currency", record=as_influxdb())
    except Exception as e:
        print(f"Error writing data: {e}")


async def main():
    while True:
        data = get_data()
        influx_data = as_influxdb(data)
        await write_data(influx_data)
        await asyncio.sleep(30)


if __name__ == "__main__":
    asyncio.run(main())
