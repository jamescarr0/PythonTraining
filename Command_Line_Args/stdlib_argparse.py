# Example program experimenting with argparse.
# Basic CLI.  Prints help, version and simply iterates through the file names passed to it

import argparse

def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        usage="%(prog)s <OPTIONS> [FILES]",
        description="Nothing to see, just playing around with CLI and stdlib argparse" 
    )
    parser.add_argument("-v", "--version", action="version", version=f"{parser.prog} v1.0.0")
    parser.add_argument("files", nargs="*") # Any number of files
    return parser

parser = init_argparse()
args = parser.parse_args()

if not args.files:
    print(parser.print_help())

count = 1
print("You passed the following file arguments...")
for arg in args.files:
    print(f"file {count}:> {arg}")
    count+=1