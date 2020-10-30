import scanner
import ply.yacc as yacc

tokens = scanner.tokens

precedence = (
    ('nonassoc', 'LESSER', 'GREATER', 'LESSEREQUAL', 'GREATEREQUAL'),
    ("left", "EQUAL"),
    ('left', 'COMMA'),
    ('right', 'ASSIGN'),
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


def p_program(t):
    """program : instructions"""
    pass


def p_instructions(t):
    """instructions : instruction instructions
                | """
    pass


def p_empty_instruction(t):
    """instruction : SEMICOLON"""
    pass


def p_expression_value(t):
    """expression : INTEGER
                  | FLOAT
                  | matrix
                  | STRING"""
    # t[0] = t[1]
    pass


def p_expression_ID(t):
    """expression : ID"""
    # t[0] = names[t[1]]
    pass


def p_group_expression(t):
    """expression : LPAREN expression RPAREN"""
    pass


def p_instructions_scope(t):
    """instructions_scope : LCURLY instructions RCURLY"""
    pass


def p_expression_binop(t):
    """expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression DOTPLUS expression
                  | expression DOTMINUS expression
                  | expression DOTTIMES expression
                  | expression DOTDIVIDE expression"""
    pass


def p_expression_relation(t):
    """bool : expression LESSER expression
            | expression GREATER expression
            | expression LESSEREQUAL expression
            | expression GREATEREQUAL expression
            | expression NOTEQUAL expression
            | expression EQUAL expression"""
    pass


def p_uminus(t):
    """expression : MINUS expression %prec UMINUS"""
    pass


def p_trans(t):
    """matrix : expression TRANS"""
    pass


def p_matrix_assign(t):
    """instruction : ID ASSIGN matrix SEMICOLON"""
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
    # if t[2] == "=":
    #    names[t[1]] = t[3]
    pass


def p_position_assign(t):
    """instruction : ID array ASSIGN expression SEMICOLON
                   | ID array PLUSASSIGN expression SEMICOLON
                   | ID array MINUSASSIGN expression SEMICOLON
                   | ID array TIMESASSIGN expression SEMICOLON
                   | ID array DIVIDEASSIGN expression SEMICOLON"""  # A[0,1] = 5, etc.
    pass


def p_if_else(t):
    """instruction : IF bool instructions_scope
                  | IF bool instructions_scope ELSE instructions_scope"""
    pass


def p_while(t):
    """instruction : WHILE LBRACET bool RBRACET instructions_scope"""
    pass


def p_for(t):
    """instruction : FOR ID ASSIGN expression RANGE expression instructions_scope"""
    pass


def p_special_instruction(t):
    """instruction : BREAK SEMICOLON
                   | CONTINUE SEMICOLON
                   | RETURN SEMICOLON"""
    pass


def p_print(t):
    """instruction : PRINT expression"""
    #print(t[2])
    pass

def p_matrix(t):
    """matrix : LBRACET arraylist RBRACET"""
    pass


def p_arraylist(t):
    """arraylist : array
                 | array COMMA arraylist"""
    pass


def p_array(t):
    """array : LBRACET list RBRACET"""
    pass


def p_list(t):
    """list : expression
            | expression COMMA list"""
    pass


def p_array_access(t):
    """expression : ID array"""  # A[0,1], B[1], etc.
    pass


parser = yacc.yacc()
