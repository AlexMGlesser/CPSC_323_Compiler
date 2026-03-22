import re

class TokenType:
    EOF = "EOF"
    IDENTIFIER = "IDENTIFIER"
    NUMBER = "NUMBER"
    # Define other tokens (e.g., PLUS, MINUS, etc.)

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {self.value})"

class Scanner:
    def __init__(self, source):
        self.source = source
        self.tokens = []
        self.start = 0
        self.current = 0

    def scan_tokens(self):
        while not self.is_at_end():
            self.advance()
        self.tokens.append(Token(TokenType.EOF, ""))
        return self.tokens

    def advance(self):
        self.current += 1
        return self.source[self.current - 1]

    def is_at_end(self):
        return self.current >= len(self.source)