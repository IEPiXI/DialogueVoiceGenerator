from time import sleep
from chatgpt import Assistant
from elevenlabs import ElevenLabHelper

PATH_AUDIOS = "single_audio/"

PATH_SYSTEM_MESSAGE = "example/system_message.txt"
PATH_USER_MESSAGE = "example/user_message.txt"
PATH_ASSISTANT_MESSAGE = "example/assistant_message.txt"

PATH_OUTPUTS = "outputs/out.txt"
class Main():


    def __init__(self):

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

    def generate_audios_from_text(self):
        count = 0
        dialogue_arr = self.load_message(PATH_OUTPUTS).split("\n")
        for item in dialogue_arr:
            if not item == '':
                name, sentence = item.split(":")
                self.elevenlab.generate_audio(PATH_AUDIOS, str(count) + "_" + name, sentence, name)
                sleep(1)
                count += 1 

if __name__ == "__main__":
    main = Main()
    main.generate_audios_from_text()

