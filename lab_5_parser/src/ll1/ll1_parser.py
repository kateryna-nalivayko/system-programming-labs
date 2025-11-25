from first_follow import Grammar
from ast_builder import Number, BinaryOp, Paren


class ParseError(Exception):
    """Помилка синтаксичного аналізу."""
    pass


class LL1Parser:
    """
    Рекурсивний LL(1)-парсер для граматики:

        E  → T E'
        E' → + T E' | ε
        T  → F T'
        T' → * F T' | ε
        F  → ( E ) | id
    """

    def __init__(self, grammar: Grammar):
        self.grammar = grammar
        self.tokens = []
        self.pos = 0

    # -----------------------------
    # Token API
    # -----------------------------
    def _peek(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def _consume(self, expected=None):
        tok = self._peek()
        if tok is None:
            raise ParseError(f"Неочікуваний кінець вводу, очікував {expected}")

        if expected is not None and tok != expected:
            raise ParseError(f"Очікував {expected}, отримав {tok}")

        self.pos += 1
        return tok

    # -----------------------------
    # Public parse entry
    # -----------------------------
    def parse(self, tokens):
        """
        tokens: ["id", "+", "id", "*", "id"]
        """
        self.tokens = tokens
        self.pos = 0

        node = self._parse_E()

        # Перевірка, що не лишилося зайвих токенів
        if self.pos != len(self.tokens):
            raise ParseError(
                f"Зайві токени після виразу: {self.tokens[self.pos:]}"
            )

        return node

    # -----------------------------
    # Grammar rules
    # -----------------------------
    # E → T E'
    def _parse_E(self):
        left = self._parse_T()
        return self._parse_Ep(left)

    # E' → + T E' | ε
    def _parse_Ep(self, left):
        while self._peek() == "+":
            self._consume("+")
            right = self._parse_T()
            left = BinaryOp("+", left, right)
        return left  # ε

    # T → F T'
    def _parse_T(self):
        left = self._parse_F()
        return self._parse_Tp(left)

    # T' → * F T' | ε
    def _parse_Tp(self, left):
        while self._peek() == "*":
            self._consume("*")
            right = self._parse_F()
            left = BinaryOp("*", left, right)
        return left  # ε

    # F → ( E ) | id
    def _parse_F(self):
        tok = self._peek()

        if tok == "id":
            self._consume("id")
            return Number("id")

        if tok == "(":
            self._consume("(")
            expr = self._parse_E()
            self._consume(")")
            return Paren(expr)

        raise ParseError(
            f"Неочікуваний токен {tok}, очікував 'id' або '('"
        )