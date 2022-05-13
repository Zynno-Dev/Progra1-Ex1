
def crearMatriz(filas, columnas):
    matriz = [ [0] * columnas for i in range(filas) ]
    return matriz


def imprimirMatriz(matriz):
    for fila in matriz:
        print(fila)
        
        

filas = 4
columnas = 4

valor = 0

inicio = 0
hasta = 3

matriz = crearMatriz( filas, columnas)
imprimirMatriz(matriz)
ciclos = 2

for j in range(ciclos):

    #completamos la primer fila (avanzo por columna de izquierda a derecha)
    for i in range(inicio, hasta+1, 1):
        valor += 1
        matriz[inicio][i] = valor


    #completar la ultima columna (avanzo por fila de arriba hacia abajo)
    for i in range(inicio+1, hasta+1, 1):
        valor +=1
        matriz[i][hasta] = valor


    #completar la ultima fila (avanzo por columna de derecha a izquierda)
    for i in range( hasta-1, inicio-1, -1):
        valor +=1
        matriz[hasta][i] = valor

    #completar la ultima columna (avanzo por fila de abajo hacia arriba)
    for i in range( hasta-1, inicio, -1 ):
        valor +=1
        matriz[i][inicio] = valor

    inicio += 1
    hasta -= 1
    

imprimirMatriz(matriz)
