def to_terminals(lex_stream):
    terms = []
    rich = []

    mapping = {
        "ZMINNA": "ID",
        "CHYSLO": "NUMBER",
        "PRYSVOIENNIA": "ASSIGN",
        "KRAPKA_Z_COMOYU": "SEMI",
        "DODAVANNIA": "PLUS",
        "MNOZHENNIA": "MULT",
        "DILENNIA":  "DIV",
        "POWER":     "POW",
        "LAPKA_L": "LPAREN",
        "LAPKA_R": "RPAREN",
    }

    for typ, value, line, col in lex_stream:
        if typ in mapping:
            terms.append(mapping[typ])
            rich.append((mapping[typ], value))
    return terms, rich