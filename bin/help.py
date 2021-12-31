# Help function
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


u = '''
[help]
 To list available commands 
   use "lcom" command

 For extra info and help on
   particular commands type
   "-h" after you command, e.g "(command)
    -h". If help is
   available, it will be shown.

 Enter mathematical
   expressions directly into the
   shell to evaluate them. Also
   you can issue a special keyword
   "--math" to list the supported 
   mathematical functions.

Issue "exit" to exit the shell
'''

v = '''
[version]
v0.1
'''

i = '''
[About]
Squirrix Mobile is a Mobile Operating enviroment
for the ChipLet computer
'''

h = '''Usage: help [options]

[options]:

-help         Print help
-i            Print info
-v            Print version
-h            Print this msg
'''


def main(argv):
    # help gets an empty argv,
    # shell doesnt send the
    # comm name anymore
    if '-h' in argv:
        talk(h)
        return
    if '-v' in argv:
        talk(v)
        return
    if '-i' in argv:
        talk(i)
        return
    if '-help' in argv:
        talk(u)
        return
    talk(i, u, v)
