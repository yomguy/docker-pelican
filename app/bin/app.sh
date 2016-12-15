#!/bin/bash

if [ "$1" = "--runserver" ]; then
    make devserver
else
    make html
    pelicangit -s pelicanconf.py
fi
