def crearMatriz(filas, columnas):
    matriz = [ [0] * columnas for i in range(filas) ]
    return matriz
    
def llenarMatrizPorTeclado(matriz):
    
    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):
            print("Fila: ", fila, " Columna:", columna)
            matriz[fila][columna] = int(input("Valor:"))
    
def ordenearFormaAscendenteFila(matriz):
    
    for fila in matriz:
        fila = fila.sort()
    
def intercambiarFilas( matriz, fila1, fila2):
    aux = matriz[fila1]
    matriz[fila1] = matriz[fila2]
    matriz[fila2] = aux
    
def main():
    #Creamos la matriz
    matriz = crearMatriz(4,4)
    print(matriz)    
    
    #a: numeros impares en la diagonal desde la izquierda
    j = 1
    for i in range( len(matriz) ):
        matriz[i][i] = j
        j +=2
        
    print(matriz)
    
    #b: 3 potencia columna, en la diagonal desde la derecha
    matriz = crearMatriz(4,4)
    j = len(matriz[0])-1
    print(j)
    base = 1
    for i in range( len(matriz) ):
        matriz[i][j]= 3**j
        j = j - 1
    
    print( matriz )
    
    #c
    matriz = crearMatriz(4,4)
    j = 0
    elementos = len(matriz)
    for i in range( elementos ):
        for j in range (i+1):
            matriz[i][j] = elementos-i
            
    print(matriz)
        
main()