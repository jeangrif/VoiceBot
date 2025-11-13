FROM python:3.10-slim

# Dépendances système minimales
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# On copie ton projet Rasa
COPY rasa_bot/ /app/

# On reçoit la licence au build
ARG RASA_LICENSE
ENV RASA_LICENSE=${RASA_LICENSE}

# On installe Rasa Pro
RUN pip install --no-cache-dir rasa-pro

# On entraîne le modèle au build (utilise la licence)
RUN python -m rasa train

EXPOSE 5005

# On lance le serveur Rasa
CMD ["python", "-m", "rasa", "run", "--enable-api", "--cors", "*", "--debug"]
