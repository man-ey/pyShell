# shell.py

import os
from commandHandler import *

available_commands = ['help', 'add', 'use link', 'list', 'quit']


while 1:
    x = input('> ')
    
    if x == 'quit':
        break

    elif x == 'help':
        print(available_commands)

    elif x == 'list':
        list_all()

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

    elif x == 'use link' :
        print('which command?')
        y = input('> ')
        cmd = get_command(y)
        if (cmd) :
            if (len(cmd) > 1) :
                print_commands(cmd)
                print('Which command? Enter the number')
                y = input('> ')
                if (int(y) < len(cmd)) :
                    print('the amendment?')
                    x = input('> ')
                    os.system(cmd[y][1] + ' ' + x)
                else :
                    print('Not a listed option')

            else :
                print('the amendment?')
                y = input('> ')
                print(cmd[0][1])
                os.system(cmd[0][1] + ' ' + y)

    else:
        print('Unknown command')