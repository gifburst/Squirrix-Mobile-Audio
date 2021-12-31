# clear screen command
from os import system
from platform import system as sysname
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()



def _help():
    usage = '''
Usage: clear'''
    talk(usage)


def main():
    system_name = sysname()
    if system_name == 'Windows':
        system('cls')
    elif system_name == 'Linux':
        system('clear')
    return
