import re

# Token types
tokens = ['ID', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS', 'LPAREN', 'RPAREN', 'SEMI']

# Regex rules (order matters!)
token_specs = [
    ('NUMBER',   r'\d+(\.\d+)?'),     # Integers or floats
    ('ID',       r'[a-zA-Z_]\w*'),    # Variables
    ('PLUS',     r'\+'),              # Operators
    ('MINUS',    r'-'),
    ('TIMES',    r'\*'),
    ('DIVIDE',   r'/'),
    ('EQUALS',   r'='),
    ('LPAREN',   r'\('),
    ('RPAREN',   r'\)'),
    ('SEMI',     r';'),
    ('SKIP',     r'[ \t\n]'),         # Ignored characters
    ('ERROR',    r'.'),               # Catch-all for errors
]

# Build the lexer regex
token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specs)
lexer = re.compile(token_regex)

def tokenize(code):
    pos = 0
    while pos < len(code):
        match = lexer.match(code, pos)
        if not match:
            raise SyntaxError(f"Unknown character at position {pos}: '{code[pos]}'")
        
        token_type = match.lastgroup
        value = match.group(token_type)
        
        if token_type == 'NUMBER':
            value = float(value) if '.' in value else int(value)
        elif token_type == 'SKIP':
            pos = match.end()  # Skip whitespace
            continue
        elif token_type == 'ERROR':
            raise SyntaxError(f"Illegal character: '{value}'")
        
        yield (token_type, value)
        pos = match.end()

# Example usage
code = "a = 3 + b * 2;"
for token in tokenize(code):
    print(token)