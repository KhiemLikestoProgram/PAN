from typing import Any

from var import *

class PanError:
    def __init__(self, type: Any, message: str, pos: Position) -> None:
        c.print(f"[white]At [#40e540]{pos.fn}:[blue]{pos.ln}:[yellow]{pos.col}[/][/][/]:")
        c.print(f"[bold italic #e98f8f]{type}[/][white]: {message}[/]")

class PanSyntaxError(PanError):
    def __init__(self, message: str, pos: Position) -> None:
        super().__init__(self.__name__, message, pos)

if __name__ == '__main__':
    PanError('ErrorTypeHere', 'Error message here.', Position('some/path/to/file.txt', 12, 41))