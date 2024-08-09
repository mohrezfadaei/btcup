import pytest

from app.repositories import CurrencyRepository


@pytest.fixture
def currency_repo():
    return CurrencyRepository(
        api_token="test_api_token", base_url="https://www.alphavantage.co/query"
    )


def test_get_exchange_rate(currency_repo, requests_mock):
    mock_response = {
        "Realtime Currency Exchange Rate": {"5. Exchange Rate": "30000.00"}
    }
    requests_mock.get(
        "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=EUR&apikey=test_api_token",
        json=mock_response,
    )
    rate = currency_repo.get_exchange_rate("USD", "EUR")
    assert rate == 30000.00
