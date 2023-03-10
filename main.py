from chatgpt import Assistant
from elevenlabs import ElevenLabHelper

def main():
    assistant = Assistant(  system_message = "You are a helpful assistant.", 
                            user_message = "Who won the world series in 2020?", 
                            assistant_message = "The Los Angeles Dodgers won the World Series in 2020."
                        )

    assistant.get_api_key()
    answer = assistant.send_message("How much is the fish?")
    print(answer)

def main2():
    elevenlab = ElevenLabHelper()
    elevenlab.example()

if __name__ == "__main__":
    main2()

