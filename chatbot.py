def chatbot():
    print("AI: Hello! I'm your friendly Assistant. Type 'bye' to exit.")

    while True:
        u_input = input("You: ").lower().strip()

        if u_input == "hello":
            print("AI: Hi there! How can I help you today?")
        elif u_input == "how are you":
            print("AI: I'm just a bunch of code, but I'm running smoothly. How about you?")
        elif u_input == "what's your name":
            print("AI: You can call me ChatBot9000. Sounds cool, right?")
        elif u_input == "bye":
            print("AI: Goodbye! Have a great day.")
            break
        else:
            print("AI: I'm not sure how to respond to that. Try saying 'hello' or 'how are you'.")

chatbot()