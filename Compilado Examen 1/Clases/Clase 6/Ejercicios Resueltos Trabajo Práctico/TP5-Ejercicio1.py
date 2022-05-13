class CaracterError(Exception):
    pass

#Ejercicio 1:

def ingresarNroNatural():
    
    nro = int(input("Ingrese un nro. natural:"))
    if nro < 0:
        raise ValueError("No es un nro. positivo mayor a cero.")
    
    return nro


def main():
    try:
        miNumero = ingresarNroNatural()
        print(miNumero)
    except TypeError as e:
        print( "Error de tipo: ", e )
    except ValueError as e:
        print( "El error es: ", e )
    except Exception as e:
        print( "Ha ocurrido un error: ", e )
        
main()