#!/bin/bash

if [ -f /var/in/pelicanconf.py ]; then
    conf=/var/in/pelicanconf.py
else
    conf=pelicanconf.py
fi

if [ "$1" = "--runserver" ]; then
    pelican --debug --autoreload -s $conf
else
    # pelican -s $conf
    pelicangit -s $conf
fi
