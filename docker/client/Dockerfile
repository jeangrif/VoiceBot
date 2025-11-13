FROM python:3.10-slim

WORKDIR /app

COPY whisper_client/ /app/whisper_client/
COPY main.py /app/main.py
COPY audio/ /app/audio/

RUN pip install --no-cache-dir requests

CMD ["python", "main.py"]
