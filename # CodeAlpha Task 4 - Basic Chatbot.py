# CodeAlpha Task 4 - Basic Chatbot

def chatbot():
    print("===================================")
    print("      Welcome to Simple Chatbot")
    print("Type 'bye' to exit the chatbot.")
    print("===================================")

    while True:
        user = input("\nYou: ").lower()

        if user == "hello":
            print("Bot: Hi! Nice to meet you.")

        elif user == "hi":
            print("Bot: Hello! How can I help you?")

        elif user == "how are you":
            print("Bot: I'm fine, thanks! How about you?")

        elif user == "i am fine":
            print("Bot: Great! Have a wonderful day.")

        elif user == "what is your name":
            print("Bot: I am a simple Python chatbot.")

        elif user == "who created you":
            print("Bot: I was created using Python for CodeAlpha Task 4.")

        elif user == "thank you":
            print("Bot: You're welcome!")

        elif user == "bye":
            print("Bot: Goodbye! Have a nice day.")
            break

        else:
            print("Bot: Sorry, I don't understand that. Please try another question.")

# Run the chatbot
chatbot()