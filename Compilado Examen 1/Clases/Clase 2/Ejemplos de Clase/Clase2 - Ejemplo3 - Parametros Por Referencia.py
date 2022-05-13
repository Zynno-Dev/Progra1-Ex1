#Esta funcion multiplica cada valor de lista * 5 (es una lista de 3 elementos)
def multiplicarPorCinco( lista ):
    for i in range (len(lista)):
        lista[i] = lista[i] * 5
        
#programa principal

miLista = [ 1, 2, 3, 7, 8 ]

print( miLista )

multiplicarPorCinco( miLista )

print( miLista )


    