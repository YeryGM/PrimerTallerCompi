class ASTNode:
    pass

class BinOp(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op  # e.g., '+', '*'
        self.right = right

class Assign(ASTNode):
    def __init__(self, var, expr):
        self.var = var  # ID (e.g., 'a')
        self.expr = expr  # Right-hand side (e.g., '3 + b')

class Number(ASTNode):
    def __init__(self, value):
        self.value = value

class Variable(ASTNode):
    def __init__(self, name):
        self.name = name