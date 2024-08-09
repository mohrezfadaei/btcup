# py-btcup

**Python BTC Up** application fetches cryptocurrency exchange rates from the Alpha Vantage API and stores them in an InfluxDB database.

## Table of Contents

- [py-btcup](#py-btcup)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Usage](#usage)
  - [Development](#development)
  - [Testing](#testing)
  - [Linting](#linting)
  - [Docker](#docker)
  - [License](#license)

## Features

- Fetches real-time exchange rates between specified cryptocurrencies and fiat currencies.
- Stores exchange rates in an InfluxDB database.
- Uses environment variables for configuration.
- Containerized using Docker.

## Prerequisites

- Python 3.10+
- Docker (for containerization)
- [Alpha Vantage](https://www.alphavantage.co/support/#api-key) API Key
- InfluxDB instance

## Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/mohrezfadaei/btcup.git
    cd btcup
    ```

2. **Install dependencies**:

    ```sh
    make install
    ```

3. **Install development dependencies**:

    ```sh
    make install-dev
    ```

## Configuration

Create a `.env` file in the root directory with the following content:

```env
DEBUG=true
API_TOKEN=your_api_token
API_URL=https://www.alphavantage.co/query
API_FROM_CURRENCY=BTC
API_TO_CURRENCY=USD
INFLUX_URL=your_influx_url
INFLUX_TOKEN=your_influx_secret
INFLUX_ORG=your_influx_org
UPDATE_INTERVAL_SEC=30
```

## Usage

To run the application:

```sh
make run
```

## Development

To set up the development environment, run:

```sh
make install-dev
```

## Testing

To run the tests:

```sh
make test
```

## Linting

To lint the code:

```sh
make lint
```

## Docker

1. **Build Docker image**:

    ```sh
    docker-compose build .
    ```

2. **Start Docker containers**:

    ```sh
    docker-compose up -d
    ```

3. **Stop Docker containers**:

    ```sh
    docker-compose down
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
