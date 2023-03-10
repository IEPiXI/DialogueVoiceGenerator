from chatgpt import Assistant


def main():
    assistant = Assistant(  system_message = "You are a helpful assistant.", 
                            user_message = "Who won the world series in 2020?", 
                            assistant_message = "The Los Angeles Dodgers won the World Series in 2020."
                        )
                        
    assistant.get_api_key()
    answer = assistant.send_message("Hey how are you?")
    print(answer)

if __name__ == "__main__":
    main()

