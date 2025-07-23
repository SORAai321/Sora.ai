from sora_core import SoraCore

def main():
    sora = SoraCore()
    print("Sora v0.1 is ready to chat with you.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Sora: Bye for now!")
            break
        response = sora.chat(user_input)
        print("Sora:", response)

if __name__ == "__main__":
    main()
