# commandHandler.py

import csv

commands = []

def load_commands() :
    commands.clear
    with open('library/commands.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar = '|')
        for row in reader:
            commands.append(row)

def add_command(cmdName, cmd) :
    if check_existence(cmdName, cmd):
        print('Command already saved')
    else :
        with open('library/commands.csv', 'a+', newline='') as writeobj:
            csvwriter = csv.writer(writeobj)
            csvwriter.writerow((cmdName + ',' + cmd).split(','))
            writeobj.close

def check_existence(cmdName, cmd) :
    load_commands()
    if ([cmdName, cmd]) in commands:
        print('true')
        return True
    else: return False

def get_command(cmdName) :
    load_commands()
    toReturn = []
    for cmd in commands :
        if cmdName in cmd: 
            toReturn.append(cmd)
    if len(toReturn) > 0:
        return toReturn
    else :
        print('Command title not found')

def list_all() :
    load_commands()
    return commands

