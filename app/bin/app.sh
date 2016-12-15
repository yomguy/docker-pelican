#!/bin/bash

if [ "$1" = "--runserver" ]; then
    make devserver
else
    pelicangit -s pelicanconf.py
fi
