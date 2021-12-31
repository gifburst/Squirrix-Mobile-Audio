# ren rename command
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
Usage: ren (old) (new)

(old)=> old name of file/directory
(new)=> new name of file/directory

-h            Print this help
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
    args = get_args(argv)
    # The shell does the work of replacing
    # vars already. Code segment below
    # is not required anymore.
    # args=replace_vars(args)
    # print(args)
    if len(args) < 2:
        _help()
        return
    old = get_path() + args[0]
    new = get_path() + args[1]
    try:
        os.rename(old, new)
    except OSError:
        err(2, add=old + ' not found')
