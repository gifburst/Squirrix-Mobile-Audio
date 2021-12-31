# lcom command listing utility

from lib.utils import *
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()



def _help():
    usage = '''Usage: help [options]

-h            Print this help
-a            Print all commands
              along with hidden ones.
-s (char)     Print commands starting
              with (char).'''
    talk(usage)


def main(argv):
    if '-h' in argv:
        _help()
        return

    f = get_func_list()

    # check if print hidden commands
    if '-a' in argv:
        argv.remove('-a')
        # append hidden commands
        H = ' <H>'
        f.append('set' + H)
        f.append('fwd' + H)
        # sort at last
        f.sort()

    if '-s' in argv:
        # The shell doesnt send the
        # command name in the arg list
        # so the next line is not needed
        # anymore
        # argv.pop(0)#remove com name
        argv.pop(0)  # remove arg
        try:
            arg = argv[0]
            if arg.isupper():
                arg = arg.lower()
            talk('Section:', arg.upper())
            for i in f:
                if i[0] == arg:
                    talk(i)
            return
        except IndexError:
            _help()
            return

    last = 'a'
    for i in f:
        if i[0] != last:
            last = i[0]
            talk('Section:', last.upper())
        talk(i)
