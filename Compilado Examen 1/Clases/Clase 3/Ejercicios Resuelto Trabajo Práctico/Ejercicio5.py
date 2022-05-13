'''Escribir una función que reciba una lista como parametro y devuelva True si la lista esta ordenada en forma ascendente o False en caso contrario.
Por ejemplo:
[ 1, 2, 3 ] retorna True
[ 'b', 'a'] retorna False

Desarrollar ademas el progarma para verificar el comportamiento de la función.
'''

def estaOrdenadaFormaAscendente( lista ):
    ordenada = True
    
    anterior = lista[0]
    
    for valor in lista:
        if valor < anterior:
            ordenada = False
        anterior = valor
        
    return ordenada
    
    

def main():
    listaA = [ 1, 2, 3 ]
    print(estaOrdenadaFormaAscendente( listaA ) )
          
    listaB = [ 'b','a' ]
    print(estaOrdenadaFormaAscendente( listaB ) )

    listaC = [ 1, 5, 2 ]
    print(estaOrdenadaFormaAscendente( listaC ) )

main()
