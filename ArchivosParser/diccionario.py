from unicodedata import category
from ArchivosParser.Pregunta import Pregunta
import random


class Diccionario:
    def __init__(self, listaCategoriasRecibida, listaPreguntasRecibida):
        self.diccionario = dict()
        for categoria in listaCategoriasRecibida:
            listaPreguntas = []
            for pregunta in listaPreguntasRecibida:
                if pregunta[0] == categoria: 
                    listaPreguntas.append(Pregunta(*pregunta))
            self.diccionario[categoria] = listaPreguntas

    def vaciar(self):
        self.diccionario.clean()

    def get(self, categoria):
        return self.diccionario.get(categoria)
    
    def conseguirCategorias(self):
        return list(self.diccionario.keys())

    def conseguirPreguntas(self):
        return list(self.diccionario.values())

    def filtroCategoria(self,categoria):
        return list(self.diccionario[categoria])

    def pop(self,categoria):
        self.diccionario.pop(categoria)
    
    def filtroValor(self,dificultad,ncategoria):
        listaPreguntas= []
        for categoria in self.diccionario:
            temp = self.diccionario[categoria]
            for pregunta in temp:
                if dificultad == "facil":
                    if pregunta.getValor() <= 800 and pregunta.getCategoria()==ncategoria:
                        listaPreguntas.append((
                            pregunta.categoria,
                            pregunta.pregunta.replace("'",""),
                            pregunta.respuesta,
                            pregunta.valor
                            ))
                else:
                    if pregunta.getValor() > 800 and pregunta.getCategoria()==ncategoria:
                        listaPreguntas.append((
                            pregunta.categoria,
                            pregunta.pregunta.replace("'",""),
                            pregunta.respuesta,
                            pregunta.valor
                            ))
        return listaPreguntas
        
    def preguntasAleatorias(self,listaPreguntas):
        listaAleatoria=[]
        tamanoFaciles =0 
        tamanoDificiles=0
        for m in listaPreguntas:
            if(m[3] <= 800):
                tamanoFaciles += 1
            else:
                tamanoDificiles += 1
        if(listaPreguntas[1][3] <=800 ):
            for p in range(tamanoFaciles if tamanoFaciles < 5 else 5 ): 
                numero = random.randint(0,len(listaPreguntas)-1)
                while numero in listaAleatoria:
                    numero = random.randint(0,len(listaPreguntas)-1) 
                listaAleatoria.append(numero)   
        else:
            for q in range(tamanoDificiles if tamanoDificiles < 10 else 10):
                numero = random.randint(0,len(listaPreguntas)-1)
                while numero in listaAleatoria:
                    numero = random.randint(0,len(listaPreguntas)-1)
                listaAleatoria.append(numero)
                
        return [listaPreguntas[idx] for idx in listaAleatoria] 

            

    def __str__(self):
        return "Lista de Categorias: \n" + "\n".join(self.diccionario.keys()) +"\n" + "Lista de Preguntas: \n" + "\n".join(map(str,self.diccionario.values()))
