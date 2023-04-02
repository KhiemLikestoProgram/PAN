if __name__ != "__main__":
    import re
    import sys
    from pathlib import Path
    from typing import Any

    from var import *
    
    @dataclass # taken from var
    class Token:
        tspan: tuple
        ttype: str
        tvalue: Any = None

        def __repr__(self) -> str:
            if self.tvalue is None:
                return f"Token(tspan={self.tspan}, ttype={self.ttype!r})"
            else: 
                return f"Token(tspan={self.tspan}, ttype={self.ttype!r}, tvalue={self.tvalue})"

    class Lexer:
        def __init__(self, file: Path) -> None:
            self.txt = file.read_text("utf-8").splitlines()
            self.pos = Position(ln=1, col=0, fn=file)
            self.currentLine: str = None
            
            regexparts = [r'(?P<%s>%s)' % (t, RULES[t].regex) for t in RULES]
            self.regex = re.compile('|'.join(regexparts))
        
        def advance(self):
            if self.pos.ln-1 < len(self.txt):
                self.currentLine = self.txt[self.pos.ln-1]
                self.pos.ln += 1
                self.pos.col = 0
            else:
                self.currentLine = None
                raise EOFError

        def __iter__(self):
            self.advance()
            while self.currentLine != None:
                if self.pos.col >= len(self.currentLine):
                    try:
                        self.advance()
                    except EOFError:
                        break

                currentChar = self.currentLine[self.pos.col]
                
                # For literals that are 2 characters more -- OR -- patterns.
                m = self.regex.match(string=self.currentLine, pos=self.pos.col)
                if m:
                    tok = Token(
                                tspan=m.span(),
                                ttype=RULES[m.lastgroup].type, 
                                tvalue=m.group(m.lastgroup)
                               )
                    self.pos.col = m.end()
                    yield tok

                # For single character literals (builtin `in` Python keyword is faster than RegEx).
                elif currentChar in [t.char for t in LITERALS]:
                    pstart = self.pos.col
                    pend = pstart + len(currentChar)

                    tok = Token(
                                tspan=(pstart, pend),
                                ttype=[t.type for t in LITERALS if t.char == currentChar][0]
                               )
                    self.pos.col += 1
                    yield tok

                elif currentChar in IGNORE: self.pos.col += 1

                else:
                    print('Invalid character: "%s" [temp].' % self.currentLine[self.pos.col])
                    sys.exit(2)
