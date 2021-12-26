#! /usr/bin/python3

# mcb.py - Saves and loads pieces of text to the clipboard

# Usage: py.exe mc.py save <keyword> - Saves clipboard to keyword
#        py.exe mc.py <keyword> - Loads keyword to clipboard
#        py.exe mc.py list - Loads all keywords to clipboard

import shelve
import pyperclip
import sys

shelf = shelve.open('mc')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    shelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(shelf.keys())))
    else:
        pyperclip.copy(shelf[sys.argv[1]])
shelf.close()
