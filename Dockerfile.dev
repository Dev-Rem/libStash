FROM python:3.8

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /usr/src/libStash

COPY ./libStash/requirements.txt /usr/src/libStash/

COPY . /usr/src/libStash/

RUN pip install -r requirements.txt

RUN adduser --disabled-password --gecos '' user
USER user



