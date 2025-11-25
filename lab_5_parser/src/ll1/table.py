from collections import defaultdict
from first_follow import EPS

def build_ll1_table(grammar, FIRST, FOLLOW):
    """
    Побудова таблиці LL(1) для граматики:
    M[A][a] = A → α  (продукція)
    """

    M = {A: defaultdict(list) for A in sorted(grammar.nonterminals)}

    for A in sorted(grammar.nonterminals):
        for alpha in grammar.productions[A]:

            # 1. FIRST(alpha), але без ε
            first_alpha = set()

            nullable = True
            for X in alpha:
                first_alpha.update(FIRST[X] - {EPS})
                if EPS not in FIRST[X]:
                    nullable = False
                    break

            # Записуємо M[A, a] = A → α для всіх a ∈ FIRST(alpha)
            for a in first_alpha:
                M[A][a].append(alpha)

            # 2. Якщо alpha може породжувати ε → додаємо FOLLOW(A)
            if nullable:
                for b in FOLLOW[A]:
                    M[A][b].append(alpha)

    return M


def print_ll1_table(M):
    """
    Друк LL(1)-таблиці у форматі:
        Нетермінал | Стовпці (термінали)
    """

    all_terminals = sorted({t for row in M.values() for t in row.keys()})

    # Заголовок
    print("LL(1) TABLE:")
    print("".ljust(10), *[t.rjust(10) for t in all_terminals])

    # Рядки нетерміналів
    for A in sorted(M.keys()):
        row = M[A]
        line = A.ljust(10)
        for t in all_terminals:
            if t in row:
                # Перетворюємо продукцію в рядок A -> α
                rules = [" ".join(prod) for prod in row[t]]
                line += (" " + str(rules)).rjust(11)
            else:
                line += " ".rjust(11)
        print(line)