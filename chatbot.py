def chatbot():
    print("ChatBot: Hello! I am your AI chatbot.")
    print("ChatBot: Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ["hello", "hi", "hey"]:
            print("ChatBot: Hello! How can I help you?")

        elif "how are you" in user_input:
            print("ChatBot: I am fine. Thanks for asking!")

        elif "your name" in user_input:
            print("ChatBot: My name is CODSOFT ChatBot.")

        elif "help" in user_input:
            print("ChatBot: I can answer simple questions about myself.")

        elif "thank" in user_input:
            print("ChatBot: You're welcome!")

        elif user_input in ["bye", "exit", "quit"]:
            print("ChatBot: Goodbye! Have a nice day.")
            break

        else:
            print("ChatBot: Sorry, I don't understand that.")

chatbot()