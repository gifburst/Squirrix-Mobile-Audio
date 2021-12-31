# date command prints date

import time
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()



def main():
    time_stamp = time.strftime('%A, %d %B %Y')
    talk(time_stamp)
