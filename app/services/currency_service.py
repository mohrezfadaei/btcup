class CurrencyService:
    def __init__(self, currency_repo, influx_writer):
        self.currency_repo = currency_repo
        self.influx_writer = influx_writer

    async def fetch_and_store_currency_rate(self, from_currency: str, to_currency: str):
        try:
            rate = self.currency_repo.get_exchange_rate(from_currency, to_currency)
            formatted_data = self.influx_writer.format_data(rate)
            await self.influx_writer.write_data(formatted_data)
        except Exception as e:
            print(f"Error in fetch_and_store_currency_rate: {e}")
