import sys
from pathlib import Path

from lex import Lexer
from parse import Parser


def main() -> None:
    if len(sys.argv) < 2:
        print('Missing file name.')
        sys.exit(1)

    FILE = Path(sys.argv[1]).absolute()
    if FILE.exists(): FILE.resolve()
    else:
        print(f'"{FILE.absolute()}" does NOT exist.')
        sys.exit(1)

    tokens = iter(Lexer(FILE))
    for t in tokens:
        print(t, t.__class__.__name__)
    Parser(tokens)


if __name__ == "__main__":
    main()
