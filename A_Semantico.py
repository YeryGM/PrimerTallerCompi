from A_Sintactico.AST import Assign, BinOp, Number, Variable

symbol_table = {'b': 'int'}  # Pretend 'b' is declared

def validate_semantics(node):
    if isinstance(node, Variable):
        if node.name not in symbol_table:
            raise NameError(f"Undeclared variable: {node.name}")
    elif isinstance(node, BinOp):
        validate_semantics(node.left)
        validate_semantics(node.right)
    elif isinstance(node, Assign):
        validate_semantics(node.expr)
        symbol_table[node.var.name] = 'int'  # Mock type assignment