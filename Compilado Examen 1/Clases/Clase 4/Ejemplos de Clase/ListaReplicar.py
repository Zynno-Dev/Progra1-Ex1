from random import randint

lista = [ 1, 2, 3]
print(lista*2)

lista = [ 1, 2, 3]
print(lista*0)

#Crear una lista con el cuadrado de los valores pares
lista = [ 1, 2, 3, 4, 5 ]
listaPares = []
for valor in lista:
    if(valor%2==0):
        listaPares.append( valor**2 )
        
print(listaPares)

#Crear una lista con el cuadrado de los valores pares
#Por Comprensión
lista = [ 1, 2, 3, 4, 5 ]
listaPares = [ valor**2 for valor in lista if valor%2==0]

print(listaPares)


#Crear una lista, los valores pares se deben elevar al cuadrado
#Los valores impares, al cubo.
#Resolver Por Comprensión
lista = [ 1, 2, 3, 4, 5 ]
lista2 = [ valor**2 if valor%2==0 else valor**3 for valor in lista ]

print( lista2)

#Crear una lista con 5 valores ingresados por teclado
lista = [ int(input("Ingrese un nro.:") ) for valor in range(5) ]

print(lista)

#Crear una lista con 10 valores en el 1 y el 100
lista = [ randint(1,101) for valor in range(10) ]

print(lista)

