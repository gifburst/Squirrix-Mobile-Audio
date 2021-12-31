# forward commands to the host system
from lib.utils import *
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()



def _help():
    usage = '''
Usage: fwd (command)

Where command is a valid
host system command.
'''
    talk(usage)


def main(argv):
    if len(argv) == 0 or '-h' in argv:
        _help()
        return

    from os import system
    system(make_s(argv))
