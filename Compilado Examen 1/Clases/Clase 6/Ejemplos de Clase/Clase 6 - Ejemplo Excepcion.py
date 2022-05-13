
nro1 = int(input("Ingresa un nro:"))
nro2 = int(input("Ingresa otro nro:"))

try:
    division = nro1 / nro2
except:
    print("No se puede dividir, error")
else:
    print( "La division es: ", division)
finally:
    print("Se ha ejecutado la operación")