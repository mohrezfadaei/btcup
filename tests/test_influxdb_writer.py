import pytest

from app.utils.influxdb_writer import InfluxDBWriter


@pytest.fixture
def influx_writer():
    return InfluxDBWriter(
        influx_url="http://localhost:8086",
        influx_token="test_token",
        influx_org="test_org",
    )


def test_format_data(influx_writer):
    formatted_data = influx_writer.format_data(30000.00)
    assert "btc_rate=30000.0" in formatted_data


@pytest.mark.asyncio
async def test_write_data(mocker, influx_writer):
    mock_write_api = mocker.AsyncMock()
    mock_influx_client = mocker.Mock()
    mock_influx_client.write_api.return_value = mock_write_api

    mocker.patch(
        "app.utils.influxdb_writer.InfluxDBClientAsync", return_value=mock_influx_client
    )

    formatted_data = "currency_data,btc_rate=30000.0 1627584010000000000"
    await influx_writer.write_data(formatted_data)

    mock_write_api.write.assert_called_once_with(
        bucket="currency", record=formatted_data
    )
