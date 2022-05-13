from random import (randint, randrange)
# matriz = []
# filas = 5
# columnas = 5

# for i in range(filas):
#     matriz.append([])
#     for j in range(columnas):
#         matriz[i].append(0)

# print(matriz)
# print ("Forma 2 - Lista por comprension")

# matriz2 = [ [0] * columnas for i in range(filas) ] 
# print(matriz2)

matriz = []

# filas = int(input("Ingrese el numero de filas: "))
# columnas = int(input("Ingrese el numero de columnas: "))
# def crearMatriz2(filas, columnas):
#     matriz = [ [0] * columnas for i in range(filas) ]
#     return matriz

#EJ2

# def crearMatriz2(filas, columnas):
#     matriz = []
#     for i in range(filas):
#         matriz.append([randint(1,50)])
#         for j in range(columnas):
#             matriz[i].append(randint(1,50))
#     return(matriz)

# print(crearMatriz2(5,5))

# EJ3

def crearMatriz3(filas, columnas):
    matriz = []
    for i in range(filas):
        matriz.append([randrange(0,50,2)])
        for j in range(columnas):
            matriz[i].append(randrange(0,50,2))
    return(matriz)

print(crearMatriz3(10,10))