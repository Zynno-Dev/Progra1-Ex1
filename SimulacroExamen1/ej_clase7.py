def concatenar_caracter(palabra, caracter):
    palabra_concatenada = ""
    for i in range(len(palabra)):
        palabra_concatenada = palabra_concatenada + palabra[i]
        if i != len(palabra) -1:
            palabra_concatenada = palabra_concatenada + caracter
    return palabra_concatenada

def cambiar_caracter(palabra, caracter_original, caracter_reemplaza):
    palabra_concatenada = ""
    
    for letra in palabra:
        if (letra == caracter_original):
            palabra_concatenada = palabra_concatenada + caracter_reemplaza
        else:
            palabra_concatenada = palabra_concatenada + letra

    return palabra_concatenada


caracter_cambiado = cambiar_caracter("archivo parcial 1.py", " ", "-")
print(caracter_cambiado)


cadena = concatenar_caracter("margen", "-")
print(cadena)

cadena = "margen"

cad1 = ['-']*(len(cadena)*2-1)
print(cad1)

cad1[::2] = cadena
print(cad1)

cad2 = ''.join(cad1)
print(cad2)

#######################################################
cadena = "margen"

char1 = "-"

cad2 = char1.join(list(cadena))
print(cad2)

########################################################

otra_cadena = "archivo parcial 1.py"
otra2 = otra_cadena.replace(" ", "-")
print(otra2)
