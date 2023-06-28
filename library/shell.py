# shell.py

import subprocess
from commandHandler import *

available_commands = ['help', 'list' 'quit']


while 1:
    x = input('> ')
    
    if x == 'quit':
        break

    elif x == 'help':
        print(available_commands)

    elif x == 'list':
        print(list_all())

    elif x == 'add':
        print('Title of the new command?')
        y = input('> ')
        print('Enter the command:')
        x = input('> ')
        add_command(y, x)
    
    elif x == 'use':
        print('which command?')
        y = input('> ')
        print(get_command(y))

    else:
        print('Unknown command')