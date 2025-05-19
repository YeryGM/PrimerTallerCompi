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


def print_ast(node, indent=0):
    indent_str = '  ' * indent
    if isinstance(node, Assign):
        print(f"{indent_str}Assign:")
        print(f"{indent_str}  var: {node.var.name}")
        print(f"{indent_str}  expr:")
        print_ast(node.expr, indent + 2)
    elif isinstance(node, BinOp):
        print(f"{indent_str}BinOp({node.op}):")
        print_ast(node.left, indent + 1)
        print_ast(node.right, indent + 1)
    elif isinstance(node, (Number, Variable)):
        print(f"{indent_str}{type(node).__name__}({node.value if isinstance(node, Number) else node.name})")

