FROM python:3.10-alpine

LABEL maintainer="Mohammad Reza Fadaei <mohrezfadaei@gmail.com>"

ENV DEBUG=true
ENV API_URL=None
ENV API_TOKEN=None
ENV API_FROM_CURRENCY=BTC
ENV API_TO_CURRENCY=USD
ENV INFLUX_URL=http://influxdb:8086
ENV INFLUX_SECRET=secret
ENV INFLUX_ORG=admin
ENV UPDATE_INTERVAL_SEC=30

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt


RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "python" ]

CMD [ "app/main.py" ]