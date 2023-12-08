#!/bin/sh

# Zainstaluj zależności
pip install -r requirements.txt

# Uruchom serwer Django
python manage.py runserver 0.0.0.0:8080
