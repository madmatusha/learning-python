#!/usr/bin/env python

def select_command(command):
    match command:
        case 'Menu':
            print('Menu')
        case 'Help':
            print('Help')
        case 'Exit':
            print('Exit')
            exit(0)
        case _:
            print('Unknown command')

while True:
    command = input()
    select_command(command)
