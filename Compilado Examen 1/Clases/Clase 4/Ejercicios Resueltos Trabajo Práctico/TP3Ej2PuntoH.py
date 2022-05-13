def crearMatriz(filas, columnas):
    matriz = [ [0] * columnas for i in range(filas) ]
    return matriz
    
def imprimirMatriz(matriz):
    for fila in matriz:
        print(fila)
        
def main():
    filas = 4
    columnas = 4
    
    #h
    print("Punto h:")
    valor = 0
    matriz = crearMatriz(filas,columnas)

    #primer diagonal
    inicio = 0
    hasta = 1
    for i in range( inicio, hasta ):
        valor += 1
        matriz[i][i] = valor
    
    #segunda diagonal, me muevo por columna en orden decreciente, fila ascendente
    inicio = 0
    hasta = 1
    for i in range( inicio, hasta+1 ):
        for j in range( hasta, inicio-1,-1 ):
            if i!= j:
                valor += 1
                matriz[i][j] = valor
    
    #tercera diagonal, me muevo por columna en orden decreciente, fila ascendente
    inicio = 0
    hasta = 2
    for i in range( inicio, hasta+1 ):
        valor += 1
        matriz[i][hasta-i] = valor
        
    #cuarta diagonal, me muevo por columna en orden decreciente, fila ascendente
    inicio = 0
    hasta = 3
    for i in range( inicio, hasta+1 ):
        valor += 1
        matriz[i][hasta-i] = valor

    #quinta diagonal, me muevo por columna en orden decreciente, fila ascendente
    inicio = 1
    hasta = 4
    for i in range( inicio, hasta ):
        valor += 1
        matriz[i][hasta-i] = valor

    #sexta diagonal, me muevo por columna en orden decreciente, fila ascendente
    inicio = 2
    hasta = 3
    for i in range( inicio, hasta+1 ):
        for j in range( hasta, inicio-1,-1 ):
            if i!= j:
                valor += 1
                matriz[i][j] = valor
    
    inicio = 3
    hasta = 3
    for i in range( inicio, hasta+1 ):
        valor += 1
        matriz[i][i] = valor

    imprimirMatriz(matriz)
    
main()