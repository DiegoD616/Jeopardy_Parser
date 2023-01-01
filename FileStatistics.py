import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

class FileStatistics:
    def __init__(self, questionsDicc):
        self.questionsDicc = questionsDicc
        self.vectorizer = TfidfVectorizer(ngram_range=(1, 3), stop_words='english')

    def getPopularCategories(self):
        popularCategories = {}
        listaCategorias = self.questionsDicc.conseguirCategorias()
        sumaTotal = 0
        
        for categoria in listaCategorias:
            cantidadPreguntas = len(self.questionsDicc.get(categoria))
            popularCategories[categoria] = cantidadPreguntas
            sumaTotal = sumaTotal + cantidadPreguntas

        avg = sumaTotal / len(listaCategorias)
        
        return dict([item for item in popularCategories.items() if item[1] > 3*avg])

    def getKeyWords(self, categoria, numberKeyWords=5):
        listaPreguntas = self.questionsDicc.get(categoria)
        TF_IDF_Matrix = self.vectorizer.fit_transform([p.pregunta for p in listaPreguntas]).toarray().T
        vocab  = list(self.vectorizer.vocabulary_.keys())
        avrs = []
        
        for vector in TF_IDF_Matrix:
            avrs.append(np.average(vector[vector > 0]))
        idxBiggest = np.argsort(-np.array(avrs))[:numberKeyWords]
        
        return [vocab[idx] for idx in idxBiggest]

