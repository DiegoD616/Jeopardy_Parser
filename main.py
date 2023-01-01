from sys import argv
import json
from FileStatistics import FileStatistics
from ArchivosParser.Parser import Parser
from ArchivosParser.diccionario import Diccionario
from flask import Flask, render_template, url_for, request


app = Flask(__name__)

def getQuestionsDicc(): 
     try:
          return getQuestionsDicc.dicc
     except AttributeError:
          parser = Parser()
          parser.leerArchivo(str(argv[1]))
          getQuestionsDicc.dicc = parser.parseo()
          return getQuestionsDicc.dicc

def getFileStatistics():
     try:
          return getFileStatistics.FileStatistics
     except AttributeError:
          getFileStatistics.FileStatistics = FileStatistics(getQuestionsDicc())
          return getFileStatistics.FileStatistics

@app.route("/")
def index():
     return render_template("general/index.html")

@app.route("/selectCategories")
def selectCategories():
     return render_template("training/selectCategories.html")

@app.route("/train")
def train():
     return render_template("training/train.html")

@app.route("/selectCategories/getEasyQuestions/<categoria>", methods=["POST"])
def getEasyQuestions2(categoria):
     listaFacil = getQuestionsDicc().filtroValor("facil", categoria)
     return json.dumps(getQuestionsDicc().preguntasAleatorias(listaFacil))

@app.route("/train/getEasyQuestions/<categoria>", methods=["POST"])
def getEasyQuestions(categoria):
     listaFacil = getQuestionsDicc().filtroValor("facil", categoria)
     return json.dumps(getQuestionsDicc().preguntasAleatorias(listaFacil))

@app.route("/train/getHardQuestions/<categoria>", methods=["POST"])
def getHardQuestions(categoria):
     listaDificiles = getQuestionsDicc().filtroValor("dificil", categoria)
     return json.dumps(getQuestionsDicc().preguntasAleatorias(listaDificiles))

@app.route("/statistics/categoriesStatistics")
def categorieStatistics():
     return render_template("statistics/categoriesStatistics.html")

@app.route("/statistics/popularCategories", methods=["POST"])
def popularCategories():
     return json.dumps(getFileStatistics().getPopularCategories())

@app.route("/statistics/keyWords/<categoria>/<int:numberWords>", methods=["POST"])
def palabrasClave(categoria, numberWords):
     return json.dumps(getFileStatistics().getKeyWords(categoria, numberWords))
     
@app.errorhandler(404)
def not_found(e):
    return render_template('general/404_not_found.html')

if __name__=="__main__":
    app.run(debug=True)