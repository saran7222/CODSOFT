import streamlit as st
from datetime import datetime

# Title
st.title("Friendly Assistant")
st.write("Hello! I am a simple chatbot. Ask me something.")

# User input
msg = st.text_input("Type your message")

if msg:
    msg = msg.lower()

    if msg == "hi" or msg == "hello":
        st.success("Hello! Nice to meet you.")

    elif msg == "how are you":
        st.success("I am doing good. Hope you are also doing well.")

    elif msg == "your name":
        st.success("My name is Friendly Assistant.")

    elif msg == "time":
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        st.success("Current time is " + current_time)

    elif msg == "date":
        now = datetime.now()
        current_date = now.strftime("%d-%m-%Y")
        st.success("Today's date is " + current_date)

    elif msg == "internship":
        st.success("Internship helps students gain practical experience.")

    elif msg == "college":
        st.success("College life teaches learning and responsibility.")

    elif msg == "python":
        st.success("Python is simple and useful for many projects.")

    elif msg == "bye":
        st.success("Bye! Have a nice day.")

    else:
        st.warning("Sorry, I do not understand that question.")
