from dataclasses import dataclass
from pathlib import Path
from types import SimpleNamespace

from rich.console import Console
c = Console()

IGNORE = ' \t'
RULES  = {
    "T_STR": {
        "type": "STR",
        "regex": r'".*?"|\'.*?\''
    },
    "T_INT": {
        "type": "INT",
        "regex": r"(?<![.0-9])(\d+)(?![.0-9])"
    },
    "T_FLOAT": {
        "type": "FLOAT",
        "regex": r"\d*\.\d+"
    },
}
LITERALS = [
    ("T_PLUS", "+"),
    ("T_MINUS", "-"),
    ("T_MUL", "*"),
    ("T_DIV", "/"),
    ("T_LPAREN", "("),
    ("T_RPAREN", ")"),
]


for t in RULES:
    RULES[t] = SimpleNamespace(type=RULES[t]['type'], regex=RULES[t]['regex'])
for i, t in enumerate(LITERALS):
    LITERALS[i] = SimpleNamespace(type=t[0], char=t[1])

@dataclass
class Position:
    fn: Path
    ln: int
    col: int
