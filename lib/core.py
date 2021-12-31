# CORE file contains main shell mechanisms
from importlib import import_module as _import
from time import sleep

from lib.utils import *
from lib.vfs import init
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

class shell():
    def __init__(self):
        init()

    def __repr__(self):
        return '<Shell Instance>'

    def get_input(self):
        if prop.get('prompt') != NULL:
            if prop.get('prompt') == '-def':
                sh = '@Squirrix/' + get_path() + '> '
            else:
                sh = prop.get('prompt') + ' '
        else:
            sh = '@Squirrix/' + get_path() + '> '
        inp = input(sh)
        return inp

    def execute(self, inp):
        inp = inp.split()
        # print(inp)
        inp = make_s(replace_vars(inp))
        inp = inp.split()
        # print(inp)
        # Get hidden commands as well
        f_list = get_func_list(True)

        try:
            f = inp[0]
            inp.pop(0)
        except IndexError:
            return
        if f in f_list:
            mod = 'bin.' + f
            m = _import(mod)
            try:
                m.main(inp)
            except TypeError:
                try:
                    m.main()
                except TypeError:
                    err(1)
            except AttributeError:
                err(1, f)
        elif f not in f_list:
            analyze(f)

    def start(self):
        print('Squirrix Mobile')
        talk('Squirrix Mobile')
        # write config file
        write_config()
        sleep(1)
        talk('Copyright (c) Squirrel Computers 2021\n')
        sleep (2)
        talk('Starting Squirrix Mobile\n')
        sleep(0.5)
        talk('Type "help" for help or type "lcom" to list every command...\n')
        while True:
            inp = self.get_input()
            self.execute(inp)
