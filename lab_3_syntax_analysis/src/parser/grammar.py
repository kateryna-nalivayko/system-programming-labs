TERMINALS = [
    'ID', 'ASSIGN', 'SEMI',
    'NUMBER', 'PLUS', 'MULT', 'DIV', 'POW', 'LPAREN', 'RPAREN',
    'IF', 'ELSE', 'WHILE',
    'DUSHKA_L', 'DUSHKA_R'
]

GRAMMAR = [
    ['s', ['stmt_list']],
    ['stmt_list', ['stmt_list', 'stmt']],
    ['stmt_list', ['stmt']],

    ['stmt', ['ID', 'ASSIGN', 'expr', 'SEMI']],
    ['stmt', ['IF', 'LPAREN', 'expr', 'RPAREN', 'stmt']],
    ['stmt', ['IF', 'LPAREN', 'expr', 'RPAREN', 'stmt', 'ELSE', 'stmt']],
    ['stmt', ['WHILE', 'LPAREN', 'expr', 'RPAREN', 'stmt']],
    ['stmt', ['DUSHKA_L', 'stmt_list', 'DUSHKA_R']],


    ['expr', ['add']],

    ['add', ['add', 'PLUS', 'mul']],
    ['add', ['mul']],

    ['mul', ['mul', 'MULT', 'pow']],
    ['mul', ['mul', 'DIV', 'pow']],
    ['mul', ['pow']],

    ['pow', ['atom', 'POW', 'pow']],
    ['pow', ['atom']],

    ['atom', ['NUMBER']],
    ['atom', ['ID']],
    ['atom', ['LPAREN', 'expr', 'RPAREN']],
]
