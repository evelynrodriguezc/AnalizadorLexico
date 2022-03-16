import ply.yacc as yacc
from mini_pascal import tokens
import mini_pascal
import sys

VERBOSE = 1

#nombres del grupo
#Alejandro Agudelo Trejos
#Santiago Acosta Rendón
#Daniela Chaux Gallego
#----------------------------------------
def p_program(p):
	'program : PROGRAM ID SEMICOLON declaration_list '
	pass

def p_declaration_list_1(p):
	'declaration_list : declaration_list  declaration'
	pass

def p_declaration_list_2(p):
	'declaration_list : declaration'
	pass

def p_declaration(p):
	'''declaration : var_declaration
				   | block_declaration'''
	pass

def p_var_declaration_1(p):
	'var_declaration :  VAR var_declaration2 COLON type_specifier SEMICOLON'
	pass

def p_var_declaration_2(p):
	'''var_declaration2 : ID COMMA var_declaration2
						| ID'''
	pass

def p_type_specifier_1(p):
	'type_specifier : INTEGER'
	pass

def p_type_specifier_2(p):
	'type_specifier : REAL'
	pass

def p_type_specifier_3(p):
	'type_specifier : CHAR'
	pass

def p_type_specifier_4(p):
	'type_specifier : BOOLEAN'
	pass

def p_type_specifier_5(p):
	'type_specifier : STRING'
	pass

def p_block_declaration(p):
	'block_declaration : BEGIN compount_stmt END'
	pass

def p_compount_stmt(p):
	'compount_stmt : statement_list '
	pass

def p_statement_list_1(p):
	'statement_list : statement_list statement'
	pass

def p_statement_list_2(p):
	'statement_list : empty'
	pass

def p_statement(p):
	'''statement : expression_stmt
				| selection_stmt
				| iteration_stmt
				| io_stmt
	'''
	pass

def p_io_stmt_1(p):
	'io_stmt : WRITELN LPAREN TXT RPAREN SEMICOLON'
	pass
def p_io_stmt_2(p):
	'io_stmt : WRITELN LPAREN TXT RPAREN COMMA expression2 SEMICOLON'
	pass
def p_io_stmt_3(p):
	'io_stmt : READLN LPAREN ID RPAREN SEMICOLON'
	pass
def p_expression2_1(p):
	'''expression2 : expression COMMA expression2
					| expression '''
	pass
def p_expression_stmt_1(p):
	'expression_stmt : expression SEMICOLON'
	pass

def p_expression_stmt_2(p):
	'expression_stmt : SEMICOLON'
	pass

def p_selection_stmt_1(p):
	'selection_stmt : IF LPAREN expression RPAREN THEN statement ELSE statement'
	pass
def p_selection_stmt_2(p):
	'selection_stmt : IF LPAREN expression RPAREN THEN BEGIN statement END ELSE statement'
	pass
def p_selection_stmt_3(p):
	'selection_stmt : IF LPAREN expression RPAREN THEN BEGIN statement END ELSE  BEGIN statement END'
	pass
def p_selection_stmt_4(p):
	'selection_stmt : IF LPAREN expression RPAREN THEN statement ELSE BEGIN statement END'
	pass
def p_selection_stmt_5(p):
	'selection_stmt : IF LPAREN expression RPAREN THEN statement'
	pass
def p_selection_stmt_6(p):
	'selection_stmt : IF LPAREN expression RPAREN THEN BEGIN statement END'
	pass

def p_iteration_stmt_1(p):
	'iteration_stmt : WHILE LPAREN expression RPAREN DO BEGIN statement END SEMICOLON'
	pass

def p_iteration_stmt_2(p):
	'iteration_stmt : WHILE LPAREN expression RPAREN DO BEGIN statement END'
	pass

def p_expression_1(p):
	'expression : var EQUAL expression'
	pass

def p_expression_2(p):
	'expression : simple_expression'
	pass

def p_expression_3(p):
	'expression : var ASSIGNMENT expression'
	pass

def p_var_1(p):
	'var : ID'
	pass

def p_simple_expression_1(p):
	'simple_expression : additive_expression relop additive_expression'
	pass

def p_simple_expression_2(p):
	'simple_expression : additive_expression'
	pass

def p_relop(p):
	'''relop : LESS
			| LESSEQUAL
			| GREATER
			| GREATEREQUAL
			| DEQUAL
			| DISTINT
	'''
	pass

def p_additive_expression_1(p):
	'''additive_expression : additive_expression addop term

        '''
	pass

def p_additive_expression_2(p):
	'additive_expression : term'
	pass

def p_addop(p):
	'''addop : PLUS
			| MINUS
	'''
	pass

def p_term_1(p):
	'term : term mulop factor'
	pass

def p_term_2(p):
	'term : factor'
	pass

def p_mulop(p):
	'''mulop : 	TIMES
				| DIVIDE
	'''
	pass

def p_factor_1(p):
	'factor : LPAREN expression RPAREN'
	pass

def p_factor_2(p):
	'factor : var'
	pass

def p_factor_4(p):
	'factor : NUMBER'
	pass

def p_empty(p):
	'empty :'
	pass

def p_error(p):
	if VERBOSE:
		if p is not None:
			print ("ERROR SINTACTICO EN LA LINEA " + str(p.lexer.lineno) + " NO SE ESPERABA EL Token  " + str(p.value))
		else:
			pass#print ("ERROR SINTACTICO EN LA LINEA: " + str(cminus_lexer.lexer.lineno))
	else:
		raise Exception('syntax', 'error')


parser = yacc.yacc()

if __name__ == '__main__':

	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'evaluacion_pascal.PASCAL'

	f = open(fin, 'r')
	data = f.read()
	#print (data)
	parser.parse(data, tracking=True)
	print("Amiguito, tengo el placer de informar que Tu parser reconocio correctamente todo")
	#input()
