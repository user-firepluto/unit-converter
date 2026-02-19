#!/usr/bin/env python3.14
#main.py

import os
import calc

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

c = 'y'
while c == 'y':

    print('Unit Conversor 0.1\nType "help" to instructions, or "exit" to close the program\n')

    conv = str(input())

    if conv == 'mass':
        clear()
        calc.mass()

    if conv == 'help':
        clear()
        print('"mass" - convert mass\n"exit" to close the program')

    if conv == 'exit':
        clear()
        c = 'n'