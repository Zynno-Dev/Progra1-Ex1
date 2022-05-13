#Ejercicio 5
from math import sqrt

try:
    nro = int(input("Ingrese un nro:"))
    if (nro<0):
        raise ValueError("No puede ingresar un nro. negativo")

    raiz = sqrt(nro)
except ValueError as e:
    print(e)
else:
    print("La raiz cuadrada es: ", raiz)
    
