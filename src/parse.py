from typing import Iterator

from numpy import int64

from var import *

if __name__ != "__main__":

    @dataclass
    class NumberNode:
        num: int

        def __post_init__(self):
            self.num = int64(self.num)

    class Parser:
        def __init__(self, tokens: Iterator) -> None:
            self.tokens = tuple(tokens)
            self.tokIdx = 1
            self.advance()

        def advance(self):
            self.tokIdx += 1
            if self.tokIdx < len(self.tokens):
                self.currentTok = self.tokens[self.tokIdx]
        
        def factor(self):
            if self.currentTok.ttype in (RULES['T_INT'].type, RULES['T_FLOAT'].type):
                self.advance()
                return NumberNode(self.currentTok)
        
        def term(self): 
            left = self.factor()

            while self.currentTok in (LITERALS['T_MUL', 'T_DIV']):
                opToken = self.currentTok
                right = self.factor()
            
            return BinOpNode(left, opToken, right)

