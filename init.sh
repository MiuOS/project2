#!/bin/sh

CRON_JOB="* * * * * /usr/local/bin/python /app/manage.py get_payments >> /app/cron.log 2>> /app/cron_error.log #unique_identifier_1"

apt-get update
apt-get install -y cron

# Zainstaluj zależności
pip install -r requirements.txt

# Tworzenie migracji
python manage.py makemigrations

# Wykonywanie migracji
python manage.py migrate

# utwórz superusera Django jeśli nie istnieje
echo "from users.models import CustomUser as User; User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword') if not User.objects.filter(username='admin').exists() else None" | python manage.py shell

(crontab -l | grep -v "#unique_identifier_1" ; echo "$CRON_JOB") | crontab -
service cron start

# Uruchom serwer Django
python manage.py runserver 0.0.0.0:80
