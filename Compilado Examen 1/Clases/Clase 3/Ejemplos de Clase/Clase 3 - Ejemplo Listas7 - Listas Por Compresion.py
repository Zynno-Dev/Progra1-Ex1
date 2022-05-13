#Listas por comprensión

lista = [ 1,2,3,4,5,6 ]

print("Cubo de cada valor de la lista")
print( [ i**3 for i in lista ] )

print("Cuadrado de cada valor de la lista")
print( [ i**2 for i in lista ] )

print("Cuadrado de los pares")
print( [ i**2 for i in lista if i%2==0 ] )

