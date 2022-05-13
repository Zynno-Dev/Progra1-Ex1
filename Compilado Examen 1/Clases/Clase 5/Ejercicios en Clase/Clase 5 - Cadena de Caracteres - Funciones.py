#Cadena de Caracteres: Ejercitacion
cadena1 = "Hola Mundo!!!"
cadena2 = "Este es un ejemplo para todos los alumnos"

if len(cadena1) > len(cadena2):
    print("Cadena 1 es mayor")
else:
    print("Cadena 2 es mayor")
    
texto = input("Ingrese un texto:")
mayor = max(texto)
menor = min(texto)

print("El mayor unicode es: ", mayor)
print("El menor unicode es: ", menor)

vocales = ['a','e','i','o','u']

for letra in texto:
    if letra in vocales:
        print( "La letra : ", letra, " tiene el unicode: ", ord(letra) )
        