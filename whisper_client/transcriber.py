import subprocess
import subprocess
import os

WHISPER_DIR = "whisper/build/bin"
WHISPER_BIN = "./whisper-cli"     # note: local to WHISPER_DIR
MODEL_PATH = "../../models/ggml-base.en.bin"  # relative from WHISPER_DIR

class WhisperTranscriber:
    @staticmethod
    def transcribe(audio_path: str) -> str:

        return "Hello word"
