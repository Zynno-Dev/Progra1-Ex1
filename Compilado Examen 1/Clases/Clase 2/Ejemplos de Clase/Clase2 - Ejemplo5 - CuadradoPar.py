#Calcula el cuadrado de un nro. solo si es par
def cuadradoPar(numero):
    
    if( not (numero % 2 == 0) ):
        return
    else:
        return numero ** 2


#programa principal
print( cuadradoPar( 8 ) )
print( cuadradoPar( 3 ) )
print( cuadradoPar( 2 ) )

        