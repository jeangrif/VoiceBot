FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# On copie le projet Rasa (notamment actions/)
COPY rasa_bot/ /app/

# On passe la licence au build (comme pour rasa)
ARG RASA_LICENSE
ENV RASA_LICENSE=${RASA_LICENSE}

# On installe Rasa Pro + le SDK des actions
RUN pip install --no-cache-dir rasa-pro

EXPOSE 5055

# On lance le serveur d'actions
CMD ["python", "-m", "rasa", "run", "actions", "--debug"]


