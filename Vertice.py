class Vertice(object):
    numVertice = None
    cor = None
    distancia = None
    predecessor = None

    def __init__(self, pNumVertice, pCor, pDistancia, pPredecessor):
        self.numVertice = pNumVertice
        self.cor = pCor
        self.distancia = pDistancia
        self.predecessor = pPredecessor