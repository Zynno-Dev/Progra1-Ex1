filas = 5
columnas = 5
matriz = []
print("Crear Matriz Forma 1")
for fila in range(filas):
    matriz.append([])
    for columna in range(columnas):
        matriz[fila].append(0)
    
print(matriz)
print("Crear Matriz Forma 2 - Por Replicacion")

matriz2 = []
for fila in range(filas):
    matriz2.append( [0]*columnas )

print (matriz2)