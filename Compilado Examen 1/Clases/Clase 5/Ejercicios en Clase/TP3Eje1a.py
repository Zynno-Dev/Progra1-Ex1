from random import randint

#Crear una matriz de NxN

#Funcion para crear una matriz dadas sus filas y columnas
def crearMatriz(filas,columnas):
    matriz = [ [0]*columnas for i in range(filas) ]
    return matriz 

def crearMatrizTradicional(filas, columnas):
    matriz = []
    for i in range(filas):
        matriz.append([])
        for j in range( columnas ):
            matriz[i].append(0)
        
    return matriz
         
def llenarMatrizConEnteros(filas,columnas):
    matriz = []
    for i in range(filas):
        matriz.append([])
        for j in range( columnas ):
            matriz[i].append(randint(1,100))
    
    
    return matriz 
   
def intercambiarFila( matriz, fila1, fila2 ):
    aux = matriz[fila1]
    matriz[fila1] = matriz[fila2]
    matriz[fila2] = aux

def intercambiarColumnas(matriz, columna1, columna2 ):
    for i in range(len(matriz) ):
        aux = matriz[i][columna1]
        matriz[i][columna1] = matriz[i][columna2]
        matriz[i][columna2] = aux
        
def diagonal(matriz):
    j = 1
    for i in range(len(matriz) ):
        matriz[i][i] = j
        j = j + 2
    

filas = int(input("Ingrese nro. de filas:"))
columnas = int(input("Ingrese nro. de columnas:"))

miMatriz = crearMatriz(filas,columnas)
print(miMatriz)

miMatriz2 = crearMatrizTradicional(filas,columnas)
print(miMatriz2)
    
miMatriz3 = llenarMatrizConEnteros(filas,columnas)
print(miMatriz3)


intercambiarFila(miMatriz3, 0,1)
print(miMatriz3)

miMatriz4 = crearMatrizTradicional(filas,columnas)
diagonal(miMatriz4)
print(miMatriz4)
