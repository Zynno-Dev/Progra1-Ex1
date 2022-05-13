import random

n = 3
# def crearMatriz(n):
matriz=[]
    # matrizTraspuesta = []
for f in range(n):
    fila=[]
    for c in range(n):
        azar=random.randint(0, 9)
        fila.append(azar)
    matriz.append(fila)

for i in matriz:
    print(i)
print()

matrizTranspuesta = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for f in range(len(matriz)):
    for c in range(len(matriz[0])):
        matrizTranspuesta[c][f] = matriz[f][c]

for i in matrizTranspuesta:
    print(i)