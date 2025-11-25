from first_follow import Grammar, compute_first, compute_follow
import os

BASE = os.path.dirname(__file__)
GRAMMAR_PATH = os.path.join(BASE, "expr.bnf")

g = Grammar.from_bnf(GRAMMAR_PATH)
FIRST = compute_first(g)
FOLLOW = compute_follow(g, FIRST)

print("=== FIRST (final, ordered) ===")
for nt in sorted(g.nonterminals):
    print(f"{nt}: {FIRST[nt]}")

print("\n=== FIRST (terminals) ===")
for t in sorted(g.terminals):
    print(f"{t}: {FIRST[t]}")

print("\n=== FOLLOW (final, ordered) ===")
for nt in sorted(g.nonterminals):
    print(f"{nt}: {FOLLOW[nt]}")
