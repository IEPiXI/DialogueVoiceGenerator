from elevenlabslib import *
from elevenlabslib.helpers import *
from dotenv import load_dotenv
import os
class ElevenLabHelper():

    def __init__(self):
        load_dotenv()
        self.api_key = os.environ.get("api-key-elevenlabs")
        self.user = ElevenLabsUser(self.api_key)

    def generate_audio(self, path, file_name, text, voice):
        voice = self.user.get_voices_by_name(voice)[0]  # This is a list because multiple voices can have the same name
        mp3Data = voice.generate_audio_bytes(text)
        
        if not os.path.exists(path):
            os.mkdir(path)
            
        save_bytes_to_path(path + file_name + ".wav",mp3Data)
