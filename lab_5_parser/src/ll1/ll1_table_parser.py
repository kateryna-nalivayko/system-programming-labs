# Стековий LL(1) синтаксичний аналізатор.
# Використовує таблицю M[A][a] із table.py
# Ця версія робить лише перевірку синтаксису — без побудови AST.
# Робота виконується відповідно до класичного алгоритму LL(1).

from lab_5_parser.src.ll1.first_follow import Grammar, EPS
from lab_5_parser.src.ll1.table import build_ll1_table


class ParseError(Exception):
    pass


class LL1TableParser:
    """
    Проста реалізація стекового LL(1)-парсера.
    Принцип роботи:
      - маємо стек символів (нетермінали і термінали)
      - читаємо вхідні токени
      - термінали мають збігатися з токенами
      - нетермінали розгортаються за таблицею LL(1)
    """

    def __init__(self, grammar: Grammar):
        self.grammar = grammar

        # Обчислюємо FIRST/FOLLOW
        from lab_5_parser.src.ll1.first_follow import compute_first, compute_follow
        self.FIRST = compute_first(grammar)
        self.FOLLOW = compute_follow(grammar, self.FIRST)

        # Будуємо LL(1)-таблицю
        self.table = build_ll1_table(grammar, self.FIRST, self.FOLLOW)

        self.tokens = []
        self.pos = 0

    # -----------------------------------------
    # Робота з токенами
    # -----------------------------------------
    def _peek(self):
        """Повертає поточний токен без зсуву."""
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def _consume(self, expected):
        """З'їдає токен, якщо він збігається з expected."""
        tok = self._peek()
        if tok != expected:
            raise ParseError(f"Очікував {expected}, отримав {tok}")
        self.pos += 1

    # -----------------------------------------
    # Основна функція розбору
    # -----------------------------------------
    def parse(self, tokens):
        """
        Повертає True, якщо синтаксичний аналіз успішний.
        tokens: список токенів (наприклад ["id", "+", "id"])
        """
        self.tokens = tokens + ["$"]
        self.pos = 0

        # Стек LL(1)
        stack = ["$", self.grammar.start_symbol]

        while True:
            top = stack.pop()
            current = self._peek()

            # -------------------------------
            # 1) Термінал
            # -------------------------------
            if top in self.grammar.terminals or top == "$":
                if top == current:
                    self._consume(current)
                    if top == "$":
                        return True
                else:
                    raise ParseError(f"Очікував {top}, отримав {current}")
                continue

            # -------------------------------
            # 2) Нетермінал
            # -------------------------------
            if current not in self.table[top]:
                raise ParseError(
                    f"Помилка у нетерміналі {top}: немає правила для токена {current}"
                )

            production = self.table[top][current][0]

            # Якщо правило = ε → нічого не додаємо в стек
            if production == [EPS]:
                continue

            # Додаємо тіло правила у зворотному порядку
            for symbol in reversed(production):
                stack.append(symbol)