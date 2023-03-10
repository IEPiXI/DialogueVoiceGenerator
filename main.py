from chatgpt import Assistant


def main():
    assistant = Assistant()
    assistant.get_api_key()
    answer = assistant.send_message("Hey how are you?")
    print(answer)
    
if __name__ == "__main__":
    main()

