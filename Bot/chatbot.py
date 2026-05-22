from datetime import datetime

print("Simple Chatbot")
print("Type quit to close")

while True:

    msg = input("You : ").lower()

    if msg == "hi" or msg == "hello":
        print("Bot : Hello")

    elif msg == "how are you":
        print("Bot : I am fine. How are you?")

    elif msg == "your name":
        print("Bot : My name is SmartBot")

    elif msg == "time":
        now = datetime.now()
        t = now.strftime("%H:%M")
        print("Bot : Current time is", t)

    elif msg == "date":
        now = datetime.now()
        d = now.strftime("%d-%m-%Y")
        print("Bot : Today's date is", d)

    elif msg == "internship":
        print("Bot : Internship helps to learn practical skills")

    elif msg == "college":
        print("Bot : College life is important for learning and growth")

    elif msg == "python":
        print("Bot : Python is easy and useful for AI projects")

    elif msg == "bye":
        print("Bot : Bye. Have a good day")
        break

    else:
        print("Bot : Sorry, I don't know that")