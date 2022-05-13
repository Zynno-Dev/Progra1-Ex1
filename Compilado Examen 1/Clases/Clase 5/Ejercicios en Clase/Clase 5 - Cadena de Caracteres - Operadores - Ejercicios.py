'''
Dado un texto informar la cantidad de vocales que existen en el mismo.
Dado un texto informar la cantidad de consonantes que existen en el mismo.
Dado un texto informar la cantidad de caracteres sin utilizar la función predefinida len (sin considerar espacios).
'''

cadena = "hola mundo"

vocales = ['a', 'e', 'i', 'o','u']

contadorVocales = 0
contadorConsonantes = 0

#Encontrar todas las vocales

for letra in cadena:
    if letra in vocales:
        contadorVocales += 1
    else:
        if letra != " ":
            contadorConsonantes += 1
        
print("Cantidad de Vocales: ", contadorVocales)
print("Cantidad de Consonantes: ", contadorConsonantes)
print("Total: ", contadorVocales + contadorConsonantes)

print("Solución con subindices:")
contadorVocales = 0
contadorConsonantes = 0

for i in range(len(cadena)):
    letra = cadena[i] 
    if( letra in vocales ):
        contadorVocales += 1
    else:
        if letra != " ":
            contadorConsonantes += 1
        
        
print("Cantidad de Vocales: ", contadorVocales)
print("Cantidad de Consonantes: ", contadorConsonantes)
print("Total: ", contadorVocales + contadorConsonantes)
        