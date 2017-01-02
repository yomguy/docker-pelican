#!/bin/bash

if [ -f /var/in/pelicanconf.py ]; then
    conf=/var/in/pelicanconf.py
else
    conf=pelicanconf.py
fi

pelican -s $conf
