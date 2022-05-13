
def imprimirMatriz( matriz ):
    
    filas = len(matriz)
    columnas = len(matriz[0])
    print("[")
    for i in range(filas):

        if i < filas-1:
            print( matriz[i], end=",\n" )
        else:
            print( matriz[i])
        
    print("]")
            
    
matriz = [ [ 1,2 ], [3,4] ]


matriz = [ [ 1, 2 ],
           [ 3, 4 ],
           [ 5, 6 ] ]
           
matriz = [ [ 0, 0 ],
           [ 0, 0 ],
           [ 0, 0 ] ]


filas = 3
columnas = 3
matriz =[]
for i in range(filas):
    matriz.append([0]*columnas)

print( matriz )


filas = 3
columnas = 3
matriz =[]
for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        matriz[i].append(0)

print( matriz )


#Crear una matriz de 3x4
filas = 3
columnas = 4
matriz = [ [0] * columnas for i in range(filas) ]

print(matriz)

imprimirMatriz( matriz )
           
