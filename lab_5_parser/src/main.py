# Тут підряд виконується:
# 1) читання граматики
# 2) FIRST
# 3) FOLLOW
# 4) LL(1)-таблиця
# 5) LL(1) стековий синтаксичний аналіз
# 6) рекурсивний синтаксичний аналіз + AST
# 7) побудова .dot та .png дерева
# python -m lab_5_parser.src.main

from lab_5_parser.src.ll1.first_follow import Grammar, compute_first, compute_follow
from lab_5_parser.src.ll1.ll1_table_parser import LL1TableParser
from lab_5_parser.src.ll1.recursive_parser import RecursiveParser

from lab_5_parser.src.visualize.render import render_ast


GRAMMAR_PATH = "lab_5_parser/grammar/expr.bnf"


def print_section(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def main():
    # ------------------------------------------------------------
    # 1. Читання граматики
    # ------------------------------------------------------------
    print_section("1. Читання граматики з expr.bnf")
    grammar = Grammar.from_bnf(GRAMMAR_PATH)
    print("Нетермінали:", grammar.nonterminals)
    print("Термінали:", grammar.terminals)
    print("Стартовий символ:", grammar.start_symbol)

    # ------------------------------------------------------------
    # 2. FIRST
    # ------------------------------------------------------------
    print_section("2. FIRST(1) для кожного нетермінала")
    FIRST = compute_first(grammar)
    for A, s in FIRST.items():
        print(f"FIRST({A}) = {s}")

    # ------------------------------------------------------------
    # 3. FOLLOW
    # ------------------------------------------------------------
    print_section("3. FOLLOW(1) для кожного нетермінала")
    FOLLOW = compute_follow(grammar, FIRST)
    for A, s in FOLLOW.items():
        print(f"FOLLOW({A}) = {s}")

    # ------------------------------------------------------------
    # 4. LL(1) таблиця
    # ------------------------------------------------------------
    print_section("4. Побудова LL(1)-таблиці синтаксичного аналізу")
    table_parser = LL1TableParser(grammar)
    table = table_parser.table

    for A in table:
        print(f"\n[A = {A}]")
        for a, rules in table[A].items():
            print(f"  M[{A}, {a}] = {rules}")

    # ------------------------------------------------------------
    # 5. LL(1) стековий парсер
    # ------------------------------------------------------------
    print_section("5. LL(1) стековий синтаксичний аналіз")
    tokens = ["id", "+", "id", "*", "id"]
    print("Вхідні токени:", tokens)

    parser = LL1TableParser(grammar)
    ok = parser.parse(tokens)

    print("Результат стекового аналізу:", "OK" if ok else "ERROR")

    # ------------------------------------------------------------
    # 6. Рекурсивний синтаксичний аналіз + AST
    # ------------------------------------------------------------
    print_section("6. Рекурсивний LL(1)-аналізатор (AST)")
    rparser = RecursiveParser(grammar)
    ast = rparser.parse(tokens)

    print("Отримане AST:")
    print(ast)

    # ------------------------------------------------------------
    # 7. Візуалізація AST через Graphviz
    # ------------------------------------------------------------
    print_section("7. Побудова AST → DOT → PNG")
    render_ast(ast, filename="example_ast")
    print("AST збережено у visualize/output/example_ast.png")


if __name__ == "__main__":
    main()