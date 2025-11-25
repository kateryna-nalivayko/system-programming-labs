from first_follow import Grammar, compute_first, compute_follow
from table import build_ll1_table, print_ll1_table
import os

BASE = os.path.dirname(__file__)
g = Grammar.from_bnf(os.path.join(BASE, "expr.bnf"))

FIRST = compute_first(g)
FOLLOW = compute_follow(g, FIRST)

M = build_ll1_table(g, FIRST, FOLLOW)

print_ll1_table(M)