from A_Sintactico.AST import Assign, BinOp, Number, Variable

class TACGenerator:
    def __init__(self):
        self.temp_count = 0
        self.code = []

    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"

    def generate(self, node):
        if isinstance(node, Number):
            return node.value
        elif isinstance(node, Variable):
            return node.name
        elif isinstance(node, BinOp):
            left = self.generate(node.left)
            right = self.generate(node.right)
            temp = self.new_temp()
            self.code.append((node.op, left, right, temp))
            return temp
        elif isinstance(node, Assign):
            expr_result = self.generate(node.expr)
            self.code.append(('=', expr_result, None, node.var.name))
            return None

    def get_tac(self):
        return self.code

def print_tac(tac):
    for op, left, right, result in tac:
        if op == '=':
            print(f"{result} = {left}")
        else:
            print(f"{result} = {left} {op} {right}")
