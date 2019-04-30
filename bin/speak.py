# speak command speak input
import time

from lib.utils import *


def _help():
    usage = '''
Usage: speak <string>

-h            Print this help
-t            Speak system time
-d            Speak system date
'''
    print(usage)


def main(argv):
    try:
        import sl4a
    except ImportError:
        print('This feature is not available')
        return

    if len(argv) < 1 or '-h' in argv:
        _help()
        return
    # The shell doesnt send the
    # command name in the arg list
    # so the next line is not needed
    # anymore
    # argv.pop(0)
    arg = make_s(argv)

    if '-t' in argv:
        arg = time.strftime('%I %M %p')
    if '-d' in argv:
        arg = time.strftime('%A, %d %B %Y')

    droid = sl4a.Android()
    # print(arg)
    droid.makeToast('Speaking...')
    droid.ttsSpeak(arg)
