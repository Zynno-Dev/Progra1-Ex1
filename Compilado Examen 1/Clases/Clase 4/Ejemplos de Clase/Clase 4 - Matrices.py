#Clase 4: Matrices
#Creamos una matriz de 2x2

matriz = [ [ 1, 2 ] , [ 3, 4 ] ]

print(matriz)
print("Acceder Forma Basica")
print( matriz[0][0] )
print( matriz[0][1] )
print( matriz[1][0] )
print( matriz[1][1] )

print( "Acceder con For 1")
for fila in matriz:
    for columna in fila:
        print (columna)
        
print( "Acceder a la primer fila")
for fila in matriz[0]:
    print(fila)
    


