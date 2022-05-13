from random import randint, randrange

#Ejercicios en Clase
#1. Crear una funcion para crear una matriz de n,m
def crearMatriz( filas, columnas ):
    matriz = [ [0]*columnas for i in range(filas) ]
    return matriz

def crearMatrizAleatorios(filas, columnas):
    #matriz = [ [randint(1,50)]*columnas for i in range(filas) ]
    matriz = []
    for fila in range(filas):
        matriz.append([])
        for columna in range(columnas):
            matriz[fila].append( randint(1,50) )
    return matriz

def crearMatrizAleatoriosPorComprension(filas, columnas):
    matriz = []
    for fila in range(filas):
        matriz.append( [randint(1,50) for i in range(columnas) ] )
            
    return matriz

def crearMatrizPares(filas, columnas):
    matriz = []
    for fila in range(filas):
        matriz.append( [randrange(0,100,2) for i in range(columnas) ] )
            
    return matriz
    
def imprimirMatriz(matriz):
    print("[")
    for fila in matriz:
        print(fila)
    
    print("]")
#Cuerpo principal del programa
def main():
    
    matriz1 = crearMatriz(3,3)
    print(matriz1)
    
    matriz2 = crearMatrizAleatorios(3,3)
    print(matriz2)

    matriz3 = crearMatrizAleatoriosPorComprension(3,3)
    print(matriz3)
    
    matriz4 = crearMatrizPares(3,3)
    print(matriz4)
    
    imprimirMatriz(matriz4)
    
main()