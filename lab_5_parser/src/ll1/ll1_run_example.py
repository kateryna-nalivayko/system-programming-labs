from first_follow import Grammar
from ll1_parser import LL1Parser

g = Grammar.from_bnf("expr.bnf")
parser = LL1Parser(g)

tokens = ["id", "+", "id", "*", "id"]
ast = parser.parse(tokens)

print("AST:", ast)