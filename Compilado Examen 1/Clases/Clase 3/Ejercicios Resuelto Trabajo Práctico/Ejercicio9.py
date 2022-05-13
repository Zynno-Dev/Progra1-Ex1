'''Generar e imprimir una lista por compresión entre A y B con los multiplos de 7 que no sean multiplos de 5.
A y B se ingresan desde el teclado.'''

a = int ( input("Ingrese A:") )
b = int ( input("Ingrese B:") )

lista = [ valor for valor in range(a, b+1) if valor%7==0 and valor%5!=0 ]

print(lista)