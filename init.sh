#!/bin/sh

# Ustaw czas oczekiwania na 10 sekund
max_attempts=10
attempts=0

# Czekaj na połączenie z bazą danych
until curl -s db:5432 || [ $attempts -eq $max_attempts ]; do
  attempts=$((attempts+1))
  echo "Czekam na połączenie z bazą danych... Próba $attempts z $max_attempts"
  sleep 1
done

# Sprawdź, czy połączenie zostało nawiązane
if [ $attempts -eq $max_attempts ]; then
  echo "Nie udało się nawiązać połączenia z bazą danych. Kontynuuję..."
else
  echo "Połączenie z bazą danych nawiązane."
fi

# Tworzenie migracji
python manage.py makemigrations

# Wykonywanie migracji
python manage.py migrate

# utwórz superusera Django jeśli nie istnieje
echo "from users.models import CustomUser as User; User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword') if not User.objects.filter(username='admin').exists() else None" | python manage.py shell

# Uruchom serwer Django
python manage.py runserver 0.0.0.0:8000
