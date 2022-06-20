FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /srv/app
RUN mkdir /srv/lib
WORKDIR /srv

RUN apt-get update && \
    apt-get install -y --force-yes git && \
    apt-get clean

RUN pip install -U pip

COPY requirements.txt /srv
RUN pip install -r requirements.txt

COPY requirements-dev.txt /srv
RUN pip install -r requirements-dev.txt --src /srv/lib

WORKDIR /srv/app
