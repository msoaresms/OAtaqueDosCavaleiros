from funcoes import *

grafo = Grafo(64)

grafoCavalo(grafo)

numEntradas = int(input())

entradas = []
for x in range(numEntradas):
    entradas.append(input())

for x in entradas:
    run(grafo, x)