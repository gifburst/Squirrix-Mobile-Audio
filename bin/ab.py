import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def main():
    talk("")
    talk("Squirrix Mobile Version 0.1")
    talk("Copyright (c) 2021 Squirrel Computers")
    talk("")
    talk("")
