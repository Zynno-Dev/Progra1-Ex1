from random import randint
'''
Escribir una función que cree una matriz de N filas y N columnas.
Escribir una función que llene una matriz con valores aleatorios de 1 al 100.
Escribir una función que retorne el o los valores repetidos en la matriz.
Escribir el programa que solicite al usuario el ingreso de la dimensión de la matriz (N) e invoque a las funciones de llenado y valores repetidos.
'''

def crearMatriz(filas, columnas):
    matriz = [ [0] * columnas for i in range(filas) ]
    return matriz

def llenarMatrizNrosAleatorios(matrix):
    for fila in range(len(matrix)):
        for columna in range(len(matrix[0])):
            matrix[fila][columna] = randint(1,10)
    
#Retorna la cantidad de ocurrencias de un elemento en una matriz, sino existe retorna -1        
def buscarEnMatriz(matriz, elemento):
    ocurrencias = 0
    
    for fila in matriz:
        if elemento in fila:
            ocurrencias += 1
            
    if ocurrencias == 0:
        ocurrencias = -1
        
    return ocurrencias

def repetidos(matrix):
    
    lRepetidos = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            elemento = matrix[i][j]
            if ( buscarEnMatriz(matrix, elemento) > 1 and elemento not in lRepetidos ):
                lRepetidos.append( elemento )

    return lRepetidos


def main():
    #crear matriz
    matriz = crearMatriz(4,4)
    print( matriz )
    
    #llenar con nros al azar
    llenarMatrizNrosAleatorios(matriz)
    print( matriz )
    
    #buscar repetidos
    lista = repetidos(matriz)
    print( lista )
    
main()