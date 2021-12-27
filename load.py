import pyperclip
import shelve
import sys


def load(args):
    shelf = shelve.open('shelf')
    pyperclip.copy(args.key or shelf[sys.argv[1]])
    shelf.close()
