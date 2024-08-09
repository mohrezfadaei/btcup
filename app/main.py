import asyncio
import logging

from app import __version__

from .config import Config
from .repositories import CurrencyRepository
from .services import CurrencyService
from .utils import InfluxDBWriter

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def main():
    logger.info(f"Starting Currency App version {__version__}")

    config = Config()

    api_url = config.get("API_URL")
    api_token = config.get("API_TOKEN")
    api_from_currency = config.get("API_FROM_CURRENCY")
    api_to_currency = config.get("API_TO_CURRENCY")
    influx_url = config.get("INFLUX_URL")
    influx_token = config.get("INFLUX_TOKEN")
    influx_org = config.get("INFLUX_ORG")
    update_interval_sec = config.get("UPDATE_INTERVAL_SEC", default=30)

    currency_repo = CurrencyRepository(api_token=api_token, base_url=api_url)
    influx_writer = InfluxDBWriter(
        influxdb_url=influx_url, influxdb_token=influx_token, influxdb_org=influx_org
    )
    currency_service = CurrencyService(currency_repo, influx_writer)

    while True:
        await currency_service.fetch_and_store_currency_rate(
            api_from_currency, api_to_currency
        )
        await asyncio.sleep(update_interval_sec)


if __name__ == "__main__":
    asyncio.run(main())
