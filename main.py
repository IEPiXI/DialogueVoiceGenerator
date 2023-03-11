from chatgpt import Assistant
from elevenlabs import ElevenLabHelper

PATH_TO_AUDIOS = "single_audio/"

def main():
    elevenlab = ElevenLabHelper()
    assistant = Assistant(  system_message = "You provide trialogues between three people."
                         )

    assistant.get_api_key()
    answer = assistant.send_message("""Provide a funny conversation between president Biden, former president Trump and former president Obama. 
                                              Let them pretend to play Rocket League while they flame each other. Leave out any information 
                                              that doesn't relate to a person talking. """)
    print(answer)


if __name__ == "__main__":
    main()


