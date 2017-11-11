class Grafo(object):
    adj = []
    ordem = 0
    tamanho = 0

    def __init__(self, pN):
        self.inicializar(pN)

    @property
    def destroi(self):
        self.adj.clear()
        self.ordem = 0
        self.tamanho = 0

    def inicializar(self, pN):
        if self.ordem != 0 : self.destroi
        self.ordem = pN
        self.tamanho = 0
        self.adj = [[] for i in range(pN+1)]

    def inserirAresta(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)
        self.tamanho = self.tamanho+1

    @property
    def mostrar(self):
        for i in range(1, self.ordem+1):
            print(str(i) +" - ", end='')
            print(self.adj[i])