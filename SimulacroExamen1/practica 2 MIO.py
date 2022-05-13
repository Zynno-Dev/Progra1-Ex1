#generar matriz 5x5
def generar_matriz():
    matriz = []
    for i in range(5):
        matriz.append([])
        for j in range(5):
            matriz[i].append(0)
    return matriz

def imprimir_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=' ')
        print()

def remplazarPorCaracterSegunPosicion(matriz, caracter, posicion):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == posicion[0] and j == posicion[1]:
                matriz[i][j] = caracter
    return matriz

# matrizTest = generar_matriz()
# imprimir_matriz(matrizTest)
# print('---------------')
# remplazarPorCaracterSegunPosicion(matrizTest, 'X', (1,1))
# imprimir_matriz(matrizTest)
# print('---------------')
# remplazarPorCaracterSegunPosicion(matrizTest, 'X', (2,2))
# imprimir_matriz(matrizTest)

print(generar_matriz())