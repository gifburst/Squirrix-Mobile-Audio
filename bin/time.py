# time command prints current time
import time
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()



def main():
    time_stamp = time.strftime('%I:%M:%S %p')
    talk(time_stamp)
