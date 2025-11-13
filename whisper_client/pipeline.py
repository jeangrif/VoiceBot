from whisper_client.transcriber import WhisperTranscriber
from whisper_client.rasa_client import RasaClient

class VoicePipeline:

    def __init__(self):
        self.transcriber = WhisperTranscriber()
        self.rasa = RasaClient()

    def run(self, audio_path):
        text = self.transcriber.transcribe(audio_path)
        print("📢 Transcription:", text)

        reply = self.rasa.ask(text)
        print("🤖 Rasa:", reply)
        return reply
