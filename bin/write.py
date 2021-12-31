# write function
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
Usage: write (filename)

if (filename) exists inputs
will be appended else a new 
file will be created.

-h            Print this help
-r            Overwrite the 
              original file.
              All data is lost.

Use '%' in front of global
vars to use the value as
the file name.

While in write mode use
"-exit" to exit write mode
"-show" to see file contents
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

    # replace the vars
    # The shell does the work of replacing
    # vars already. Code segment below
    # is not required anymore.
    # argv = replace_vars(argv)

    if '-r' in argv:
        argv.pop(0)
        path = get_path() + make_s(argv)
        try:
            with open(path, 'w') as f:
                pass
            talk('Writing over "', make_s(argv), '" file', sep='')
        except IOError:
            err(3, add='Cant write into a directory')
            return

    path = get_path() + make_s(argv)
    s = 'write>'
    try:
        with open(path, 'a') as f:
            while True:
                inp = input(s)
                if '-exit' in inp:
                    break
                elif '-show' in inp:
                    f.close()
                    _show(path)
                    f = open(path, 'a')
                else:
                    print(inp, file=f)
    except IOError:
        err(3, add='Cant write into a directory')


def _show(path):
    with open(path) as f:
        data = f.readlines()
    talk('START\n')
    talk(make_s2(data))
    talk('END\n')
