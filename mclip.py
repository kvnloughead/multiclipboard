#! /usr/bin/python3

# mcb.py - Saves and loads pieces of text to the clipboard

# Usage: `WindowsKey + r` and then type `mc [args]`
#         mc save <keyword> - Saves clipboard to keyword
#         mc <keyword> - Loads keyword to clipboard
#         mc list_ - Loads all keywords to clipboard

import argparse
import shelve
import pyperclip
import sys

from save import save
from list_ import list_
from load import load

parser = argparse.ArgumentParser()

subparsers = parser.add_subparsers(
    title="subcommands", description="", help="-"*10)

save_parser = subparsers.add_parser(
    "save",
    aliases=["s"],
    help="`mc save foo` saves the current clipboard content with the key")
save_parser.add_argument(
    "key", nargs="?", help="the key to associate with the current clipboard content")
save_parser.set_defaults(func=save)

list_parser = subparsers.add_parser(
    "list",
    aliases=["l"],
    help="loads list of all saved keys to clipboard")
list_parser.set_defaults(func=list_)

load_parser = subparsers.add_parser(
    "load",
    help="`mc load foo` or `mc foo` loads `shelf[foo]` to the clipboard. No alias but the empty alias.")
load_parser.add_argument(
    "key", nargs="?", help="the lookup key"
)
load_parser.set_defaults(func=load)

args = parser.parse_args(['load'] if len(sys.argv) == 2 else None)

if not "func" in args:
    parser.print_help()
    sys.exit()
else:
    args.func(args)
