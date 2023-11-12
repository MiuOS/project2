#!/bin/sh

# Czekaj na połączenie z bazą danych (opcjonalnie)

# Tworzenie migracji
python manage.py makemigrations

# Wykonywanie migracji
python manage.py migrate

# Uruchom serwer Django
python manage.py runserver 0.0.0.0:8000
