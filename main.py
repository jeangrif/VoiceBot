from whisper_client.pipeline import VoicePipeline

if __name__ == "__main__":
    bot = VoicePipeline()
    bot.run("audio/test.wav")
