#Cadena de Caracteres: Metodos

cadena = "Hola Mundo"

print( cadena.split() )

cadena = "Juan Perez, 345534, CABA"
lista = cadena.split(sep=",") 

nombre = lista[0]
telefono = lista[1]
localidad = lista[2]

print(nombre)

opcion = input("Ingrese una opcion:")
if opcion.isdigit():
    print("es un valor numerico")
else:
    print("no es una opcion valida")
  
#Si nos piden un valor numerico de X digitos
opcion = input("Ingrese una opcion:")
if( opcion.isdigit() and len(opcion)==4):
    print("es un valor numerico de 4 digitos")
else:
    print("no es una opcion valida")
    
    

