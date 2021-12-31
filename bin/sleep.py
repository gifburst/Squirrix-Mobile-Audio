# sleep command
from time import sleep

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
Usage: sleep (int)

shell sleeps for (int) time
in seconds

-h            Print this help
'''
    talk(usage)


def main(argv):
    if len(argv) < 1 or '-h' in argv:
        _help()
        return
    # The shell doesnt send the
    # command name in the arg list
    # so the next line is not needed
    # anymore
    # argv.pop(0)
    try:
        t = int(make_s(argv))
        sleep(t)
    except ValueError:
        talk('"', make_s(argv), '" is not a valid time interval', sep='')
