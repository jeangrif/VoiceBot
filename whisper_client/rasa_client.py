import os
import time
import requests

class RasaClient:

    def __init__(self, url: str | None = None):
        self.url = url or os.getenv(
            "RASA_URL",
            "http://localhost:5005/webhooks/rest/webhook"
        )

    def ask(self, text: str, retries: int = 5, delay: float = 1.0):
        payload = {"sender": "user", "message": text}

        last_exc = None
        for attempt in range(retries):
            try:
                response = requests.post(self.url, json=payload, timeout=5)
                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException as e:
                last_exc = e
                print(f"[RasaClient] Retry {attempt+1}/{retries} failed: {e}")
                time.sleep(delay)

        raise last_exc
