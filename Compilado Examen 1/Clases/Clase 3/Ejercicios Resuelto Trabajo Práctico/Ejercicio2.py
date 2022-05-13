from random import randint

def crearListaAleatorios(cantidad):
    lista = [ randint( 1,100) for i in range(cantidad) ]
    return lista


def repetidosLista(lista):
    hayRepetidos = False
    for valor in lista:
        if( lista.count(valor) > 1):
            hayRepetidos = True
            
    return hayRepetidos

def nuevaLista(lista):
    listaNueva = [ valor for valor in lista if lista.count(valor) == 1 ]
    return listaNueva

#a
listaAleatorios = crearListaAleatorios(50)
print(listaAleatorios)

#b
lista = [ 3, 0, 2, 5, 1, 10]
print(repetidosLista( lista ) )

#c
lista = [ 3, 2, 4, 4, 1, 10, 15]
lista2 = nuevaLista(lista)
print(lista2)
#####OJO Revisar, no esta incluyendo los repetidos