import pyperclip
import shelve


def list_(args):
    shelf = shelve.open('shelf')
    pyperclip.copy(str(list(shelf.keys())))
    shelf.close()
