from .AST import Assign, BinOp, Number, Variable

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_token = self.tokens[self.pos] if tokens else None

    def advance(self):
        self.pos += 1
        self.current_token = self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def parse(self):
        return self.assignment()

    def assignment(self):
        """Parse assignments: ID = expr;"""
        var = Variable(self.current_token[1])
        self.advance()  # Consume ID
        self.advance()  # Consume '='
        expr = self.expr()
        return Assign(var, expr)

    def expr(self):
        """Parse expressions: term ((PLUS|MINUS) term)*"""
        node = self.term()
        while self.current_token and self.current_token[0] in ('PLUS', 'MINUS'):
            op = self.current_token[1]
            self.advance()
            node = BinOp(node, op, self.term())
        return node

    def term(self):
        """Parse terms: factor ((TIMES|DIVIDE) factor)*"""
        node = self.factor()
        while self.current_token and self.current_token[0] in ('TIMES', 'DIVIDE'):
            op = self.current_token[1]
            self.advance()
            node = BinOp(node, op, self.factor())
        return node

    def factor(self):
        """Parse factors: NUMBER | ID | ( expr )"""
        token = self.current_token
        if token[0] == 'NUMBER':
            self.advance()
            return Number(token[1])
        elif token[0] == 'ID':
            self.advance()
            return Variable(token[1])
        elif token[0] == 'LPAREN':
            self.advance()
            node = self.expr()
            if self.current_token[0] != 'RPAREN':
                raise SyntaxError("Expected ')'")
            self.advance()
            return node
        else:
            raise SyntaxError(f"Unexpected token: {token[0]}")