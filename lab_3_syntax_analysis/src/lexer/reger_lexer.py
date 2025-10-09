import re
from lab_3_syntax_analysis.src.lexer.tokens import TOKEN_SPECS


class LexicalError(Exception):
    def __init__(self, symbol: str, pos: int, line: int, col: int):
        super().__init__(f"LexicalError: невідомий символ '{symbol}' (рядок {line}, позиція {col})")
        self.symbol = symbol
        self.pos = pos
        self.line = line
        self.col = col


def tokenize(code: str):
    token_regex = "|".join(f"(?P<{name}>{pattern})" for name, pattern in TOKEN_SPECS)
    get_token = re.compile(token_regex).match

    pos = 0
    line = 1
    col = 1
    n = len(code)

    while pos < n:
        match = get_token(code, pos)
        if not match:
            raise LexicalError(code[pos], pos, line, col)

        kind = match.lastgroup
        value = match.group()
        start = pos
        end = match.end()

        if kind == "NOVYI_RIADOK":
            line += 1
            col = 1
        else:
            col += (end - start)

        pos = end

        if kind in {"PROPUSK", "KOMENTAR_ODN", "KOMENTAR_BAG"}:
            continue

        yield kind, value, line, col


def main():
    path = "/Users/admin/Documents/system-programming-labs/lab_3_syntax_analysis/samples/example.cs"

    with open(path, "r", encoding="utf-8") as f:
        code = f.read()

    try:
        for token in tokenize(code):
            print(token)
    except LexicalError as e:
        print(e)


if __name__ == "__main__":
    main()
