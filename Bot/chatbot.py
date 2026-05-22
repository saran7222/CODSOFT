import streamlit as st
from datetime import datetime

st.title("Simple Chatbot")

msg = st.text_input("You :")

if msg:
    msg = msg.lower()

    if msg == "hi" or msg == "hello":
        st.write("Bot : Hello")

    elif msg == "how are you":
        st.write("Bot : I am fine. How are you?")

    elif msg == "your name":
        st.write("Bot : My name is SmartBot")

    elif msg == "time":
        now = datetime.now()
        t = now.strftime("%H:%M")
        st.write("Bot : Current time is " + t)

    elif msg == "date":
        now = datetime.now()
        d = now.strftime("%d-%m-%Y")
        st.write("Bot : Today's date is " + d)

    elif msg == "internship":
        st.write("Bot : Internship helps to learn practical skills")

    elif msg == "college":
        st.write("Bot : College life is important for learning and growth")

    elif msg == "python":
        st.write("Bot : Python is easy and useful for AI projects")

    elif msg == "bye":
        st.write("Bot : Bye. Have a good day")

    else:
        st.write("Bot : Sorry, I don't know that")
