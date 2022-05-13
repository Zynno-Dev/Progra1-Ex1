from random import randint

def crearMatriz(filas, columnas):
    matriz = [ [0] * columnas for i in range(filas) ]
    return matriz

def imprimirMatriz(matriz):
    for fila in matriz:
        print(fila)
        
def existeEnMatriz(matriz, elemento):
    existe = False
    for fila in matriz:
        if elemento in fila:
            existe = True
            
    return existe

def rellenarMatrizAzar(n):
    
    matriz = crearMatriz(n,n)
    
    for i in range(n):
        for j in range(n):
            nroAzar = randint(0, n**2)
            while existeEnMatriz(matriz,nroAzar) == True:
                nroAzar = randint(0, n**2)
                
            matriz[i][j] = nroAzar
        
    return matriz          

def main():
    n = int( input("Ingrese n:"))
    matriz = rellenarMatrizAzar(n)
    imprimirMatriz(matriz)


main()