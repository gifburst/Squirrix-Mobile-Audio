# test lock shell
from lib.pwd import chpwd, lock
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def _help():
    usage = '''
Usage: lock [options]
[options]:
-h            Print this help
-chpass       Change password
'''
    talk(usage)


def main(argv):
    if '-h' in argv:
        _help()
        return
    # The shell doesnt send the
    # command name in the arg list
    # so the next line is not needed
    # anymore
    # argv.pop(0)
    if '-chpass' in argv:
        chpwd()
        return
    lock()
