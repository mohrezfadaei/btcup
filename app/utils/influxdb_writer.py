import time

from influxdb_client.client.influxdb_client_async import InfluxDBClientAsync


class InfluxDBWriter:
    def __init__(self, influxdb_url: str, influxdb_token: str, influxdb_org: str):
        self.influxdb_url = influxdb_url
        self.influxdb_token = influxdb_token
        self.influxdb_org = influxdb_org

    def format_data(
        self, currency_rate: str, measurement_name: str = "currency_data"
    ) -> str:
        timestamp = str(int(time.time() * 1e9))
        return f"{measurement_name},btc_rate={currency_rate} {timestamp}"

    async def write_data(self, formatted_data: str, bucket: str = "currency"):
        async with InfluxDBClientAsync(
            url=self.influxdb_url, token=self.influxdb_token, org=self.influxdb_org
        ) as client:
            await client.write_api().write(bucket=bucket, record=formatted_data)
