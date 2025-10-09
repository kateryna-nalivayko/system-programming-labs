from lab_3_syntax_analysis.src.lexer.reger_lexer import tokenize
from lab_3_syntax_analysis.src.parser.adapters import to_terminals
from lab_3_syntax_analysis.src.parser.grammar import TERMINALS, GRAMMAR
from lab_3_syntax_analysis.src.parser.worley_parser import EarleyParser

from lab_3_syntax_analysis.src.parser.ast_builder import build_ast, eval_ast, gen_python_code


def main():
    path = "/Users/admin/Documents/system-programming-labs/lab_3_syntax_analysis/samples/min_gramma.cs"

    with open(path, "r", encoding="utf-8") as f:
        code = f.read()

    lexed = list(tokenize(code))

    terms, rich = to_terminals(lexed)

    parser = EarleyParser(TERMINALS, GRAMMAR, debug=True)
    ok = parser.recognize(terms)

    print("Синтаксичний аналiз тексту проведено, все добре!" if ok else 'Помилка')

    ast = build_ast(rich)
    value = eval_ast(ast, {})
    py_code = gen_python_code(ast)

    print("Результат обчислення:", value)
    print("Згенерований код на Python:")
    print(py_code)


if __name__ == "__main__":
    main()
