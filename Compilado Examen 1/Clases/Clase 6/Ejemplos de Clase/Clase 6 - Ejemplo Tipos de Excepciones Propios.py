class DigitoException( Exception ):
    pass


try:
    n = int(input("Ingrese un digito entre 1 y 10:"))
    
    if n<1 or n>10:
        raise DigitoException("Debe ser entre 1 y 10")
    
except DigitoException as e:
    print("Ha ingresado un digito incorrecto:", e)
except ValueError as e:
    print("Ha ingresado un digito incorrecto")
except Exception as e:
    print("Ha ocurrido un error: ", e)
else:
    print("Todo Ok")
finally:
    print("Fin.")