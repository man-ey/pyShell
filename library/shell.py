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
                if not (y.isdigit()) :
                    print('did not enter a number. Returning.')
                elif (int(y) - 1 < len(cmd)) :
                    print('the amendment/link?')
                    x = input('> ')
                    print(cmd[y][1] + x)
                    os.system(cmd[y][1] + x)
                else :
                    print('Not a listed option. Returning.')

            else :
                print('the amendment/link?')
                y = input('> ')
                print(cmd[0][1] + y)
                os.system(cmd[0][1] + y)

    elif x == 'delete' :
        print('Which command to delete?')
        y = input('> ')
        cmd = get_command(y)
        if (cmd) :
            print('Which command to delete?')
            print_commands(cmd)
            y = input('> ')
            if not (y.isdigit()):
                print('Did not enter a number. Returning.')
            elif (int(y) - 1 < len(cmd)) :
                delete_command(cmd[int(y) - 1])
            else :
                print('Not a listed option. Returning.')

    else:
        print('Unknown command')