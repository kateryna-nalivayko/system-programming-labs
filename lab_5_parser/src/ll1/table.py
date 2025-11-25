# Побудова LL(1)-таблиці: M[A][a] = список продукцій A → α.
# Якщо граматика LL(1), то в кожній комірці таблиці буде максимум одна продукція.

from collections import defaultdict
from first_follow import EPS


def build_ll1_table(grammar, FIRST, FOLLOW):
    """
    Будує таблицю LL(1) для заданої граматики.
    """

    M = {A: defaultdict(list) for A in sorted(grammar.nonterminals)}

    for A in sorted(grammar.nonterminals):
        for alpha in grammar.productions[A]:

            # Обчислюємо FIRST(alpha)
            first_alpha = set()
            nullable = True

            for X in alpha:
                first_alpha |= (FIRST[X] - {EPS})
                if EPS not in FIRST[X]:
                    nullable = False
                    break

            # FIRST(alpha) → таблиця
            for a in first_alpha:
                M[A][a].append(alpha)

            # Якщо α може породжувати ε → додаємо FOLLOW(A)
            if nullable:
                for b in FOLLOW[A]:
                    M[A][b].append(alpha)

    return M


def print_ll1_table(M):
    """Друк LL(1)-таблиці."""
    all_terminals = sorted({t for row in M.values() for t in row.keys()})

    print("LL(1) TABLE:")
    print("".ljust(10), *[t.rjust(10) for t in all_terminals])

    for A in sorted(M.keys()):
        row = M[A]
        line = A.ljust(10)

        for t in all_terminals:
            if t in row:
                rules = [" ".join(prod) for prod in row[t]]
                line += (" " + str(rules)).rjust(11)
            else:
                line += " ".rjust(11)

        print(line)