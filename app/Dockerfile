FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /srv/app
RUN mkdir /srv/lib
WORKDIR /srv

COPY etc/requirements-debian.txt /srv
RUN apt-get update && \
    DEBIAN_PACKAGES=$(egrep -v "^\s*(#|$)" requirements-debian.txt) && \
    apt-get install -y --force-yes $DEBIAN_PACKAGES && \
    echo fr_FR.UTF-8 UTF-8 >> /etc/locale.gen && \
    locale-gen && \
    apt-get clean

ENV LANG fr_FR.UTF-8
ENV LANGUAGE fr_FR:fr
ENV LC_ALL fr_FR.UTF-8

RUN pip install -U pip

COPY etc/requirements.txt /srv
RUN pip install -r requirements.txt

COPY etc/requirements-dev.txt /srv
RUN pip install -r requirements-dev.txt --src /srv/lib

WORKDIR /srv/app
