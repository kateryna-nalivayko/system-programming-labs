from lab_5_parser.src.ll1.first_follow import Grammar
from lab_5_parser.src.ll1.recursive_parser import LL1Parser
from lab_5_parser.src.visualize.render import render_ast


g = Grammar.from_bnf("src/ll1/expr.bnf")
parser = LL1Parser(g)

tokens = ["id", "+", "id", "*", "id"]
ast = parser.parse(tokens)

render_ast(ast, filename="example1")