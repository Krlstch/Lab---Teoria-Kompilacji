"""program : instructions"""

"""instructions : instruction instructions
                | """

"""instruction : SEMICOLON"""  # pusta instrukcja

"""expression : INTEGER
              | FLOAT
              | matrix
              | bool
              | ID
              | STRING"""

"""expression : LPAREN expression RPAREN"""

"""instruction_scope = LCURLY instructions RCURLY"""


# wyrażenia binarne, w tym operacje macierzowe 'element po elemencie'

"""expression : expression PLUS expression
              | expression MINUS expression
              | expression TIMES expression
              | expression DIVIDE expression
              | expression DOTPLUS expression
              | expression DOTMINUS expression
              | expression DOTTIMES expression
              | expression DOTDIVIDE expression"""

# wyrażenia relacyjne

"""bool : expression LESSER expression
        | expression GREATER expression
        | expression LESSEREQUAL expression
        | expression GREATEREQUAL expression
        | expression NOTEQUAL expression
        | expression EQUAL expression"""

# negację unarną,

"""expression : '-' expression %prec UMINUS"""

# transpozycję macierzy,

"""matrix : expression TRANS"""

# inicjalizację macierzy konkretnymi wartościami,

"""instruction : ID ASSIGN matrix SEMICOLON"""

# macierzowe funkcje specjalne,

"""matrix : ZEROS LPAREN expression RPAREN
          | ONES LPAREN expression RPAREN
          | EYE LPAREN expression RPAREN"""

# instrukcję przypisania, w tym różne operatory przypisania

"""instruction : ID ASSIGN expression SEMICOLON
                | ID PLUSASSIGN expression SEMICOLON
                | ID MINUSASSIGN expression SEMICOLON
                | ID TIMESASSIGN expression SEMICOLON
                | ID DIVIDEASSIGN expression SEMICOLON"""

"""instruction : ID array ASSIGN expression SEMICOLON
               | ID PLUSASSIGN expression SEMICOLON
               | ID MINUSASSIGN expression SEMICOLON
               | ID TIMESASSIGN expression SEMICOLON
               | ID DIVIDEASSIGN expression SEMICOLON"""  # A[0,1] = 5, etc.

# instrukcję warunkową if-else,

"""instruction : IF LBRACET expression RBRACET instructions_scope
              | IF LBRACET expression RBRACET instructions_scope ELSE instructions_scope"""

# pętle: while and for,

"""instruction : WHILE LBRACET bool RBRACET instructions_scope"""

"""instruction : FOR ID EQUALS expression RANGE expression instructions_scope"""

# instrukcje break, continue oraz return,

"""instruction : BREAK SEMICOLON
               | CONTINUE SEMICOLON
               | RETURN SEMICOLON"""

# instrukcję print,

"""instruction : PRINT expression SEMICOLON"""

# instrukcje złożone ?

# tablice oraz ich zakresy.

"""matrix : LBRACET arraylist RBRACET"""
"""arraylist : array
             | array COMMA arraylist"""
"""array : LBRACET list RBRACET"""
"""list : expression
        | expression COMMA list"""

"""expression : ID array"""  # A[0,1], B[1], etc.

