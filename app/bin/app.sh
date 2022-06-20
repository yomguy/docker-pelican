#!/bin/bash

if [ -f /var/in/pelican_conf.py ]; then
    conf=/var/in/pelican_conf.py
else
    conf=pelican_conf.py
fi

if [ "$1" = "--runserver" ]; then
    pelican --debug --autoreload -s $conf
else
    # pelican -s $conf
    pelicangit -s $conf
fi
