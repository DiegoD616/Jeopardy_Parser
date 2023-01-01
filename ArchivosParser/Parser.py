import ArchivosParser.ply.lex as lex
from ArchivosParser.parserRules import *
import ArchivosParser.ply.yacc as yacc
from ArchivosParser.sintaxRules import *

class Parser:
    def __init__(self):
        self.lexer = lex.lex()
        self.parser = yacc.yacc()
        self.data = ""

    def leerArchivo(self, nombreArchivo):
        with open(nombreArchivo, 'r') as file:
          self.data = file.read()
          self.lexer.input(self.data)

    def parseo(self):
        return self.parser.parse(self.data)