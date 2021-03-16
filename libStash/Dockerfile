
FROM python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/libStash

COPY requirements.txt /usr/src/libStash/

COPY . /usr/src/libStash/

RUN pip install -r requirements.txt

EXPOSE 8000



