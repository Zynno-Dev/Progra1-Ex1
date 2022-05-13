#Ejercicio 2

def sumarCadenas(cadena1, cadena2):
    resultado = -1
    nro1 = 0
    nro2 = 0
    try:
        nro1 = float(cadena1)
    except ValueError:
        print("La cadena 1 no tiene un nro valido")
    else:
        try:
            nro2 = float(cadena2)
        except ValueError:
            print("La cadena 2 no tiene un nro valido")
        else:
            resultado = nro1 + nro2
        
    return resultado

def main():
    cadena1 = "3"
    cadena2 = "6"
    res = sumarCadenas(cadena1, cadena2)
    print(res)
    
main()