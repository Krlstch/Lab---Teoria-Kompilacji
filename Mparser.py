import scanner
import ply.yacc as yacc

tokens = scanner.tokens

precedence = (
    # to fill ...
    ('nonassoc', 'LESSER', 'GREATER', 'LESSEREQUAL', 'GREATEREQUAL'),
    ("left", 'PLUS', 'MINUS'),
    ("left", "TIMES", "DIVIDE"),
    ('right', 'UMINUS')
    # to fill ...
)


def p_error(p):
    if p:
        print("Syntax error at line {0}: LexToken({1}, '{2}')".format(p.lineno, p.type, p.value))
    else:
        print("Unexpected end of input")


names = {}


def p_program(p):
    """program : instructions_opt"""


def p_instructions_opt_1(p):
    """instructions_opt : instructions """


def p_instructions_opt_2(p):
    """instructions_opt : """


def p_instructions_1(p):
    """instructions : instructions instruction """


def p_instructions_2(p):
    """instructions : instruction """

# to finish the grammar
# ....


def p_expression_ID(t):
    """expression : ID"""


def p_instruction_assign(t):
    '''instruction : ID ASSIGN expression SEMICOLON
               | ID PLUSASSIGN expression SEMICOLON
               | ID MINUSASSIGN expression SEMICOLON
               | ID TIMESASSIGN expression SEMICOLON
               | ID DIVIDEASSIGN expression SEMICOLON'''
    if t[2] == '=':
        names[t[1]] = t[3]
    else:
        if t[1] not in names:
            raise SyntaxError

        if t[2] == '+=':
            t[1] += t[3]
        elif t[2] == '-=':
            t[1] -= t[3]
        elif t[2] == '*=':
            t[1] *= t[3]
        elif t[2] == '/=':
            t[1] /= t[3]


def p_instruction_matrix_assign(t):
    '''instruction : ID ASSIGN matrix SEMICOLON
               | ID PLUSASSIGN matrix SEMICOLON
               | ID MINUSASSIGN matrix SEMICOLON
               | ID TIMESASSIGN matrix SEMICOLON
               | ID DIVIDEASSIGN matrix SEMICOLON'''
    if t[2] == '=':
        names[t[1]] = t[3]
    else:
        if t[1] not in names:
            raise SyntaxError
        if len(t[1]) != len(t[3]) or len(t[1][0]) != len(t[3][0]):
            raise SyntaxError
        for i in range(len(t[1])):
            for j in range(len(t[1][0])):
                if t[2] == '+=':
                    t[1][i][j] += t[3][i][j]
                elif t[2] == '-=':
                    t[1][i][j] -= t[3][i][j]
                elif t[2] == '*=':
                    t[1][i][j] *= t[3][i][j]
                elif t[2] == '/=':
                    t[1][i][j] /= t[3][i][j]


def p_expression_binop(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if t[2] == '+':
        t[0] = t[1] + t[3]
    elif t[2] == '-':
        t[0] = t[1] - t[3]
    elif t[2] == '*':
        t[0] = t[1] * t[3]
    elif t[2] == '/':
        t[0] = t[1] / t[3]


def p_expression_binop_matrix(t):
    '''matrix : matrix DOTPLUS matrix
              | matrix DOTMINUS matrix
              | matrix DOTTIMES matrix
              | matrix DOTDIVIDE matrix'''
    if len(t[1]) != len(t[3]) or len(t[1][0]) != len(t[3][0]):
        raise SyntaxError
    t[0] = [[0 for j in range(len(t[1][0]))] for i in range(len(t[1]))]

    for i in range(len(t[1])):
        for j in range(len(t[1][0])):
            if t[2] == '.+':
                t[0][i][j] = t[1][i][j] + t[3][i][j]
            elif t[2] == '.-':
                t[0][i][j] = t[1][i][j] - t[3][i][j]
            elif t[2] == '.*':
                t[0][i][j] = t[1][i][j] * t[3][i][j]
            elif t[2] == './':
                t[0][i][j] = t[1][i][j] / t[3][i][j]


def p_expression_relation(t):
    '''bool : expression LESSER expression
                      | expression GREATER expression
                      | expression LESSEREQUAL expression
                      | expression GREATEREQUAL expression
                      | expression NOTEQUAL expression
                      | expression EQUAL expression'''
    if t[2] == '<':
        t[0] = t[1] < t[3]
    elif t[2] == '>':
        t[0] = t[1] > t[3]
    elif t[2] == '<=':
        t[0] = t[1] <= t[3]
    elif t[2] == '>=':
        t[0] = t[1] >= t[3]
    elif t[2] == '/=':
        t[0] = t[1] != t[3]
    elif t[2] == '==':
        t[0] = t[1] == t[3]


def p_expression_uminus(p):
    "expression : '-' expression %prec UMINUS"
    p[0] = -p[2]


def p_matrix_uminus(p):
    "matrix : '-' matrix %prec UMINUS"
    p[0] = [[-p[2][i][j] for j in range(len(p[0][0]))] for i in range(len(p[0]))]


def p_matrix_transpose(t):
    'matrix : matrix TRANS'
    t[0] = [[t[1][j][i] for j in range(len(t[1]))] for i in range(len(t[1][0]))]


def p_matrix(t):
    '''matrix : LBRACET arraylist RBRACET'''
    t[0] = t[2]


def p_arraylist_1(t):
    '''arraylist : array'''
    t[0] = [t[1]]


def p_arraylist_2(p):
    '''arraylist : array COMMA arraylist'''
    if len(p[1]) != len(p[3][0]):
        raise SyntaxError
    p[0] = [p[1]] + p[3]


def p_array(t):
    '''array : LBRACET list RBRACET'''
    t[0] = t[2]


def p_list_1(t):
    '''list : expression'''
    t[0] = [t[1]]


def p_list_2(p):
    '''list : expression COMMA list'''
    p[0] = [p[1]] + p[3]


def p_expression_number(t):
    '''expression : INTEGER
                  | FLOAT'''
    t[0] = t[1]


def p_matrix_gen(t):
    '''matrix : ZEROS LPAREN expression RPAREN
              | ONES LPAREN expression RPAREN
              | EYE LPAREN expression RPAREN'''
    if t[1] == "zeros":
        t[0] = [[0 for i in range(t[3])] for j in range(t[3])]
    elif t[1] == "ones":
        t[0] = [[1 for i in range(t[3])] for j in range(t[3])]
    elif t[1] == "eye":
        t[0] = [[lambda x : 1 if i == j else 0for i in range(t[3])] for j in range(t[3])]


def p_matrix_access_write(t):
    """instruction : ID array ASSIGN expression SEMICOLON"""
    if not isinstance(names[t[1]], list):
        raise SyntaxError
    if len(t[2]) != 2:
        raise SyntaxError
    if not isinstance(t[2][0], int) or not isinstance(t[2][1], int):
        raise SyntaxError
    if len(t[1]) < t[2][0] or len(t[1][0]) < t[2][1]:
        raise SyntaxError
    names[t[1]][t[2][0]][t[2][1]] = t[4]


def p_matrix_access_read(t):
    """expression : ID array"""
    if not isinstance(names[t[1]], list):
        raise SyntaxError
    if len(t[2]) != 2:
        raise SyntaxError
    if not isinstance(t[2][0], int) or not isinstance(t[2][1], int):
        raise SyntaxError
    if len(t[1]) < t[2][0] or len(t[1][0]) < t[2][1]:
        raise SyntaxError
    t[0] = names[t[1]][t[2][0]][t[2][1]]


parser = yacc.yacc()
