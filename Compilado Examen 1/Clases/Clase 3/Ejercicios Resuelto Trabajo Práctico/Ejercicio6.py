''' Escribir una función que reciba una lista de numeros enteros como parametro y la normalice, es decir, que todos sus elementos deben sumar 1.0, respetando las proporciones relativas que cada elemento tiene en la lista original.
Desarrollar tambien un programa que permita verificar el comportamiento de la función.
Por ejemplo:
[1,1,2] debe devolver [0.25, 0.25, 0.50]

Ojo, no utilizamos la formula matematica de normalizacion
Xnorm = (x-xmin/xmax-xmin)

Para obtener los resultados planteamos debemos sumar todos los valor y cada elemento dividirlo por ese resultado.
suma = sum(lista)
Para cada elemento
Xnorm=(x)/suma
'''

def normalizar(lista):
    suma = sum(lista)
    lNormalizada = [ valor/suma for valor in lista]
    
    return lNormalizada

    
def main():
    lista = [1,1,2,2,3]
    listaNormalizada = normalizar(lista)
    
    print(lista)
    print(listaNormalizada)
   
    
main()