# mkdir command

from lib.utils import *
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()



def main(argv):
    if len(argv) < 1 or '-h' in argv:
        _help()
        return
    # The shell doesnt send the
    # command name in the arg list
    # so the next line is not needed
    # anymore
    # argv.pop(0)

    # The shell does the work of replacing
    # vars already. Code segment below
    # is not required anymore.
    # argv=replace_vars(argv)

    if make_s(argv) in ('.', '..', '-'):
        err(2, add='invalid directory name')
        return
    path = get_path() + make_s(argv)
    try:
        if os.listdir(path[:-len(os.path.basename(path))]) in (os.listdir('lib'), os.listdir('bin'), os.listdir()):
            err(2)
            return
    except:
        pass

    try:
        os.mkdir(path)
    except OSError:
        talk('"', argv[0], '" directory already exsists', sep='')
        return
    talk('"', argv[0], '" directory created', sep='')
    # talk('Path:',path)


def _help():
    usage = '''Usage: mkdir (dir)
    
Where (dir) is the
    name of the new
    directory to be
    created.

Use '%' in front of
global vars to use
their value as dir name.
'''
    talk(usage)
