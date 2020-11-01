import scanner
import ply.yacc as yacc

from mast import Mast

tokens = scanner.tokens

precedence = (
    ('nonassoc', 'LESSER', 'GREATER', 'LESSEREQUAL', 'GREATEREQUAL'),
    ('left', 'COMMA'),
    ('left', 'ASSIGN'),
    ("left", 'PLUS', 'MINUS'),
    ("left", "TIMES", "DIVIDE"),
    ('right', 'UMINUS')
)


def p_error(p):
    if p:
        print("Syntax error at line {0}: LexToken({1}, '{2}')".format(p.lineno, p.type, p.value))
    else:
        print("Unexpected end of input")


names = {}
instr_list = []


def p_program(t):
    """program : instructions"""
    t[0] = t[1]


def p_instructions(t):
    """instructions : instructions instruction
                | """
    if len(t) > 1:
        t[1].append(t[2])
        t[0] = t[1]
    else:
        t[0] = []


def p_empty_instruction(t):
    """instruction : SEMICOLON"""
    pass


def p_expression_value(t):
    """expression : INTEGER
                  | FLOAT
                  | matrix
                  | STRING"""
    t[0] = t[1]


def p_expression_ID(t):
    """expression : ID"""
    t[0] = Mast(action="get", params=t[1])


def p_group_expression(t):
    """expression : LPAREN expression RPAREN"""
    t[0] = t[2]


def p_instructions_scope(t):
    """instruction : LCURLY instructions RCURLY"""
    t[0] = Mast(action="execute", params=t[2])


def p_expression_binop(t):
    """expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression"""
    t[0] = Mast(action="binop", params=[t[2], t[1], t[3]])


def p_expression_binop_mat(t):
    """expression : expression DOTPLUS expression
                  | expression DOTMINUS expression
                  | expression DOTTIMES expression
                  | expression DOTDIVIDE expression"""
    t[0] = Mast(action="binop_mat", params=[t[2], t[1], t[3]])


def p_expression_relation(t):
    """condition : expression LESSER expression
                | expression GREATER expression
                | expression LESSEREQUAL expression
                | expression GREATEREQUAL expression
                | expression NOTEQUAL expression
                | expression EQUAL expression"""
    t[0] = Mast(action="relation", params=[t[2], t[1], t[3]])


def p_uminus(t):
    """expression : MINUS expression %prec UMINUS"""
    t[0] = Mast(action="uminus", params=t[2])


def p_trans(t):
    """matrix : expression TRANS"""
    pass


def p_matrix_gen(t):
    """matrix : ZEROS LPAREN expression RPAREN
              | ONES LPAREN expression RPAREN
              | EYE LPAREN expression RPAREN"""
    pass


def p_assign(t):
    """instruction : ID ASSIGN expression SEMICOLON
                    | ID PLUSASSIGN expression SEMICOLON
                    | ID MINUSASSIGN expression SEMICOLON
                    | ID TIMESASSIGN expression SEMICOLON
                    | ID DIVIDEASSIGN expression SEMICOLON"""
    t[0] = Mast(action='assign', params=[t[2], t[1], t[3]])


def p_position_assign(t):
    """instruction : ID array ASSIGN expression SEMICOLON
                   | ID array PLUSASSIGN expression SEMICOLON
                   | ID array MINUSASSIGN expression SEMICOLON
                   | ID array TIMESASSIGN expression SEMICOLON
                   | ID array DIVIDEASSIGN expression SEMICOLON"""  # A[0,1] = 5, etc.
    pass


def p_if_else(t):
    """instruction : IF LPAREN condition RPAREN instruction
                  | IF LPAREN condition RPAREN instruction ELSE instruction"""
    if len(t) == 6:
        t[0] = Mast(action="if", params=[t[3], t[5]])
    else:
        t[0] = Mast(action="ifelse", params=[t[3], t[5], t[7]])


def p_while(t):
    """instruction : WHILE LPAREN condition RPAREN instruction"""
    t[0] = Mast(action="while", params=[t[3], t[5]])


def p_for(t):
    """instruction : FOR ID ASSIGN expression RANGE expression instruction"""
    t[0] = Mast(action="for", params=[t[2], t[4], t[6], t[7]])


def p_special_instruction(t):
    """instruction : BREAK SEMICOLON
                   | CONTINUE SEMICOLON
                   | RETURN expression SEMICOLON"""
    pass


def p_print(t):
    """instruction : PRINT list SEMICOLON"""
    t[0] = Mast(action='print', params=t[2])



def p_matrix(t):
    """matrix : LBRACET arraylist RBRACET"""
    pass


def p_arraylist(t):
    """arraylist : array
                 | arraylist COMMA array"""
    pass


def p_array(t):
    """array : LBRACET list RBRACET"""
    pass


def p_list(t):
    """list : expression
            | list COMMA expression"""
    if len(t) > 2:
        t[1].append(t[3])
        t[0] = t[1]
    else:
        t[0] = [t[1]]


def p_array_access(t):
    """expression : ID array"""  # A[0,1], B[1], etc.
    pass


parser = yacc.yacc()
