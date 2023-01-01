# List of token names.   This is always required
tokens = (
     'FECHA',
     'VALOR',
     'NULL',
     'NUMERO',
     
     'CATEGORIAS_TAG',
     'RONDA_TAG',
     'PREGUNTAS_TAG',
     'CATEGORIA_TAG',
     'FECHA_TAG',
     'PREGUNTA_TAG',
     'VALOR_TAG',
     'RESPUESTA_TAG',
     'NUMERO_SHOW_TAG',
     
     'DOS_PUNTOS',
     'COMA',
     'CORCHETE_D',
     'CORCHETE_I',
     'CUADRO_D',
     'CUADRO_I',

     'STRING',
     'COMILLAS',
)

def t_FECHA(t):
     r'[0-9]{4}\-[0-9]{2}\-[0-9]{2}'
     return t

def t_VALOR(t): 
     r'(?<="value":\s")(?:\$\d+(?:,\d+)*)'
     return t
     
def t_NULL(t): 
     r'null'
     return t

def t_NUMERO(t):
     r'(?<=\")\d{1,4}(?=\")'
     return t

def t_CATEGORIAS_TAG(t):
     r'categories'
     return t

def t_RONDA_TAG(t):
     r'round'
     return t

def t_PREGUNTAS_TAG(t):
     r'questions'
     return t

def t_CATEGORIA_TAG(t):
     r'category'
     return t

def t_FECHA_TAG(t):
     r'air_date'
     return t

def t_PREGUNTA_TAG(t):
     r'(?<=\")question(?=\")'
     return t

def t_VALOR_TAG(t): 
     r'value'
     return t

def t_RESPUESTA_TAG(t):
     r'answer'
     return t

def t_NUMERO_SHOW_TAG(t):
     r'show_number'
     return t

def t_DOS_PUNTOS(t):
     r':\s'
     return t

def t_COMA(t):
     r','
     return t

def t_CORCHETE_D(t):
     r'\}'
     return t

def t_CORCHETE_I(t):
     r'\{'
     return t

def t_CUADRO_D(t):
     r'\](?=[,\s\}])'
     return t

def t_CUADRO_I(t):
     r'(?<=:\s)\['
     return t

def t_STRING(t): 
     r'(?:\\.?|[^"])+'
     return t

def t_COMILLAS(t):
     r'"'
     return t

# A string containing ignored characters
t_ignore  = ' \t\n\r'

# Error handling rule
def t_error(t):
     print("Illegal character '%s'" % t.value[0])
     t.lexer.skip(1)