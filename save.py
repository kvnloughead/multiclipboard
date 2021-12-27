import pyperclip
import shelve
import sys


def save(args):
    shelf = shelve.open('shelf')
    shelf[args.key] = pyperclip.paste()
    shelf.close()
