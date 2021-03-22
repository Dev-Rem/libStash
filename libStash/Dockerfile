
FROM python:3.8

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV DEBUG 0

WORKDIR /usr/src/libStash

COPY requirements.txt /usr/src/libStash/

COPY . /usr/src/libStash/

RUN pip install -r requirements.txt

RUN python3.8 manage.py collectstatic --noinput --settings=libStash.settings.development

RUN adduser user
USER user

CMD gunicorn libStash.wsgi:application --bind 0.0.0.0:$PORT



