from datetime import datetime
import json

class Pregunta:
    def __init__(self, categoria, fecha, pregunta, valor, respuesta, ronda, numeroShow):
        self.categoria = categoria
        self.fecha = datetime.strptime(fecha, "%Y-%m-%d")
        self.pregunta = pregunta
        self.valor = int(valor.replace("$","").replace(",","")) if valor != "null" else 0
        self.respuesta = respuesta
        self.ronda = ronda
        self.numeroShow = int(numeroShow)

    def __repr__(self):
        return "{Pregunta:" + self.pregunta + ",Respuesta:" + str(self.respuesta) + ",Valor:" + str(self.valor)+"}" 

    def __str__(self):
        return "{Pregunta:" + self.pregunta + ",Respuesta:" + str(self.respuesta) + ",Valor:" + str(self.valor)+"}" 
    
    def getValor(self):
        return self.valor

    def getPregunta(self):
        return self.pregunta

    def getRespuesta(self):
        return self.respuesta
    def getCategoria(self):
        return self.categoria

    def toJson(self):
        members = {"categoria": self.categoria,"pregunta":self.pregunta,"valor":self.valor,"respuesta":self.respuesta}
        return json.dumps(members)

        
    