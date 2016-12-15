#!/bin/bash

if [ "$1" = "--runserver" ]; then
    make devserver
else
    make html
    if [ -f /var/in/pelicanconf.py ]; then
        pelicangit -s /var/in/pelicanconf.py
    else
        pelicangit -s pelicanconf.py
    fi
fi
