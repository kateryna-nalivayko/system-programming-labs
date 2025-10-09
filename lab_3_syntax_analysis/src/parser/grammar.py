TERMINALS = [
    'ID', 'ASSIGN', 'SEMI',
    'NUMBER', 'PLUS', 'MULT', 'LPAREN', 'RPAREN',
]

GRAMMAR = [
    ['s', ['stmt_list']],
    ['stmt_list', ['stmt_list', 'stmt']],
    ['stmt_list', ['stmt']],

    ['stmt', ['ID', 'ASSIGN', 'expr', 'SEMI']],

    ['expr', ['term']],
    ['expr', ['expr', 'PLUS', 'term']],

    ['term', ['factor']],
    ['term', ['term', 'MULT', 'factor']],

    ['factor', ['NUMBER']],
    ['factor', ['ID']],
    ['factor', ['LPAREN', 'expr', 'RPAREN']],
]
