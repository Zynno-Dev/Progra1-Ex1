class MiExcepcion( Exception ):
    pass

def calcularPromedio(lista):
    if (len(lista) == 0 ):
        raise MiExcepcion()
    else:
        return (sum(lista)/len(lista))
    
    
lista = []
try:
    promedio = calcularPromedio(lista)
    print(promedio)

except MiExcepcion:
    print("La lista no tiene elementos")
else:
    print("Se calculo el promedio")
finally:
    print("Fin Calculo")
    

try:
    lista = [3,4,5,6]
    promedio =  calcularPromedio(lista)
    print(promedio)
except MiExcepcion:
    print("La lista no tiene elementos")
else:
    print("Se calculo el promedio")
finally:
    print("Fin Calculo")
    