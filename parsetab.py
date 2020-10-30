
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocLESSERGREATERLESSEREQUALGREATEREQUALleftEQUALleftCOMMArightASSIGNleftPLUSMINUSleftTIMESDIVIDErightUMINUSASSIGN BREAK COMMA COMMENT CONTINUE DIVIDE DIVIDEASSIGN DOTDIVIDE DOTMINUS DOTPLUS DOTTIMES ELSE EQUAL EYE FLOAT FOR GREATER GREATEREQUAL ID IF INTEGER LBRACET LCURLY LESSER LESSEREQUAL LPAREN MINUS MINUSASSIGN NOTEQUAL ONES PLUS PLUSASSIGN PRINT RANGE RBRACET RCURLY RETURN RPAREN SEMICOLON STRING TIMES TIMESASSIGN TRANS WHILE ZEROSprogram : instructionsinstructions : instruction instructions\n                | instruction : SEMICOLONexpression : INTEGER\n                  | FLOAT\n                  | matrix\n                  | STRINGexpression : IDexpression : LPAREN expression RPARENinstructions_scope : LCURLY instructions RCURLYexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expression\n                  | expression DOTPLUS expression\n                  | expression DOTMINUS expression\n                  | expression DOTTIMES expression\n                  | expression DOTDIVIDE expressionbool : expression LESSER expression\n            | expression GREATER expression\n            | expression LESSEREQUAL expression\n            | expression GREATEREQUAL expression\n            | expression NOTEQUAL expression\n            | expression EQUAL expressionexpression : MINUS expression %prec UMINUSmatrix : expression TRANSinstruction : ID ASSIGN matrix SEMICOLONmatrix : ZEROS LPAREN expression RPAREN\n              | ONES LPAREN expression RPAREN\n              | EYE LPAREN expression RPARENinstruction : ID ASSIGN expression SEMICOLON\n                    | ID PLUSASSIGN expression SEMICOLON\n                    | ID MINUSASSIGN expression SEMICOLON\n                    | ID TIMESASSIGN expression SEMICOLON\n                    | ID DIVIDEASSIGN expression SEMICOLONinstruction : ID array ASSIGN expression SEMICOLON\n                   | ID array PLUSASSIGN expression SEMICOLON\n                   | ID array MINUSASSIGN expression SEMICOLON\n                   | ID array TIMESASSIGN expression SEMICOLON\n                   | ID array DIVIDEASSIGN expression SEMICOLONinstruction : IF bool instructions_scope\n                  | IF bool instructions_scope ELSE instructions_scopeinstruction : WHILE LBRACET bool RBRACET instructions_scopeinstruction : FOR ID ASSIGN expression RANGE expression instructions_scopeinstruction : BREAK SEMICOLON\n                   | CONTINUE SEMICOLON\n                   | RETURN SEMICOLONinstruction : PRINT expressionmatrix : LBRACET arraylist RBRACETarraylist : array\n                 | array COMMA arraylistarray : LBRACET list RBRACETlist : expression\n            | expression COMMA listexpression : ID array'
    
