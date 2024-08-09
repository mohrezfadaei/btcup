import pytest

from app.services import CurrencyService


@pytest.mark.asyncio
async def test_fetch_and_store_currency_rate(mocker):
    mock_currency_repo = mocker.Mock()
    mock_influx_writer = mocker.Mock()

    mock_currency_repo.get_exchange_rate.return_value = 30000.00
    mock_influx_writer.format_data.return_value = (
        "currency_data,btc_rate=30000.0 1627584010000000000"
    )
    mock_influx_writer.write_data.return_value = None

    service = CurrencyService(
        currency_repo=mock_currency_repo, influx_writer=mock_influx_writer
    )
    await service.fetch_and_store_currency_rate("BTC", "USD")

    mock_currency_repo.get_exchange_rate.assert_called_once_with("BTC", "USD")
    mock_influx_writer.format_data.assert_called_once_with(30000.00)
    mock_influx_writer.write_data.assert_called_once_with(
        "currency_data,btc_rate=30000.0 1627584010000000000"
    )
