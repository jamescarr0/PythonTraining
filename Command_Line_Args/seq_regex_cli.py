# Unix SEQ clone.

import re
import sys

from typing import Dict, List

USAGE = (
    f"Usage: {sys.argv[0]} [-s seperator] [first [increment]] last"
)

args_pattern = re.compile(
    r"""
    ^
    (
        (--(?P<HELP>help).*)|
        ((?:-s|--separator)\s(?P<SEP>.*?)\s)?
        ((?P<OP1>-?\d+))(\s(?P<OP2>-?\d+))?(\s(?P<OP3>-?\d+))?
    )
    $
""",
    re.VERBOSE,
)


def parse(arg_line: str) -> Dict[str, str]:
    args: Dict[str, str] = {}
    if match_object := args_pattern.match(arg_line):
        args = {k: v for k, v in match_object.groupdict().items()
                if v is not None}
    return args


def seq(operands: List[int], sep: str = "\n") -> str:
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
    args = parse(" ".join(sys.argv[1:]))
    if not args:
        raise SystemExit(USAGE)
    if args.get("HELP"):
        print(USAGE)
        return
    operands = [int(v) for k, v in args.items() if k.startswith("OP")]
    sep = args.get("SEP", "\n")
    print(seq(operands, sep))


if __name__ == '__main__':
    main()
