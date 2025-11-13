from dataclasses import dataclass
from typing import Any, Dict, List, Tuple


@dataclass
class AST:
    kind: str
    children: List["AST"]
    value: Any = None


def build_ast(tokens: List[Tuple[str, str]]) -> AST:
    pos = 0

    def peek():
        return tokens[pos] if pos < len(tokens) else ("EOF", "")

    def eat(expected: str) -> str:
        nonlocal pos
        t, v = peek()
        if t != expected:
            raise SyntaxError(f"Очікував {expected}, отримав {t}")
        pos += 1
        return v

    def factor() -> AST:
        t, v = peek()
        if t == "NUMBER":
            eat("NUMBER")
            return AST("Number", [], v)
        if t == "ID":
            eat("ID")
            return AST("Var", [], v)
        if t == "LPAREN":
            eat("LPAREN")
            node = expr()
            eat("RPAREN")
            return node
        raise SyntaxError(f"Неочікуваний токен у factor: {t}")

    def pow_expr() -> AST:
        left = factor()
        t, _ = peek()
        if t == "POW":
            eat("POW")
            right = pow_expr()  # Правоасоціативність: рекурсія вправо
            return AST("Pow", [left, right])
        else:
            return left

    def term() -> AST:
        node = pow_expr()
        while True:
            t, _ = peek()
            if t == "MULT":
                eat("MULT")
                node = AST("Mul", [node, pow_expr()])
            # Додавання підтримки ділення
            elif t == "DIV":
                eat("DIV")
                node = AST("Div", [node, pow_expr()])
            else:
                return node

    def expr() -> AST:
        node = term()
        while True:
            t, _ = peek()
            if t == "PLUS":
                eat("PLUS")
                node = AST("Add", [node, term()])
            else:
                return node

    # stmt
    name = eat("ID")
    eat("ASSIGN")
    rhs = expr()
    eat("SEMI")
    return AST("Assign", [AST("Var", [], name), rhs])


def eval_ast(node: AST, env: Dict[str, Any] | None = None) -> Any:
    env = env or {}
    k = node.kind
    if k == "Number":
        s = str(node.value)
        return float(s) if "." in s else int(s)
    if k == "Var":
        return env.get(node.value, 0)
    if k == "Add":
        return eval_ast(node.children[0], env) + eval_ast(node.children[1], env)
    if k == "Mul":
        return eval_ast(node.children[0], env) * eval_ast(node.children[1], env)
    if k == "Div":
        return eval_ast(node.children[0], env) / eval_ast(node.children[1], env)
    if k == "Pow":
        return eval_ast(node.children[0], env) ** eval_ast(node.children[1], env)
    if k == "Assign":
        name = node.children[0].value
        val = eval_ast(node.children[1], env)
        env[name] = val
        return val
    raise ValueError(f"Невідомий тип вузла: {k}")


def gen_python_code(node: AST) -> str:
    k = node.kind
    if k == "Number":
        return str(node.value)
    if k == "Var":
        return node.value
    if k == "Add":
        return f"({gen_python_code(node.children[0])} + {gen_python_code(node.children[1])})"
    if k == "Mul":
        return f"({gen_python_code(node.children[0])} * {gen_python_code(node.children[1])})"
    if k == "Div":
        return f"({gen_python_code(node.children[0])} / {gen_python_code(node.children[1])})"
    if k == "Pow":
        return f"({gen_python_code(node.children[0])} ** {gen_python_code(node.children[1])})"
    if k == "Assign":
        name = node.children[0].value
        rhs = gen_python_code(node.children[1])
        return f"{name} = {rhs}"
    raise ValueError(f"Невідомий тип вузла: {k}")
