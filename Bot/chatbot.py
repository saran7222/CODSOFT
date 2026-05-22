import streamlit as st
import time

print("💖 Welcome to the Love Program 💖")
print("-" * 40)

name = input("✨ Say your name: ").strip().lower()

if name == "keerthi" or name == "keerthivarshini":
    print("\n💗 Checking heart connection... 💗")
    time.sleep(2)

    lines = [
        "🌸 Hey Keerthi... 💕",
        "🫂 You are my fav and when I'm with you I feel happy 💗",
        "😚 I love you so much dii chlo 🫂💗😚",
        "✨ Your smile makes my day brighter ☀️💖",
        "🌍 Among everyone, you are special to me 💕",
        "💞 Talking with you feels like peace and happiness 🥹",
        "🌹 Every moment with you becomes a beautiful memory 💫",
        "💓 You are the reason for many of my smiles 😍",
        "🦋 No matter what happens, you will always be precious 💗",
        "❤️ Thank you for being you, Keerthi 🌸"
    ]

    for line in lines:
        print(line)
        time.sleep(2)

    print("\n🎀 Love Meter Loading... 🎀")
    time.sleep(2)
    print("💯 Love Level: Infinite ♾️💖")

    print("""
          💗💗💗💗💗
        💗           💗
       💗   KEERTHI   💗
        💗           💗
          💗💗💗💗💗
    """)

else:
    print("\n😅 Oops! This love code is only for Keerthi / Keerthivarshini 💔")
