from first_follow import Grammar
from ll1_table_parser import LL1TableParser

g = Grammar.from_bnf("../../grammar/expr.bnf")
parser = LL1TableParser(g)

tokens = ["id", "+", "id", "*", "id"]

result = parser.parse(tokens)
print("LL(1) parse OK:", result)