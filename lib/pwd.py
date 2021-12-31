# for sleeping
# Password routines
import getpass
import hashlib
import pyttsx3
from time import sleep

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


key = 'lib/lock.key'


def chpwd():
    p = '''
Unlock the shell to prove authenticity.'''
    print(p)
    lock()
    talk('Authenticity Proved...')
    sleep(1)
    _reg_pass()


def lock():
    try:
        with open(key) as kw:
            data = kw.readline()
        p = '''The shell is LOCKED.'''
        print(p)
        inp = get_hash(getpass.getpass())
        if inp in data:
            return
        else:
            talk('\nIncorrect password !')
            lock()
    except IOError:
        p = '''
Registered password was not found.
Enter Password to register.
'''
        print(p)
        _reg_pass()
        talk('Now locking the shell...\n')
        lock()


def _reg_pass():
    p = '''
You wont be able to see what
you are typing.
'''
    talk(p)
    _pass = get_pass()
    with open(key, 'w') as kw:
        talk(_pass, sep='\n', file=kw)
    talk('\nPassword was registered...')


def get_pass():
    new_password = getpass.getpass('New Password: ')
    if len(new_password) < 4:
        p = '''Password must be atleast 4 characters long...
'''
        talk(p)
        return get_pass()
    confirm_password = getpass.getpass('Confirm Password: ')
    if new_password == confirm_password:
        pass_key = get_hash(new_password)
        return pass_key
    else:
        talk("Passwords entered doesn't match...")
        return get_pass()


def get_hash(_pass):
    _pass = bytes(_pass, 'utf-8')
    _hash = hashlib.new('sha1', _pass)
    _hash = _hash.hexdigest()
    return _hash
