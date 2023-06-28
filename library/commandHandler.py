# commandHandler.py

import csv
from pathlib import Path

script_location = Path(__file__).absolute().parent
file_location = script_location / 'commands.csv'

commands = []

def load_commands() :
    commands.clear()
    with open(file_location, newline='') as csvfile:
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
        print('Command not found')
        return toReturn

def list_all() :
    load_commands()
    for cmd in commands :
        print(cmd)

def print_commands(commands_list) :
    counter = 1
    for cmd in commands_list :
        print(str(counter) + ' ' + cmd[counter - 1])
        counter += 1

def delete_command(command) :
    with open('library/commands.csv', 'r+') as csvfile :
        reader = csv.reader(csvfile)
        rows = [row for row in csv.reader(csvfile) if not ((command[0] in row) and (command[1] in row))]
        csvfile.seek(0)
        csvfile.truncate()
        writer = csv.writer(csvfile)
        writer.writerows(rows)
            


