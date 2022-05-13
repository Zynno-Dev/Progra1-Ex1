from random import randint

# Llena una lista con numeros al azar de 4 digitos.
# La cantidad de elementos tambien es al azar de 2 digitos
def cargarListaAzar():
    cantidadElementos = randint(0, 99)
    print("La cantidad de elementos es:", cantidadElementos)
    lista = [ randint(0,9999) for i in range(cantidadElementos) ]
    return lista

#Retorna la sumatoria de todos los elementos de la lista
def sumatoriaLista(lista):
    suma = 0
    for valor in lista:
        suma += valor
        
    return suma

#Elimina un valor de una lista
def eliminarValor(lista, valor):
    print("Eliminamos el valor: ", valor)
    lista.remove(valor)

#Verifica si los valores de una lista son capicuas
#Retorna True si es capicua, False si no es capicua
#Ejemplo: 50 17 91 17 50 es capicua
def esCapicua(lista):
    esCapicua = False

    #Si la lista es igual a lista en reversa, es capicua
    #Para la reversa podemos usar slicing [::-1] 
    # lista[::-1] #invierte una lista
    if( lista == lista[::-1]):
        esCapicua = True
        
    return esCapicua
        
        
    
    
    
    
#1. Definimos la Lista
lista = []

#a. 
lista = cargarListaAzar()
print( lista )

#b
suma = sumatoriaLista(lista)
print("Sumatoria:", suma)
print( lista )

#c
#valor = int(input("Ingrese un valor a eliminar:"))
#eliminarValor(lista, valor)
#print( lista )

#d
lista = [50, 17, 91, 91, 17, 50]
esCapicua = esCapicua(lista)
print( esCapicua )
print(lista)