_lr_action_items = {'$end':([0,1,2,3,4,13,23,24,25,26,27,36,37,38,39,53,69,70,72,80,81,82,83,84,85,91,101,102,103,104,105,106,107,108,109,113,117,118,119,120,121,123,124,125,126,127,129,132,],[-3,0,-1,-3,-4,-2,-5,-6,-7,-8,-9,-46,-47,-48,-49,-42,-27,-56,-26,-28,-32,-33,-34,-35,-36,-53,-12,-13,-14,-15,-16,-17,-18,-19,-10,-50,-37,-38,-39,-40,-41,-43,-11,-29,-30,-31,-44,-45,]),'SEMICOLON':([0,3,4,9,10,11,23,24,25,26,27,36,37,38,39,40,41,42,43,44,45,53,54,69,70,72,80,81,82,83,84,85,86,87,88,89,90,91,101,102,103,104,105,106,107,108,109,113,117,118,119,120,121,123,124,125,126,127,129,132,],[4,4,-4,36,37,38,-5,-6,-7,-8,-9,-46,-47,-48,-49,80,81,82,83,84,85,-42,4,-27,-56,-26,-28,-32,-33,-34,-35,-36,117,118,119,120,121,-53,-12,-13,-14,-15,-16,-17,-18,-19,-10,-50,-37,-38,-39,-40,-41,-43,-11,-29,-30,-31,-44,-45,]),'ID':([0,3,4,6,8,12,14,15,16,17,18,20,23,24,25,26,27,28,29,34,36,37,38,39,46,47,48,49,50,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,73,74,75,79,80,81,82,83,84,85,91,92,101,102,103,104,105,106,107,108,109,113,117,118,119,120,121,123,124,125,126,127,129,130,132,],[5,5,-4,27,35,27,27,27,27,27,27,27,-5,-6,-7,-8,-9,27,27,27,-46,-47,-48,-49,27,27,27,27,27,-42,5,27,27,27,27,27,27,27,27,27,27,27,27,27,27,-27,-56,-26,27,27,27,27,-28,-32,-33,-34,-35,-36,-53,27,-12,-13,-14,-15,-16,-17,-18,-19,-10,-50,-37,-38,-39,-40,-41,-43,-11,-29,-30,-31,-44,27,-45,]),'IF':([0,3,4,23,24,25,26,27,36,37,38,39,53,54,69,70,72,80,81,82,83,84,85,91,101,102,103,104,105,106,107,108,109,113,117,118,119,120,121,123,124,125,126,127,129,132,],[6,6,-4,-5,-6,-7,-8,-9,-46,-47,-48,-49,-42,6,-27,-56,-26,-28,-32,-33,-34,-35,-36,-53,-12,-13,-14,-15,-16,-17,-18,-19,-10,-50,-37,-38,-39,-40,-41,-43,-11,-29,-30,-31,-44,-45,]),'WHILE':([0,3,4,23,24,25,26,27,36,37,38,39,53,54,69,70,72,80,81,82,83,84,85,91,101,102,103,104,105,106,107,108,109,113,117,118,119,120,121,123,124,125,126,127,129,132,],[7,7,-4,-5,-6,-7,-8,-9,-46,-47,-48,-49,-42,7,-27,-56,-26,-28,-32,-33,-34,-35,-36,-53,-12,-13,-14,-15,-16,-17,-18,-19,-10,-50,-37,-38,-39,-40,-41,-43,-11,-29,-30,-31,-44,-45,]),'FOR':([0,3,4,23,24,25,26,27,36,37,38,39,53,54,69,70,72,80,81,82,83,84,85,91,101,102,103,104,105,106,107,108,109,113,117,118,119,120,121,123,124,125,126,127,129,132,],[8,8,-4,-5,-6,-7,-8,-9,-46,-47,-48,-49,-42,8,-27,-56,-26,-28,-32,-33,-34,-35,-36,-53,-12,-13,-14,-15,-16,-17,-18,-19,-10,-50,-37,-38,-39,-40,-41,-43,-11,-29,-30,-31,-44,-45,]),'BREAK':([0,3,4,23,24,25,26,27,36,37,38,39,53,54,69,70,72,80,81,82,83,84,85,91,101,102,103,104,105,106,107,108,109,113,117,118,119,120,121,123,124,125,126,127,129,132,],[9,9,-4,-5,-6,-7,-8,-9,-46,-47,-48,-49,-42,9,-27,-56,-26,-28,-32,-33,-34,-35,-36,-53,-12,-13,-14,-15,-16,-17,-18,-19,-10,-50,-37,-38,-39,-40,-41,-43,-11,-29,-30,-31,-44,-45,]),'CONTINUE':([0,3,4,23,24,25,26,27,36,37,38,39,53,54,69,70,72,80,81,82,83,84,85,91,101,102,103,104,105,106,107,108,109,113,117,118,119,120,121,123,124,125,126,127,129,132,],[10,10,-4,-5,-6,-7,-8,-9,-46,-47,-48,-49,-42,10,-27,-56,-26,-28,-32,-33,-34,-35,-36,-53,-12,-13,-14,-15,-16,-17,-18,-19,-10,-50,-37,-38,-39,-40,-41,-43,-11,-29,-30,-31,-44,-45,]),'RETURN':([0,3,4,23,24,25,26,27,36,37,38,39,53,54,69,70,72,80,81,82,83,84,85,91,101,102,103,104,105,106,107,108,109,113,117,118,119,120,121,123,124,125,126,127,129,132,],[11,11,-4,-5,-6,-7,-8,-9,-46,-47,-48,-49,-42,11,-27,-56,-26,-28,-32,-33,-34,-35,-36,-53,-12,-13,-14,-15,-16,-17,-18,-19,-10,-50,-37,-38,-39,-40,-41,-43,-11,-29,-30,-31,-44,-45,]),'PRINT':([0,3,4,23,24,25,26,27,36,37,38,39,53,54,69,70,72,80,81,82,83,84,85,91,101,102,103,104,105,106,107,108,109,113,117,118,119,120,121,123,124,125,126,127,129,132,],[12,12,-4,-5,-6,-7,-8,-9,-46,-47,-48,-49,-42,12,-27,-56,-26,-28,-32,-33,-34,-35,-36,-53,-12,-13,-14,-15,-16,-17,-18,-19,-10,-50,-37,-38,-39,-40,-41,-43,-11,-29,-30,-31,-44,-45,]),'RCURLY':([3,4,13,23,24,25,26,27,36,37,38,39,53,54,69,70,72,80,81,82,83,84,85,91,94,101,102,103,104,105,106,107,108,109,113,117,118,119,120,121,123,124,125,126,127,129,132,],[-3,-4,-2,-5,-6,-7,-8,-9,-46,-47,-48,-49,-42,-3,-27,-56,-26,-28,-32,-33,-34,-35,-36,-53,124,-12,-13,-14,-15,-16,-17,-18,-19,-10,-50,-37,-38,-39,-40,-41,-43,-11,-29,-30,-31,-44,-45,]),'ASSIGN':([5,19,35,91,],[14,46,79,-53,]),'PLUSASSIGN':([5,19,91,],[15,47,-53,]),'MINUSASSIGN':([5,19,91,],[16,48,-53,]),'TIMESASSIGN':([5,19,91,],[17,49,-53,]),'DIVIDEASSIGN':([5,19,91,],[18,50,-53,]),'LBRACET':([5,6,7,12,14,15,16,17,18,20,27,28,29,33,34,46,47,48,49,50,55,56,57,58,59,60,61,62,63,64,65,66,67,68,73,74,75,79,92,114,130,],[20,33,34,33,33,33,33,33,33,33,20,33,33,20,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,20,33,]),'INTEGER':([6,12,14,15,16,17,18,20,28,29,34,46,47,48,49,50,55,56,57,58,59,60,61,62,63,64,65,66,67,68,73,74,75,79,92,130,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'FLOAT':([6,12,14,15,16,17,18,20,28,29,34,46,47,48,49,50,55,56,57,58,59,60,61,62,63,64,65,66,67,68,73,74,75,79,92,130,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'STRING':([6,12,14,15,16,17,18,20,28,29,34,46,47,48,49,50,55,56,57,58,59,60,61,62,63,64,65,66,67,68,73,74,75,79,92,130,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'LPAREN':([6,12,14,15,16,17,18,20,28,29,30,31,32,34,46,47,48,49,50,55,56,57,58,59,60,61,62,63,64,65,66,67,68,73,74,75,79,92,130,],[28,28,28,28,28,28,28,28,28,28,73,74,75,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'MINUS':([6,12,14,15,16,17,18,20,22,23,24,25,26,27,28,29,34,39,40,41,42,43,44,45,46,47,48,49,50,52,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,79,86,87,88,89,90,91,92,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,125,126,127,130,131,],[29,29,29,29,29,29,29,29,62,-5,-6,-7,-8,-9,29,29,29,62,-7,62,62,62,62,62,29,29,29,29,29,62,29,29,29,29,29,29,29,29,29,29,29,29,29,29,-27,-56,62,-26,29,29,29,29,62,62,62,62,62,-53,29,62,62,62,62,62,62,-12,-13,-14,-15,62,62,62,62,-10,62,62,62,-50,62,-29,-30,-31,29,62,]),'ZEROS':([6,12,14,15,16,17,18,20,28,29,34,46,47,48,49,50,55,56,57,58,59,60,61,62,63,64,65,66,67,68,73,74,75,79,92,130,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'ONES':([6,12,14,15,16,17,18,20,28,29,34,46,47,48,49,50,55,56,57,58,59,60,61,62,63,64,65,66,67,68,73,74,75,79,92,130,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'EYE':([6,12,14,15,16,17,18,20,28,29,34,46,47,48,49,50,55,56,57,58,59,60,61,62,63,64,65,66,67,68,73,74,75,79,92,130,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'LCURLY':([21,23,24,25,26,27,69,70,72,91,93,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,113,115,125,126,127,131,],[54,-5,-6,-7,-8,-9,-27,-56,-26,-53,54,-20,-21,-22,-23,-24,-25,-12,-13,-14,-15,-16,-17,-18,-19,-10,-50,54,-29,-30,-31,54,]),'LESSER':([22,23,24,25,26,27,69,70,72,91,101,102,103,104,105,106,107,108,109,113,125,126,127,],[55,-5,-6,-7,-8,-9,-27,-56,-26,-53,-12,-13,-14,-15,-16,-17,-18,-19,-10,-50,-29,-30,-31,]),'GREATER':([22,23,24,25,26,27,69,70,72,91,101,102,103,104,105,106,107,108,109,113,125,126,127,],[56,-5,-6,-7,-8,-9,-27,-56,-26,-53,-12,-13,-14,-15,-16,-17,-18,-19,-10,-50,-29,-30,-31,]),'LESSEREQUAL':([22,23,24,25,26,27,69,70,72,91,101,102,103,104,105,106,107,108,109,113,125,126,127,],[57,-5,-6,-7,-8,-9,-27,-56,-26,-53,-12,-13,-14,-15,-16,-17,-18,-19,-10,-50,-29,-30,-31,]),'GREATEREQUAL':([22,23,24,25,26,27,69,70,72,91,101,102,103,104,105,106,107,108,109,113,125,126,127,],[58,-5,-6,-7,-8,-9,-27,-56,-26,-53,-12,-13,-14,-15,-16,-17,-18,-19,-10,-50,-29,-30,-31,]),'NOTEQUAL':([22,23,24,25,26,27,69,70,72,91,101,102,103,104,105,106,107,108,109,113,125,126,127,],[59,-5,-6,-7,-8,-9,-27,-56,-26,-53,-12,-13,-14,-15,-16,-17,-18,-19,-10,-50,-29,-30,-31,]),'EQUAL':([22,23,24,25,26,27,69,70,72,91,101,102,103,104,105,106,107,108,109,113,125,126,127,],[60,-5,-6,-7,-8,-9,-27,-56,-26,-53,-12,-13,-14,-15,-16,-17,-18,-19,-10,-50,-29,-30,-31,]),'PLUS':([22,23,24,25,26,27,39,40,41,42,43,44,45,52,69,70,71,72,86,87,88,89,90,91,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,125,126,127,131,],[61,-5,-6,-7,-8,-9,61,-7,61,61,61,61,61,61,-27,-56,61,-26,61,61,61,61,61,-53,61,61,61,61,61,61,-12,-13,-14,-15,61,61,61,61,-10,61,61,61,-50,61,-29,-30,-31,61,]),'TIMES':([22,23,24,25,26,27,39,40,41,42,43,44,45,52,69,70,71,72,86,87,88,89,90,91,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,125,126,127,131,],[63,-5,-6,-7,-8,-9,63,-7,63,63,63,63,63,63,-27,-56,63,-26,63,63,63,63,63,-53,63,63,63,63,63,63,63,63,-14,-15,63,63,63,63,-10,63,63,63,-50,63,-29,-30,-31,63,]),'DIVIDE':([22,23,24,25,26,27,39,40,41,42,43,44,45,52,69,70,71,72,86,87,88,89,90,91,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,125,126,127,131,],[64,-5,-6,-7,-8,-9,64,-7,64,64,64,64,64,64,-27,-56,64,-26,64,64,64,64,64,-53,64,64,64,64,64,64,64,64,-14,-15,64,64,64,64,-10,64,64,64,-50,64,-29,-30,-31,64,]),'DOTPLUS':([22,23,24,25,26,27,39,40,41,42,43,44,45,52,69,70,71,72,86,87,88,89,90,91,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,125,126,127,131,],[65,-5,-6,-7,-8,-9,65,-7,65,65,65,65,65,65,-27,-56,65,-26,65,65,65,65,65,-53,65,65,65,65,65,65,-12,-13,-14,-15,65,65,65,65,-10,65,65,65,-50,65,-29,-30,-31,65,]),'DOTMINUS':([22,23,24,25,26,27,39,40,41,42,43,44,45,52,69,70,71,72,86,87,88,89,90,91,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,125,126,127,131,],[66,-5,-6,-7,-8,-9,66,-7,66,66,66,66,66,66,-27,-56,66,-26,66,66,66,66,66,-53,66,66,66,66,66,66,-12,-13,-14,-15,66,66,66,66,-10,66,66,66,-50,66,-29,-30,-31,66,]),'DOTTIMES':([22,23,24,25,26,27,39,40,41,42,43,44,45,52,69,70,71,72,86,87,88,89,90,91,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,125,126,127,131,],[67,-5,-6,-7,-8,-9,67,-7,67,67,67,67,67,67,-27,-56,67,-26,67,67,67,67,67,-53,67,67,67,67,67,67,-12,-13,-14,-15,67,67,67,67,-10,67,67,67,-50,67,-29,-30,-31,67,]),'DOTDIVIDE':([22,23,24,25,26,27,39,40,41,42,43,44,45,52,69,70,71,72,86,87,88,89,90,91,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,125,126,127,131,],[68,-5,-6,-7,-8,-9,68,-7,68,68,68,68,68,68,-27,-56,68,-26,68,68,68,68,68,-53,68,68,68,68,68,68,-12,-13,-14,-15,68,68,68,68,-10,68,68,68,-50,68,-29,-30,-31,68,]),'TRANS':([22,23,24,25,26,27,39,40,41,42,43,44,45,52,69,70,71,72,86,87,88,89,90,91,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,125,126,127,131,],[69,-5,-6,-7,-8,-9,69,-7,69,69,69,69,69,69,-27,-56,69,-26,69,69,69,69,69,-53,69,69,69,69,69,69,-12,-13,-14,-15,69,69,69,69,-10,69,69,69,-50,69,-29,-30,-31,69,]),'COMMA':([23,24,25,26,27,52,69,70,72,77,91,101,102,103,104,105,106,107,108,109,113,125,126,127,],[-5,-6,-7,-8,-9,92,-27,-56,-26,114,-53,-12,-13,-14,-15,-16,-17,-18,-19,-10,-50,-29,-30,-31,]),'RBRACET':([23,24,25,26,27,51,52,69,70,72,76,77,78,91,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,113,122,125,126,127,128,],[-5,-6,-7,-8,-9,91,-54,-27,-56,-26,113,-51,115,-53,-20,-21,-22,-23,-24,-25,-12,-13,-14,-15,-16,-17,-18,-19,-10,-50,-55,-29,-30,-31,-52,]),'RPAREN':([23,24,25,26,27,69,70,71,72,91,101,102,103,104,105,106,107,108,109,110,111,112,113,125,126,127,],[-5,-6,-7,-8,-9,-27,-56,109,-26,-53,-12,-13,-14,-15,-16,-17,-18,-19,-10,125,126,127,-50,-29,-30,-31,]),'RANGE':([23,24,25,26,27,69,70,72,91,101,102,103,104,105,106,107,108,109,113,116,125,126,127,],[-5,-6,-7,-8,-9,-27,-56,-26,-53,-12,-13,-14,-15,-16,-17,-18,-19,-10,-50,130,-29,-30,-31,]),'ELSE':([53,124,],[93,-11,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'instructions':([0,3,54,],[2,13,94,]),'instruction':([0,3,54,],[3,3,3,]),'array':([5,27,33,114,],[19,70,77,77,]),'bool':([6,34,],[21,78,]),'expression':([6,12,14,15,16,17,18,20,28,29,34,46,47,48,49,50,55,56,57,58,59,60,61,62,63,64,65,66,67,68,73,74,75,79,92,130,],[22,39,41,42,43,44,45,52,71,72,22,86,87,88,89,90,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,111,112,116,52,131,]),'matrix':([6,12,14,15,16,17,18,20,28,29,34,46,47,48,49,50,55,56,57,58,59,60,61,62,63,64,65,66,67,68,73,74,75,79,92,130,],[25,25,40,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'list':([20,92,],[51,122,]),'instructions_scope':([21,93,115,131,],[53,123,129,132,]),'arraylist':([33,114,],[76,128,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> instructions','program',1,'p_program','Mparser.py',28),
  ('instructions -> instruction instructions','instructions',2,'p_instructions','Mparser.py',33),
  ('instructions -> <empty>','instructions',0,'p_instructions','Mparser.py',34),
  ('instruction -> SEMICOLON','instruction',1,'p_empty_instruction','Mparser.py',39),
  ('expression -> INTEGER','expression',1,'p_expression_value','Mparser.py',44),
  ('expression -> FLOAT','expression',1,'p_expression_value','Mparser.py',45),
  ('expression -> matrix','expression',1,'p_expression_value','Mparser.py',46),
  ('expression -> STRING','expression',1,'p_expression_value','Mparser.py',47),
  ('expression -> ID','expression',1,'p_expression_ID','Mparser.py',53),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_group_expression','Mparser.py',59),
  ('instructions_scope -> LCURLY instructions RCURLY','instructions_scope',3,'p_instructions_scope','Mparser.py',64),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','Mparser.py',69),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','Mparser.py',70),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','Mparser.py',71),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','Mparser.py',72),
  ('expression -> expression DOTPLUS expression','expression',3,'p_expression_binop','Mparser.py',73),
  ('expression -> expression DOTMINUS expression','expression',3,'p_expression_binop','Mparser.py',74),
  ('expression -> expression DOTTIMES expression','expression',3,'p_expression_binop','Mparser.py',75),
  ('expression -> expression DOTDIVIDE expression','expression',3,'p_expression_binop','Mparser.py',76),
  ('bool -> expression LESSER expression','bool',3,'p_expression_relation','Mparser.py',81),
  ('bool -> expression GREATER expression','bool',3,'p_expression_relation','Mparser.py',82),
  ('bool -> expression LESSEREQUAL expression','bool',3,'p_expression_relation','Mparser.py',83),
  ('bool -> expression GREATEREQUAL expression','bool',3,'p_expression_relation','Mparser.py',84),
  ('bool -> expression NOTEQUAL expression','bool',3,'p_expression_relation','Mparser.py',85),
  ('bool -> expression EQUAL expression','bool',3,'p_expression_relation','Mparser.py',86),
  ('expression -> MINUS expression','expression',2,'p_uminus','Mparser.py',91),
  ('matrix -> expression TRANS','matrix',2,'p_trans','Mparser.py',96),
  ('instruction -> ID ASSIGN matrix SEMICOLON','instruction',4,'p_matrix_assign','Mparser.py',101),
  ('matrix -> ZEROS LPAREN expression RPAREN','matrix',4,'p_matrix_gen','Mparser.py',106),
  ('matrix -> ONES LPAREN expression RPAREN','matrix',4,'p_matrix_gen','Mparser.py',107),
  ('matrix -> EYE LPAREN expression RPAREN','matrix',4,'p_matrix_gen','Mparser.py',108),
  ('instruction -> ID ASSIGN expression SEMICOLON','instruction',4,'p_assign','Mparser.py',113),
  ('instruction -> ID PLUSASSIGN expression SEMICOLON','instruction',4,'p_assign','Mparser.py',114),
  ('instruction -> ID MINUSASSIGN expression SEMICOLON','instruction',4,'p_assign','Mparser.py',115),
  ('instruction -> ID TIMESASSIGN expression SEMICOLON','instruction',4,'p_assign','Mparser.py',116),
  ('instruction -> ID DIVIDEASSIGN expression SEMICOLON','instruction',4,'p_assign','Mparser.py',117),
  ('instruction -> ID array ASSIGN expression SEMICOLON','instruction',5,'p_position_assign','Mparser.py',124),
  ('instruction -> ID array PLUSASSIGN expression SEMICOLON','instruction',5,'p_position_assign','Mparser.py',125),
  ('instruction -> ID array MINUSASSIGN expression SEMICOLON','instruction',5,'p_position_assign','Mparser.py',126),
  ('instruction -> ID array TIMESASSIGN expression SEMICOLON','instruction',5,'p_position_assign','Mparser.py',127),
  ('instruction -> ID array DIVIDEASSIGN expression SEMICOLON','instruction',5,'p_position_assign','Mparser.py',128),
  ('instruction -> IF bool instructions_scope','instruction',3,'p_if_else','Mparser.py',133),
  ('instruction -> IF bool instructions_scope ELSE instructions_scope','instruction',5,'p_if_else','Mparser.py',134),
  ('instruction -> WHILE LBRACET bool RBRACET instructions_scope','instruction',5,'p_while','Mparser.py',139),
  ('instruction -> FOR ID ASSIGN expression RANGE expression instructions_scope','instruction',7,'p_for','Mparser.py',144),
  ('instruction -> BREAK SEMICOLON','instruction',2,'p_special_instruction','Mparser.py',149),
  ('instruction -> CONTINUE SEMICOLON','instruction',2,'p_special_instruction','Mparser.py',150),
  ('instruction -> RETURN SEMICOLON','instruction',2,'p_special_instruction','Mparser.py',151),
  ('instruction -> PRINT expression','instruction',2,'p_print','Mparser.py',156),
  ('matrix -> LBRACET arraylist RBRACET','matrix',3,'p_matrix','Mparser.py',161),
  ('arraylist -> array','arraylist',1,'p_arraylist','Mparser.py',166),
  ('arraylist -> array COMMA arraylist','arraylist',3,'p_arraylist','Mparser.py',167),
  ('array -> LBRACET list RBRACET','array',3,'p_array','Mparser.py',172),
  ('list -> expression','list',1,'p_list','Mparser.py',177),
  ('list -> expression COMMA list','list',3,'p_list','Mparser.py',178),
  ('expression -> ID array','expression',2,'p_array_access','Mparser.py',183),
]
