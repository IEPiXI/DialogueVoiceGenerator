from elevenlabslib import *
from elevenlabslib.helpers import *
from dotenv import load_dotenv
import os
class ElevenLabHelper():

    def __init__(self):
        load_dotenv()
        self.api_key = os.environ.get("api-key-elevenlabs")
        self.user = ElevenLabsUser(self.api_key)
        self.path_to_audios = "single_audio/"

    def generate_audio(self,text,voice,id):
        voice = self.user.get_voices_by_name(voice)[0]  # This is a list because multiple voices can have the same name
        voice.play_preview(playInBackground=False)
        mp3Data = voice.generate_audio_bytes(text)
        save_bytes_to_path(self.path_to_audios + voice + id + ".wav",mp3Data)
