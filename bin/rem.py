# rem remarks
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def _help():
    usage = '''
Usage: rem <remarks>

-h            print this help
'''
    talk(usage)


def main(argv):
    # rem just checked for -h
    # argv.pop(0) was never required
    if '-h' in argv:
        _help()
