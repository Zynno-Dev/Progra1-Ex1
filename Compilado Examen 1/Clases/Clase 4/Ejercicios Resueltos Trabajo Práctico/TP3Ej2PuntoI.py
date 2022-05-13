def crearMatriz(filas, columnas):
    matriz = [ [0] * columnas for i in range(filas) ]
    return matriz

def imprimirMatriz(matriz):
    for fila in matriz:
        print(fila)


matriz = crearMatriz(4,4)

inicio = 0
hasta = 1
valor = 0
#primer diagonal
for i in range(inicio, hasta):
    valor += 1
    matriz[i][i] = valor
    
    
#segunda diagonal
inicio = 0
hasta = 1
for i in range( inicio, hasta+1 ):
    for j in range( hasta, inicio-1,-1 ):
        if i!= j:
            valor += 1
            matriz[i][j] = valor


#tercera diagonal, me muevo por fila en orden descendente y columna en orden ascendente
inicio = 0
hasta = 2
for i in range( hasta, inicio-1, -1 ):
    valor += 1
    matriz[i][hasta-i] = valor

#cuarta diagonal, me muevo por fila en orden ascendente y columna en orden ascendente
inicio = 0
hasta = 3
for i in range( inicio, hasta+1, 1 ):
    valor += 1
    matriz[i][hasta-i] = valor

#quinta diagonal, me muevo por fila en orden descendente y columna en orden ascendente
inicio = 0
hasta = 4
for i in range( hasta-1, inicio, -1 ):
    valor += 1
    matriz[i][hasta-i] = valor


#sexta diagonal, me muevo por fila en orden ascendente y columna en orden desascendente
inicio = 2
hasta = 3
for i in range( inicio, hasta+1 ):
    for j in range( hasta, inicio-1,-1 ):
        if i!= j:
            valor += 1
            matriz[i][j] = valor


#ultima diagonal
inicio = 3
hasta = 4
for i in range(inicio, hasta):
    valor += 1
    matriz[i][i] = valor

imprimirMatriz(matriz)
        
