FROM python:3.8

WORKDIR /app

ENV PYTHONUNBUFFERED = 1
ENV PYTHONDONTWRITEBYTECODE = 1
ENV DEBUG = 0

COPY ./requirements.txt .
COPY . .

RUN pip install -r requirements.txt

RUN adduser --disabled-password --gecos '' user
USER user


CMD gunicorn --env DJANGO_SETTINGS_MODULE=libStash.settings.production libStash.wsgi:application --bind 0.0.0.0:$PORT


