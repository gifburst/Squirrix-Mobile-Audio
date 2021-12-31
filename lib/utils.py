# commons imports

import configparser as cp
import os
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


# String manipulators____________________
def make_s(l):
    __doc__ = '''
    Makes a sentence with spaces
    in between from a list of
    strings.
    returns a string.'''
    s = str()
    for i in l:
        s += i + ' '
    s = s[:-1]
    return s


def make_s2(l):
    __doc__ = '''
    Makes a sentence from a
    list of strings.
    returns a string.'''
    s = str()
    for i in l:
        s += i
    s = s[:-1]
    return s


# Error definitions______________________
def err(n, inp=None, add=None):
    # shell error
    if n == 0:
        if inp != None:
            talk('Error[0]: "', inp, '" was not recognised as a command or an expression', sep='')
        elif add != None:
            talk('Error[0]:', add)
        else:
            talk('Error[0]: invalid command or expression')
        return
    # shell error
    elif n == 1:
        if inp != None:
            talk('Error[1]: "', inp, '" command could not be executed', sep='')
        elif add != None:
            talk('Error[1]:', add)
        else:
            talk('Error[1]: command was not executed')
        return
    # path error
    elif n == 2:
        if inp != None:
            talk('Error[2]: "', inp, '" path does not exist', sep='')
        elif add != None:
            talk('Error[2]:', add)
        else:
            talk('Error[2]: invalid path')
        return
    # read write error
    elif n == 3:
        if inp != None:
            talk('Error[3]: "', inp, '" could not be opened', sep='')
        elif add != None:
            talk('Error[3]:', add)
        else:
            talk('Error[3]: file could not be read')
        return
    # Errors for set command
    elif n == 4:
        if inp != None:
            talk('Error[4]: undefined variable "', inp, '"', sep='')
        elif add != None:
            talk('Error[4]:', add)
        else:
            talk('Error[4]: undefined variable')
        return
    # prototype declaration
    elif n == 5:
        if inp != None:
            pass
        elif add != None:
            pass
        else:
            pass
        return
    else:
        talk('Invalid Error code')


# Manager functions______________________

# config path
c_path = 'lib/.configs'
NULL = 'NULL'


def get_func_list(hidden=False):
    func = os.listdir('bin/')
    f = list()
    for i in func:
        if isValid(i):
            continue
        f.append(i[:-3])
    # functions that are excepted
    # but should not be so append
    # them
    f.append('exit')
    f.append('help')
    f.append('mkdir')
    if hidden == True:
        # If hidden commands required
        # Append Hidden commands here
        f.append('set')
        f.append('fwd')
    return sorted(f)


class property_manager:
    def __init__(self, section):
        self.section = section

    def get(self, var):
        # universal get prop method
        config = cp.ConfigParser()
        config.read(c_path)
        if config.has_option(self.section, var):
            val = config.get(self.section, var)
            return val
        else:
            return NULL

    def set(self, var, val):
        # universal set prop method
        config = cp.ConfigParser()
        config.read(c_path)
        config.set(self.section, var, val)
        with open(c_path, 'w') as configs:
            config.write(configs)

    def vars(self):
        config = cp.ConfigParser()
        config.read(c_path)
        return config.options('Property')

    def delete(self, var):
        config = cp.ConfigParser()
        config.read(c_path)
        section = 'Property'
        if config.has_option(section, var):
            config.remove_option(section, var)
        with open(c_path, 'w') as configs:
            config.write(configs)

    def __repr__(self):
        return '<Property Manager>'


# Property manager instance
prop = property_manager('Property')


# algorithm to replace vars with values
def replace_vars(argv):
    if prop.get('c_char') != NULL:
        c_char = prop.get('c_char')
    else:
        c_char = '%'
    for i in range(len(argv)):
        var = argv[i]
        v = var.replace(c_char, '')
        if c_char in var and v in prop.vars():
            # talk(i, var, v)
            argv.pop(i)
            argv.insert(i, prop.get(v))
    return argv


