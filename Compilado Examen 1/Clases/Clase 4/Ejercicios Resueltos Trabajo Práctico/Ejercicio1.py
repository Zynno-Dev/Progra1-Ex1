'''
a. Cargar nros enteros en una matriz de NxN ingresando los datos desde el teclado
b. Ordenar de forma ascendente cada una de las filas de la matriz
c. Intercambiar dos filas cuyos numeros se reciben como parametros.
'''

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
    #matriz[fila_x], matriz[fila_y] = matriz[fila_y], matriz[fila_x]
    aux = matriz[fila1]
    matriz[fila1] = matriz[fila2]
    matriz[fila2] = aux
    
def main():
    #a
    matriz = crearMatriz(2,2)
    llenarMatrizPorTeclado(matriz)
    print(matriz)
    
    #b
    ordenearFormaAscendenteFila(matriz)
    print(matriz)

    #c
    intercambiarFilas(matriz, 1, 0)
    print(matriz)
main()