#Ejemplos de Clase Cadena de Caracteres: Operadores
cadena = "Hola" + " Mundo!!!"
print( cadena )

cadena = "Hola" + " Mundo!!!" + str(2022)
print( cadena )

#Podemos multiplicar una cadena nueva o una variable del tipo str
cadena = "Hola "*3
print(cadena)

cadena = cadena * 3
print(cadena)

cadena += " Clase Programacion I"
print(cadena)

#Es igual al anterior
cadena = cadena + " Clase Programacion I"

#Operador in
cadena = "Este es un texto para el operador 'in'"

if "in" in cadena:
    print("existe")
else:
    print("no existe")
    
if cadena == "Este es un texto para el operador 'in'":
    print( "es igual")
else:
    print( "no es igual")
    
