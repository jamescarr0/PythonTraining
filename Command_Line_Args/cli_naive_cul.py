# cul.py
'''
This simple (naive) CLI takes in any number of arguments along with 
one of three options, -c, -u, and -l.
It then prints the arguments in one of the following forms
-c      Capitalized
-u      UPPERCASE
-l      lowercase
-D      debug
'''

import sys

options =   [opt for opt in sys.argv[1:] if opt.startswith("-")]
args =      [opt for opt in sys.argv[1:] if not opt.startswith("-")]

if "-D" in options:
    print("Debug Output")
    print(f"Options: {options}")
    print(f"Args: {args}")

if "-c" in options:
    print(" ".join([arg.capitalize() for arg in args]))
elif "-u" in options:
    print(" ".join([arg.upper() for arg in args]))
elif "-l" in options:
    print(" ".join([arg.lower() for arg in args]))
else:
    raise SystemExit(f"Usage: {sys.argv[0]} (-c | -u | -l) <arguments>...")