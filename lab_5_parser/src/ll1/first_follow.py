from collections import defaultdict

EPS = 'ε'


# Клас Grammar зберігає всю інформацію про граматику (нетермінали, термінали та продукції)
class Grammar:
    def __init__(self):
        self.productions = defaultdict(list)
        self.nonterminals = set()
        self.terminals = set()
        self.start_symbol = None

    @staticmethod
    def from_bnf(path):
        g = Grammar()
        with open(path, 'r', encoding='utf-8') as f:
            # Читання BNF-файлу построково
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue

                # Розділяємо продукцію на ліву та праву частини
                left, right = line.split('->')
                A = left.strip()
                g.nonterminals.add(A)

                if g.start_symbol is None:
                    g.start_symbol = A

                # Підтримка кількох альтернатив A -> α | β | γ
                rhs_alts = right.split('|')
                # Додаємо кожну альтернативу до списку продукцій
                for alt in rhs_alts:
                    symbols = alt.strip().split()
                    g.productions[A].append(symbols)

                    # Визначаємо термінали (усе, що не є нетерміналом і не ε)
                    for s in symbols:
                        if not s.isupper() and s != EPS:
                            g.terminals.add(s)

        return g


# Обчислення множин FIRST(1) для кожного нетермінала
def compute_first(grammar):
    FIRST = {nt: set() for nt in grammar.nonterminals}
    FIRST.update({t: {t} for t in grammar.terminals})
    FIRST[EPS] = {EPS}

    # Ітеративний алгоритм: повторюємо, доки множини FIRST не стабілізуються
    changed = True
    while changed:
        changed = False

        # Проходимо кожну продукцію A → α
        for A in grammar.nonterminals:
            for alpha in grammar.productions[A]:
                nullable_prefix = True

                for X in alpha:
                    # Додаємо всі термінали FIRST(X), окрім ε
                    before = len(FIRST[A])
                    FIRST[A].update(FIRST[X] - {EPS})

                    # Якщо X не може породити ε — зупиняємо аналіз послідовності α
                    if EPS not in FIRST[X]:
                        nullable_prefix = False
                        break

                    if len(FIRST[A]) > before:
                        changed = True

                # Якщо всі X у α можуть породити ε — додаємо ε до FIRST(A)
                if nullable_prefix and EPS not in FIRST[A]:
                    FIRST[A].add(EPS)
                    changed = True

    return FIRST


# Обчислення множин FOLLOW(1) за правилами з книги Ахо–Сеті–Ульман
def compute_follow(grammar, FIRST):
    FOLLOW = {nt: set() for nt in grammar.nonterminals}
    # Додаємо символ кінця вводу $ до FOLLOW стартового нетермінала
    FOLLOW[grammar.start_symbol].add('$')

    changed = True
    while changed:
        changed = False

        # Перебір усіх продукцій для побудови FOLLOW
        for A in grammar.nonterminals:
            for alpha in grammar.productions[A]:

                for i, B in enumerate(alpha):
                    if B not in grammar.nonterminals:
                        continue

                    # β — символи, які йдуть після нетермінала B у продукції A → α B β
                    beta = alpha[i + 1:]

                    if beta:
                        first_beta = set()
                        nullable = True

                        # FIRST(β) \ {ε} додається до FOLLOW(B)
                        for X in beta:
                            first_beta.update(FIRST[X] - {EPS})
                            if EPS not in FIRST[X]:
                                nullable = False
                                break

                        before = len(FOLLOW[B])
                        FOLLOW[B].update(first_beta)
                        if len(FOLLOW[B]) > before:
                            changed = True

                        # Якщо β може породити ε — додаємо також FOLLOW(A)
                        if nullable:
                            before = len(FOLLOW[B])
                            FOLLOW[B].update(FOLLOW[A])
                            if len(FOLLOW[B]) > before:
                                changed = True

                    else:
                        before = len(FOLLOW[B])
                        FOLLOW[B].update(FOLLOW[A])
                        if len(FOLLOW[B]) > before:
                            changed = True

    return FOLLOW