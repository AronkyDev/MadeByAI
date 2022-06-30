from matplotlib.pyplot import text
import speech_recognition as sr #convert speech to text
import datetime #for fetching date and time
import wikipedia
import webbrowser
import requests
import playsound # to play saved mp3 file 
from gtts import gTTS # google text to speech 
import os # to save/open files 
import wolframalpha # to calculate strings into formula
from selenium import webdriver # to control browser operations

# Create a voice assistant

def assistant():
    # Create a speech recognizer
    r = sr.Recognizer()
    # Create a microphone
    m = sr.Microphone()
    # Create a voice assistant
    while True:
        # Ask the user to speak
        print("Speak: ")
        with m as source:
            audio = r.listen(source)
        # Convert speech to text
        try:
            text = r.recognize_google(audio)
            print("You said: " + text)
        except:
            print("Sorry, I didn't catch that")
        # Check if the user said "Hello"
        if "hello" in text:
            # Respond with a TTS
            assistant_response = "Hello, how are you?"
            tts = gTTS(text=assistant_response, lang='en')
            tts.save("hello.mp3")
            playsound.playsound("hello.mp3", True)
            print("Hello to you too")
        # Check if the user said "Good morning"
        elif "good morning" in text:
            print("Good morning to you too")
            say()
        # Check if the user said "Good afternoon"
        elif "good afternoon" in text:
            print("Good afternoon to you too")
        # Check if the user said "Good evening"
        elif "good evening" in text:
            print("Good evening to you too")
        # Check if the user said "Good night"
        elif "good night" in text:
            print("Good night to you too")
        # Check if the user said "What is your name"
        elif "what is your name" in text:
            print("My name is TikTok")
        # Check if the user said "What is the date"
        elif "what is the date" in text:
            print("Today is " + str(datetime.date.today()))
        # Check if the user said "What is the time"
        elif "what is the time" in text:
            print("The time is " + str(datetime.datetime.now().strftime("%H:%M:%S")))
        # Check if the user said "What is the weather"
        elif "what is the weather" in text:
            print("The weather is " + str(requests.get("http://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22").json()["weather"][0]["description"]))
assistant()