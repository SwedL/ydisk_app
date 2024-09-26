# pull the official base image
FROM python:3.11.4-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYCURL_SSL_LIBRARY=openssl

# install dependencies
RUN pip install --upgrade pip
COPY ../requirements.txt /usr/src/app
RUN apk add -u --no-cache libcurl libstdc++ \
    && apk add -u --no-cache --virtual .build-deps build-base g++ libffi-dev curl-dev \
    && pip install --no-cache-dir pycurl asyncio aiohttp[speedups] pycryptodomex scapy pandas \
    && pip install --no-cache-dir pytz influxdb slackclient certifi xlsxwriter \
    && apk del --no-cache --purge .build-deps \
    && rm -rf /var/cache/apk/*
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app
