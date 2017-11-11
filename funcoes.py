from Grafo import Grafo
##from Vertice import Vertice

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