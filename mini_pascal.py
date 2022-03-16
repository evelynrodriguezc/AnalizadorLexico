import ply.lex as lex
import sys

# list of tokens
tokens = (
    # Reserverd words
    'INTEGER',
    'REAL',
    'CHAR',
    'BOOLEAN',
    'STRING',
    'CLASS',
    'CREATE',
    'CONSTRUCTOR',
    'ARRAY',    #Definición de variables (arrays)
    'BEGIN',    #Inicio de procedimiento
    'CONST',    #Definición de constantes
    'DIV',      #División entera
    'DOWNTO',   #Bucle FOR - TO/DOWNTO - DO - END
    'END',      #Término de saltos condicionales y bucles
    'ENDC',
    'FOR',      #Bucle FOR - TO/DOWNTO - DO - END
    'FUNCTION', #Definición de función
    'IF',       #Salto condicional IF - THEN - ELSE - END
    'IN',       #Inclusión de conjuntos
    'OR',       #Disyunción lógica inclusiva
    'REPEAT',   #Bucle REPEAT - UNTIL
    'TO',       #Bucle FOR - TO/DOWNTO - DO - END
    'UNIT',     #Interfaz de programa dado
    'USES',     #Definicion para usar una libreria
    'WITH',     #Definicion para utilizar las variables de un registro.
    'AND',      #Conjunción lógica
    'CASE',     #Salto condicional SWITCH - CASE - END
    'DO',       #Bucle FOR - TO/DOWNTO - DO - END
    'ELSE',     #Salto condicional IF - THEN - ELSE - END
    'FILE',     #Definicion de un archivo
    'GOTO',     #Salto incondicional
    'MOD',      #Resto de división entera
    'NOT',      #Negación lógica
    'OF',       #Definición de variables
    'PROCEDURE',#Definición de procedimiento
    'RECORD',   #Definición de variables (registros)
    'SET',      #Definición de variables (conjuntos)
    'THEN',     #Salto condicional IF - THEN - ELSE - END
    'TYPE',     #Definición de tipos
    'UNTIL',    #Bucle REPEAT - UNTIL
    'VAR',      #Definición de variables
    'WHILE',    #Bucle WHILE - DO - END
    'XOR',      #Disyunción lógica exclusiva
    'SHL',      #Desplazar a la izquierda
    'SHR',      #Desplazar a la derecha
    'WRITELN',  #Mostrar en pantalla
    'READLN',   #Leer
    'PROGRAM',  #Definicion


    # Symbols
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LESS',
    'LESSEQUAL',
    'GREATER',
    'GREATEREQUAL',
    'EQUAL',
    'DEQUAL',
    'DISTINT',
    'SEMICOLON',
    'COMMA',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LBLOCK',
    'RBLOCK',
    'COLON',
    'HASHTAG',
    'DOT',
    'POINTER',
    'ASSIGNMENT',
    'QUOTES',

    # Others
    'ID',
    'NUMBER',
    'TXT',
    'FIN',
)

# Regular expressions rules for a simple tokens
t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_EQUAL  = r'='
t_DISTINT = r'!'
t_LESS   = r'<'
t_GREATER = r'>'
t_SEMICOLON = ';'
t_COMMA  = r','
t_LPAREN = r'\('
t_RPAREN  = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBLOCK   = r'{'
t_RBLOCK   = r'}'
t_COLON   = r':'
t_HASHTAG = r'\#'
t_DOT = r'\.'
t_POINTER = r'\^'
t_QUOTES = r'\''

def t_INTEGER(t):
    r'integer'
    return t

def t_REAL(t):
    r'real'
    return t

def t_CHAR(t):
    r'char'
    return t

def t_BOOLEAN(t):
    r'boolean'
    return t

def t_STRING(t):
    r'string'
    return t

def t_ARRAY(t):
    r'array'
    return t

def t_CLASS(t):
    r'class'
    return t

def t_CREATE(t):
    r'create'
    return t

def t_CONSTRUCTOR(t):
    r'constructor'
    return t

def t_BEGIN(t):
    r'begin'
    return t

def t_CONST(t):
    r'const'
    return t

def t_DIV(t):
    r'div'
    return t

def t_DOWNTO(t):
    r'downto'
    return t

'''def t_END(t):
    r'end'
    return t'''

def t_FOR(t):
    r'for'
    return t

def t_FUNCTION(t):
    r'function'
    return t

def t_IF(t):
    r'if'
    return t

def t_IN(t):
    r'in'
    return t

def t_OR(t):
    r'or'
    return t

def t_REPEAT(t):
    r'repeat'
    return t

def t_TO(t):
    r'to'
    return t

def t_UNIT(t):
    r'unit'
    return t

def t_USES(t):
    r'uses'
    return t

def t_WITH(t):
	r'with'
	return t

def t_AND(t):
    r'and'
    return t

def t_CASE(t):
    r'case'
    return t

def t_DO(t):
	r'do'
	return t

def t_ELSE(t):
    r'else'
    return t

def t_FILE(t):
	r'file'
	return t

def t_GOTO(t):
	r'goto'
	return t

def t_MOD(t):
	r'mod'
	return t

def t_NOT(t):
	r'not'
	return t

def t_OF(t):
	r'of'
	return t

def t_PROCEDURE(t):
	r'procedure'
	return t

def t_RECORD(t):
	r'record'
	return t

def t_SET(t):
	r'set'
	return t

def t_THEN(t):
	r'then'
	return t

def t_TYPE(t):
	r'type'
	return t

def t_UNTIL(t):
	r'until'
	return t

def t_VAR(t):
	r'var'
	return t

def t_WHILE(t):
	r'while'
	return t

def t_XOR(t):
	r'xor'
	return t

def t_SHL(t):
	r'shl'
	return t

def t_SHR(t):
	r'shr'
	return t

def t_WRITELN(t):
	r'writeln'
	return t

def t_READLN(t):
	r'readln'
	return t

def t_PROGRAM(t):
    r'program'
    return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_TXT(t):
    r'(\')(\w|\s|\d)+(\s|_|\d|\w)*(\')'
    return t

def t_ENDC(t):
    r'end (\;)'
    return t

def t_END(t):
    r'end (\.)'
    return t

def t_ID(t):
    r'\w+(_\d\w)*'
    return t

def t_LESSEQUAL(t):
	r'<='
	return t

def t_GREATEREQUAL(t):
	r'>='
	return t

def t_DEQUAL(t):
	r'!='
	return t

def t_ASSIGNMENT(t):
    r':='
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_comments(t):
    r'LBLOCK (ID)? RBLOCK'
    t.lexer.lineno += t.value.count('\n')

def t_comments_C99(t):
    r'LPAREN TIMES (ID)? TIMES RPAREN'
    t.lexer.lineno += 1

def t_error(t):
    print ("Lexical error: " + str(t.value[0]))
    t.lexer.skip(1)


def test(data, lexer):
	lexer.input(data)
	while True:
		tok = lexer.token()
		if not tok:
			break
		print (tok)

lexer = lex.lex()


if __name__ == '__main__':
	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'evaluacion_pascal.PASCAL'
	f = open(fin, 'r')
	data = f.read()
	print (data)
	lexer.input(data)
	test(data, lexer)
	input()
