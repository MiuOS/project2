# Użyj oficjalnego obrazu Pythona jako bazy
FROM python:3.9.6

# Ustaw katalog roboczy w kontenerze
WORKDIR /app

# Skopiuj plik requirements.txt do kontenera i zainstaluj zależności
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Skopiuj resztę kodu źródłowego do kontenera
COPY . .

# Ustaw zmienną środowiskową używaną przez aplikację Django
#ENV PYTHONUNBUFFERED 1

# Polecenie uruchamiane przy starcie kontenera
CMD ["sh", "init.sh"]