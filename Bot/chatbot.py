import streamlit as st
from datetime import datetime

# Title and welcome message
st.title("Friendly Assistant")
st.write("Hello! Welcome to Friendly Assistant.")
st.write("You can ask me simple questions.")

# User input
msg = st.text_input("Type your message")

if msg:
    msg = msg.lower()

    if msg == "hi" or msg == "hello":
        st.success("Hello! Nice to meet you.")

    elif msg == "how are you":
        st.success("I am doing well. Hope you are also fine.")

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
        st.success("Internship helps students learn practical skills and workplace experience.")

    elif msg == "college":
        st.success("College life is important for learning, friendship and career growth.")

    elif msg == "python":
        st.success("Python is an easy programming language and useful for AI and data projects.")

    elif msg == "ai":
        st.success("Artificial Intelligence helps machines think and solve problems.")

    elif msg == "machine learning":
        st.success("Machine Learning is a part of AI that learns from data.")

    elif msg == "who created you":
        st.success("I am a simple chatbot created using Python and Streamlit.")

    elif msg == "good morning":
        st.success("Good morning! Have a productive day.")

    elif msg == "good night":
        st.success("Good night! Take care and sleep well.")

    elif msg == "thank you":
        st.success("You are welcome. Happy to help you.")

    elif msg == "bye":
        st.success("Bye! Have a nice day.")

    else:
        st.warning("Sorry, I do not understand that question. Please try another one.")
