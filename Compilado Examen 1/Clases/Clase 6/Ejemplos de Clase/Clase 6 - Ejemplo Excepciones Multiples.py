try:
    n = int(input("ingrese un valor:"))
    resultado = 5/n
except TypeError:
    print("Ha ingresado en valor un tipo incorrecto")
except ValueError:
    print("Ha ingresado el valor del tipo texto")
except ZeroDivisionError:
    print("Ha ingresado el valor 0")
except Exception as e:
    print("Ha ocurrido un error: ", e)
finally:
    print("Fin.")
            