import datetime

print("\n Welcome to Python Chatbot \n")
print("You can chat with the bot.")
print("Type 'help' to see available commands.")
print("Type 'bye' to end the chat.\n")

while True:
    msg = input("You: ").lower()
    if msg == "hello" or msg == "hi":
        print("Bot: Hello! How can I help you today?")
    elif msg == "good morning":
        print("Bot: Good Morning! Have a wonderful day.")
    elif msg == "good evening":
        print("Bot: Good Evening!")    
    elif msg == "what is your name":
        print("Bot: My name is Python Chatbot.")
    elif msg == "who made you":
        print("Bot: I was created using Python programming.")
    elif msg == "what can you do":
        print("Bot: I can answer basic questions, tell time, date, and chat with you.")
    elif msg == "how are you":
        print("Bot: I am doing great. Thanks for asking!")
    elif msg == "i am fine":
        print("Bot: Nice to hear that!")
    elif msg == "i am sad":
        print("Bot: Don't worry. Better days are coming.")
    elif msg == "thank you":
        print("Bot: You're welcome!")
    elif msg == "what is python":
        print("Bot: Python is a simple and powerful programming language.")
    elif msg == "what is ai":
        print("Bot: AI stands for Artificial Intelligence.")
    elif msg == "what is programming":
        print("Bot: Programming means giving instructions to a computer.")
    elif msg == "tell me a joke":
        print("Bot: Why did the computer go to the doctor?")
        print("Bot: Because it caught a virus!")
    elif msg == "your favorite language":
        print("Bot: My favorite language is Python.")
    elif msg == "time":
        current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
        print("Bot: Current Time is", current_time)
    elif msg == "date":
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's Date is", current_date)
    elif msg == "day":
        current_day = datetime.datetime.now().strftime("%A")
        print("Bot: Today is", current_day)
    elif msg == "help":
        print("\n Available Commands \n")
        print("hello / hi")
        print("how are you")
        print("what is your name")
        print("what is python")
        print("what is ai")
        print("tell me a joke")
        print("time")
        print("date")
        print("day")
        print("thank you")
        print("bye")
    elif msg == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break
    else:
        print("Bot: Sorry, I don't understand that.")