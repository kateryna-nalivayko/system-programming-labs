from lab_5_parser.src.ll1.ast_builder import Number, BinaryOp, Paren


class DotGenerator:
    def __init__(self):
        self.counter = 0
        self.lines = ["digraph AST {", "    node [shape=oval];"]

    def _new_id(self):
        self.counter += 1
        return f"n{self.counter}"

    def generate(self, node):
        self._visit(node)
        self.lines.append("}")
        return "\n".join(self.lines)

    def _visit(self, node):
        nid = self._new_id()

        # Вузол числа
        if isinstance(node, Number):
            self.lines.append(f'    {nid} [label="{node.value}"];')
            return nid

        # Бінарна операція
        if isinstance(node, BinaryOp):
            self.lines.append(f'    {nid} [label="{node.op}"];')
            left = self._visit(node.left)
            right = self._visit(node.right)
            self.lines.append(f"    {nid} -> {left};")
            self.lines.append(f"    {nid} -> {right};")
            return nid

        # Дужки
        if isinstance(node, Paren):
            self.lines.append(f'    {nid} [label="()"];')
            child = self._visit(node.expr)
            self.lines.append(f"    {nid} -> {child};")
            return nid

        raise ValueError("Unknown node type")