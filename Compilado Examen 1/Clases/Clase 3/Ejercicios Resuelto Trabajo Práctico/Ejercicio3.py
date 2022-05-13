'''
Crear una lista con los cuadrados de los numeros entre 1 y N (ambos incluidos), donde N se ingresa por teclado
Luego, se pide imprimir los ultimos 10 elementos de la lista.
'''
n = int( input("Ingrese el valor de N:") )
         
listaCuadrados = [ valor**2 for valor in range(1,n+1) ]

print("La lista es:", listaCuadrados)
print("Los ultimos 10 elementos: ", listaCuadrados[-10:])

