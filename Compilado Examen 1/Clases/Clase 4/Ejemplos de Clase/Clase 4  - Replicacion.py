lista = [ 2, 3, 9, 10 ]
print( lista )

listaPares = [ valor**2 for valor in lista if (valor%2)==0 ]
print( listaPares )

listaParesImpares = [ valor**2 if valor%2==0 else valor**3 for valor in lista ]
print( listaParesImpares )

listaInput = [ int(input("Ingrese nro:")) for valor in range(5) ]
print(listaInput)

|
