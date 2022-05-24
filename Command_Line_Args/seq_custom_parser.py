# Unix SEQ clone.
# Replace regex with custom parser

import collections
import sys

from typing import List, Tuple

USAGE = (
    f"Usage: {sys.argv[0]} [-s seperator] [first [increment]] last"
)

def parse(args: List[str]) -> Tuple[str, List[str]]:
    arguments = collections.deque(args)
    sep = '\n'
    operands = []
    while arguments:
        current_arg = arguments.popleft()
        if len(operands) == 0:
            if current_arg in ["-h", "--help"]:
                print(USAGE)
                sys.exit(0)
            if current_arg in ["-s", "--seperator"]:
                sep = arguments.popleft()
                continue
        try:
            operands.append(int(current_arg))
        except ValueError:
            raise SystemExit(USAGE)

        if len(operands) > 3:
            raise SystemExit(USAGE)
    return sep, operands

def seq(operands: List[int], sep: str) -> str:
    first, inc, last = 1, 1, 1
    if len(operands) == 1:
        last = operands[0]
    if len(operands) == 2:
        first, last = operands
        if first > last:
            inc = -1
    if len(operands) == 3:
        first, inc, last = operands

    last = last + 1 if inc > 0 else -1
    return sep.join(str(i) for i in range(first, last, inc))


def main() -> None:
    sep, operands = parse(sys.argv[1:])
    if not operands:
        raise(SystemExit(USAGE))
    print(seq(operands, sep))


if __name__ == '__main__':
    main()
