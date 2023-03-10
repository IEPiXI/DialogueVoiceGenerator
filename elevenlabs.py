from elevenlabslib import *
from dotenv import load_dotenv
import os

class EvenLabHelper():

    def __init__(self):
        load_dotenv()
        self.api_key = os.environ.get("api-key")
        self.user = ElevenLabsUser(self.api_key)

    def example(self):
        voice = self.user.get_voices_by_name("Rachel")[0]  # This is a list because multiple voices can have the same name
        voice.play_preview(playInBackground=False)

        voice.generate_and_play_audio("Test.", playInBackground=False)

        for historyItem in user.get_history_items():
            if historyItem.text == "Test.":
                # The first items are the newest, so we can stop as soon as we find one.
                historyItem.delete()
                break