def write_config():
    # built in check safe
    if '.configs' not in os.listdir('lib'):
        config = cp.ConfigParser()
        # path is reserved
        config['RESERVED'] = {'path': 'root/'}
        # global vars is property
        config['Property'] = {'save_state': '0'}
        with open(c_path, 'w') as configs:
            config.write(configs)


# Path functions_________________________

def get_path():
    __doc__ = '''
    Gets current path
    of the virtual file
    system.
    returns a string.'''
    prop = property_manager('RESERVED')
    path = prop.get('path')
    return path


def set_path(path):
    __doc__ = '''
    Sets current path
    of the virtual file system.
    returns None'''
    if path[-1] != '/':
        path += '/'
    prop = property_manager('RESERVED')
    prop.set('path', path)


def get_last_path(path):
    __doc__ = '''
    Gets the last path in
    the current directory.
    returns path as string'''
    last = str()
    ctr = 0
    i = 1
    if path[-1] != '/':
        path += '/'
    while ctr != 2:
        last += path[-i]
        if path[-i] == '/':
            ctr += 1
        i += 1
    last = last[:-1]
    last = make_s2(list(reversed(last)))
    return last


def get_prv_path():
    __doc__ = '''
    Gets the previous path
    of the current directory.
    returns path as a string.'''
    path = get_path()
    last = get_last_path(path) + '/'
    path = path[:-len(last)]
    return path


def get_prv_path2(path):
    __doc__ = '''
    Gets the previous path
    of the path given as argument.
    returns path as string.'''
    last = get_last_path(path) + '/'
    path = path[:-len(last)]
    return path


# Others_________________________________
def get_args(inp):
    __doc__ = '''
    Gets the arguments seperated
    by a space from a list.
    The argument input cannot have
    spaces in them for now.
    returns arguments as list.'''
    try:
        old = inp[0].replace(' ', '')
        old = inp[0].replace('"', '')
    except IndexError:
        talk('1st argument is missing')
        return []
    try:
        new = inp[1].replace(' ', '')
        new = inp[1].replace('"', '')
    except IndexError:
        talk('2nd argument is missing')
        return []
    return [old, new]


def isValid(inp):
    __doc__ = '''Checks for valid input'''
    exceptsFile = 'lib/.exception'
    with open(exceptsFile) as exc:
        excepts = exc.readlines()
    for i in excepts:
        # talk(r'%s'%i)
        if i[:-1] in inp:
            return True
    return False


def analyze(inp):
    __doc__ = '''
    Basic function to analyze
    the input for other expressions
    returns None'''
    # The shell doesnt send the command
    # name in arg list anymore
    # so next line is not required
    # inp=make_s(inp)
    # print(inp)
    # check if is a directory
    if os.path.isdir(get_path() + inp):
        if '.' in inp:
            err(0, inp)
            return
        talk('"', inp, '" is a directory', sep='')
        return
    elif os.path.isfile(get_path() + inp):
        talk('"', inp, '" is a file', sep='')
        return
    # check if is a valid input
    if isValid(inp) or 'inp' in inp:
        err(0, inp)
        return

    try:
        exec('from math import *')
        # math func inp catcher
        # to prevent builtins msg disp
        if inp in dir():
            talk('"', inp, '" is a mathematical function', sep='')
            return
        # add true and false
        exec('true,false=True,False')
        # math func lister__________
        if inp == '--math':
            d = dir()
            d.remove('__doc__')
            d.remove('inp')
            for i in sorted(d):
                print(i)
            return
        e = eval(inp)
        if e != None:
            print(e)
    except SyntaxError:
        talk("Couldn\'t evaluate the expression")
    except NameError as e:
        err(0, inp)
    except ZeroDivisionError:
        talk('Cannot divide by zero')
    except TypeError as e:
        talk(e)
    except ValueError as e:
        talk(e)
    except AttributeError as e:
        talk(e)
