"""
Basic CAT command.  Iterate through file names passed on the CLI and print
the contents of the files to stdout.
"""

import sys

args = sys.argv[1:]
while(args):
    # Pop front so files are printed in the order they appear on the CLI.
    arg = args.pop(0)
    try:
        with open(arg, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"Error: The file '{arg}' does not exist, aborting..")
        raise(SystemExit)
