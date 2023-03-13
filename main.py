from time import sleep
from chatgpt import Assistant
from elevenlabs import ElevenLabHelper
from VideoUtils import YTDownloader, VideoEditHelper

import contextlib
import wave
import os

PATH_AUDIOS = "single_audio/"

PATH_SYSTEM_MESSAGE = "example/system_message.txt"
PATH_USER_MESSAGE = "example/user_message.txt"
PATH_ASSISTANT_MESSAGE = "example/assistant_message.txt"

PATH_OUTPUTS = "outputs/out.txt"
PATH_IMAGES = "images/"

FILENAME_AUDIO = "sounds.wav"
FILENAME_VIDEO = "video.mp4"
FILENAME_VIDEO_EDITED = "video_edited.mp4"

class Main():


    def __init__(self):

        self.list_talk_duration = []
        self.elevenlab = ElevenLabHelper()

        self.system_message = self.load_message(PATH_SYSTEM_MESSAGE)
        self.user_message = self.load_message(PATH_USER_MESSAGE)
        self.assistant_message = self.load_message(PATH_ASSISTANT_MESSAGE)

        self.assistant = Assistant(system_message = self.system_message, user_message = self.user_message, assistant_message = self.assistant_message)
        self.assistant.get_api_key()

        #answer = assistant.send_message("""Provide a funny conversation between president Biden, former president Trump and former president Obama. 
        #                                          Let them pretend to play Rocket League while they flame each other using profaine language. Leave out any information 
        #                                          that doesn't relate to a person talking. Also leave out descriptions of expressing feelings.""")

        #with open(PATH_OUTPUTS+"out.txt", "w") as text_file:
        #   text_file.write(answer)

    def load_message(self, path):
        with open(path, "r") as text_file:
            return "".join(text_file.readlines())

    def generate_audios_from_text(self, path_outputs, path_audios):
        count = 0
        dialogue_arr = self.load_message(path_outputs).split("\n")
        for item in dialogue_arr:
            if not item == '':
                name, sentence = item.split(":")
                temp_count = str(count) if count > 9 else str(0) + str(count)
                filename = temp_count + "_" + name
                self.elevenlab.generate_audio(path_audios, filename, sentence, name)
                self.list_talk_duration.append((name, self.get_wav_length(path_audios + filename)))
                sleep(1)
                count += 1 

    def merge_audios(self, path, filename):
        infiles =  sorted([path + f for f in os.listdir(path)])

        data = []
        for infile in infiles:
            w = wave.open(infile, 'rb')
            data.append( [w.getparams(), w.readframes(w.getnframes())] )
            
            #TODO REMOVE JUST FOR TESTING PURPOSES
            name = infile.split("_")[-1].split(".")[0]
            self.list_talk_duration.append((name, self.get_wav_length(infile)))

            w.close()
            
        output = wave.open(filename, 'wb')
        output.setparams(data[0][0])
        for i in range(len(data)):
            output.writeframes(data[i][1])
        output.close()

    def get_wav_length(self, fname):
        with contextlib.closing(wave.open(fname,'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            return frames / float(rate)
        
if __name__ == "__main__":
    # ---------- Generate Audios ----------
    main = Main()
    #main.generate_audios_from_text(PATH_OUTPUTS, PATH_AUDIOS)
    #main.merge_audios(PATH_AUDIOS, FILENAME_AUDIO)

    # ---------- Dowload Background Video ----------
    yt_D = YTDownloader("https://www.youtube.com/watch?v=OgtuU8t5eIQ", "1080p")
    yt_D.download()

    # ---------- Edit Video ----------
    videoEditHelper = VideoEditHelper()
    #videoEditHelper.cut_video(yt_D.filename, VIDEO_NAME, yt_D.fps, 0, main.get_wav_length(FILENAME_AUDIO))
    #videoEditHelper.set_audio(FILENAME_AUDIO, VIDEO_NAME)
    videoEditHelper.finalize_video(PATH_IMAGES, main.list_talk_duration, FILENAME_AUDIO, FILENAME_VIDEO, FILENAME_VIDEO_EDITED, 0, main.get_wav_length(FILENAME_AUDIO))
