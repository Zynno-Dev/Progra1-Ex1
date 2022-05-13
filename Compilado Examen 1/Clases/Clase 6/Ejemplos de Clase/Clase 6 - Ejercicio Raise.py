
vocales = ['a','e','i','o','u']

try:
    palabra = (input("Ingrese una palabra:")).lower()
    contador = 0
    for letra in palabra:
        if letra in vocales:
            contador += 1
            
    if contador < 3:
        raise ValueError("La palabra no tiene 3 o mas vocales")
except ValueError as e1:
    print("Error de Valor: ", e1)
except Exception as e2:
    print("Ha ocurrido un error: ", e)
else:
    print("La palabra tiene ", contador, " vocales")
    