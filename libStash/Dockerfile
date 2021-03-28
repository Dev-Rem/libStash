FROM python:3.8-alpine3.13

WORKDIR /app

ENV PYTHONUNBUFFERED = 1
ENV PYTHONDONTWRITEBYTECODE = 1
ENV DEBUG = 0

COPY ./requirements.txt .
COPY ./release.sh .
COPY . .

RUN apk add --virtual build-deps cython make libcurl libxml2-dev libxslt-dev tk-dev tcl-dev \
    && apk add build-deps libffi-dev gcc musl-dev libgcc openssl-dev curl-dev \
    && apk add build-deps g++ jpeg-dev zlib-dev lcms2-dev openjpeg-dev tiff-dev \
    && apk add  postgresql-dev fribidi-dev harfbuzz-dev \
    && apk add freetype-dev xz-dev cargo \
    && python3 -m pip install --upgrade pip \
    && pip install psycopg2 Rust \
    && pip install --upgrade Rust \
    && pip install -r requirements.txt \
    && apk del build-deps

RUN adduser --disabled-password --gecos '' user
USER user

CMD gunicorn libStash.wsgi:application --bind 0.0.0.0:$PORT


