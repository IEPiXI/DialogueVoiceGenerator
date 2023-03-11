from chatgpt import Assistant
from elevenlabs import ElevenLabHelper

PATH_AUDIOS = "single_audio/"

PATH_SYSTEM_MESSAGE = "example/system_message.txt"
PATH_USER_MESSAGE = "example/user_message.txt"
PATH_ASSISTANT_MESSAGE = "example/assistant_message.txt"

PATH_OUTPUTS = "outputs/"

def main():
     
    system_message = load_message(PATH_SYSTEM_MESSAGE)
    user_message = load_message(PATH_USER_MESSAGE)
    assistant_message = load_message(PATH_ASSISTANT_MESSAGE)

    assistant = Assistant(system_message = system_message, user_message = user_message, assistant_message = assistant_message)
    assistant.get_api_key()

    answer = assistant.send_message("""Provide a funny conversation between president Biden, former president Trump and former president Obama. 
                                              Let them pretend to play Rocket League while they flame each other using profaine language. Leave out any information 
                                              that doesn't relate to a person talking. Also leave out descriptions of expressing feelings.""")

    with open(PATH_OUTPUTS+"out.txt", "w") as text_file:
       text_file.write(answer)
    
    generate_audios_from_text(answer)

def load_message(path):
    with open(path, "r") as text_file:
       return "".join(text_file.readlines())

def generate_audios_from_text(text):
    pass

def main2():
    elevenlab = ElevenLabHelper()
    elevenlab.generate_audio(PATH_TO_AUDIOS,"1","your mum is gay","Rachel")

if __name__ == "__main__":
    main()


