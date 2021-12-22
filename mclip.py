#! /usr/bin/python3

import sys
import pyperclip

# dictionary of phrases
store = {'agree': """Yes, I agree. That sounds fine to me.""",
         'busy': """Sorry, can we do this later this week or next week?""",
         'upsell': """Would you consider making this a monthly donation?"""}


if len(sys.argv) < 2:
    print('Usage: python mclip.py <key>')
    sys.exit()

key = sys.argv[1]
if key in store:
    pyperclip.copy(store[key])
    print('Text for ' + key + ' copied to clipboard.')
else:
    print('No such key')
