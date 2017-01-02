#!/bin/bash

if [ -f /var/in/pelican_conf.py ]; then
    conf=/var/in/pelican_conf.py
else
    conf=pelican_conf.py
fi

pelican -s $conf
