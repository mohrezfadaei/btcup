FROM python:3.10-alpine

LABEL maintainer="Mohammad Reza Fadaei <mohrezfadaei@gmail.com>"

ENV BTCUP_STOCK_URL=None
ENV BTCUP_API_TOKEN=None
ENV BTCUP_INFLUX_URL=http://influxdb:8086
ENV BTCUP_INFLUX_SECRET=secret
ENV BTCUP_INFLUX_ORG=admin

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt


RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "python" ]

CMD [ "app/main.py" ]