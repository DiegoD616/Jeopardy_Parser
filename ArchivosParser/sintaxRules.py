from ArchivosParser.Pregunta import Pregunta
from ArchivosParser.diccionario import Diccionario

def p_archivo(p):
    'archivo : CORCHETE_I categorias COMA preguntas CORCHETE_D'
    p[0] = Diccionario(p[2], p[4])

def p_categorias(p):
    'categorias : COMILLAS CATEGORIAS_TAG COMILLAS DOS_PUNTOS CUADRO_I listaCategorias CUADRO_D'
    p[0] = p[6]

def p_preguntas(p):
    'preguntas : COMILLAS PREGUNTAS_TAG COMILLAS DOS_PUNTOS CUADRO_I listaPreguntas CUADRO_D'
    p[0] = p[6]

def p_listaCategorias(p):
     '''listaCategorias : itemCategoria COMA listaCategorias 
                       | itemCategoria'''
     if len(p) > 2:
          p[3].append(p[1])
          p[0] = p[3]
     else:
          listaItems = [p[1]]
          p[0] = listaItems

def p_itemCategoria(p):
     '''itemCategoria : COMILLAS STRING COMILLAS
                      | COMILLAS NUMERO COMILLAS'''
     p[0] = p[2]

def p_listaPreguntas(p):
     '''listaPreguntas : itemPregunta COMA listaPreguntas 
                    | itemPregunta'''
     if len(p) > 2:
          p[3].append(p[1])
          p[0] = p[3]
     else:
          listaItems = [p[1]]
          p[0] = listaItems

def p_itemPregunta(p):
     'itemPregunta : CORCHETE_I categoria COMA fecha COMA pregunta COMA valor COMA respuesta COMA ronda COMA numeroShow CORCHETE_D'
     p[0] = (p[2],p[4],p[6],p[8],p[10],p[12],p[14])
     
def p_categoria(p):
     '''categoria : COMILLAS CATEGORIA_TAG COMILLAS DOS_PUNTOS COMILLAS STRING COMILLAS
                  | COMILLAS CATEGORIA_TAG COMILLAS DOS_PUNTOS COMILLAS NUMERO COMILLAS'''
     p[0] = p[6]

def p_fecha(p):
     'fecha : COMILLAS FECHA_TAG COMILLAS DOS_PUNTOS COMILLAS FECHA COMILLAS'
     p[0] = p[6]

def p_pregunta(p):
     'pregunta : COMILLAS PREGUNTA_TAG COMILLAS DOS_PUNTOS COMILLAS STRING COMILLAS'
     p[0] = p[6]

def p_valor(p):
     '''valor : COMILLAS VALOR_TAG COMILLAS DOS_PUNTOS COMILLAS VALOR COMILLAS
              | COMILLAS VALOR_TAG COMILLAS DOS_PUNTOS NULL'''
     if len(p) > 6:
          p[0] = p[6]
     else:
          p[0] = p[5]

def p_respuesta(p):
     '''respuesta : COMILLAS RESPUESTA_TAG COMILLAS DOS_PUNTOS COMILLAS STRING COMILLAS
                  | COMILLAS RESPUESTA_TAG COMILLAS DOS_PUNTOS COMILLAS NUMERO COMILLAS'''
     p[0] = p[6]

def p_ronda(p):
     'ronda : COMILLAS RONDA_TAG COMILLAS DOS_PUNTOS COMILLAS STRING COMILLAS' 
     p[0] = p[6]

def p_numeroShow(p):
     'numeroShow : COMILLAS NUMERO_SHOW_TAG COMILLAS DOS_PUNTOS COMILLAS NUMERO COMILLAS'
     p[0] = p[6]

def p_error(p):
    print(f"Error de sintaxis debido al token {p}")