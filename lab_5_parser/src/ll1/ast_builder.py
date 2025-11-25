class Number:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Number({self.value})"


class BinaryOp:
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def __repr__(self):
        return f"BinaryOp('{self.op}', {self.left}, {self.right})"


class Paren:
    def __init__(self, expr):
        self.expr = expr

    def __repr__(self):
        return f"Paren({self.expr})"