try:
    n = int(input("Ingrese un digito entre 1 y 10:"))
    
    if n<1 or n>10:
        raise ValueError("Debe ser entre 1 y 10")
    
except ValueError as e:
    print(e)
    print("Ha ingresado un digito incorrecto")
except Exception as e:
    print("Ha ocurrido un error: ", e)
    