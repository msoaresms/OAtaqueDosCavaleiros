from Grafo import Grafo
from Vertice import Vertice

def coordParaVertice(i, j):
    if i == 1:
        return i*j
    else:
        return (8*(i-1))+j

def existeAresta(li, lj, ci, cj):
    n1 = abs(li-lj)
    n2 = abs(ci-cj)
    return n1+n2 == 3

def grafoCavalo(grafo):
    if grafo.ordem == 64:
        coordenadas = []
        coordenadas.append((0,0))
        for i in range(1, 9):
            for j in range(1, 9):
                coordenadas.append((i, j))

        for i in range(1, 65):
            for j in range(1, 65):
                if i != j and i < j:
                    li = coordenadas[i][1]
                    lj = coordenadas[j][1]
                    ci = coordenadas[i][0]
                    cj = coordenadas[j][0]

                    if li != lj and ci != cj and existeAresta(li, lj, ci, cj):
                        grafo.inserirAresta(i, j)

    else:
        print("A ORDEM DO GRAFO PRECISA SER IGUAL A 64")

def BFS(grafo, s):
    listaAdj = grafo.adj
    vertices = []
    for i in range(0, grafo.ordem+1):
        vertices.append(Vertice(i, 0, float("inf"), -1))
    vertices[s].cor = 1
    vertices[s].distancia = 0
    vertices[s].predecessor = -1

    fila = []
    fila.append(vertices[s])
    while len(fila) != 0:
        u = fila.pop(0)
        uAdj = listaAdj[u.numVertice]
        for x in uAdj:
            if vertices[x].cor == 0:
                vertices[x].cor = 1
                vertices[x].distancia = u.distancia+1
                vertices[x].predecessor = u.numVertice
                fila.append(vertices[x])
        vertices[u.numVertice].cor = 2
    return vertices

def run(grafo, entrada):
    posicoes = entrada.split()
    for i in range(len(posicoes)):
        aux = posicoes[i]
        posicoes[i] = coordParaVertice(ord(aux[0])-96, ord(aux[1])-48)

    rei = posicoes[4]
    distancias = []
    for i in range(len(posicoes)-1):
        bfsResultado = BFS(grafo, posicoes[i])
        predecessorRei = bfsResultado[rei].predecessor
        aux = bfsResultado[predecessorRei]
        distancias.append(aux.distancia)

    menor = min(distancias)
    for i in range(distancias.count(menor)):
        print(str(menor)+" ", end='')
    print()