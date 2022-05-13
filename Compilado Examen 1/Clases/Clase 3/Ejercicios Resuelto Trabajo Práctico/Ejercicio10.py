from random import randint

'''Generar una lista con numeros al azar entre 1 y 100 y crear una nueva lista con los elementos de la primera que sean impares.
El proceso deberá realziarse utilizando listas por compresión.
Imprimir las dos listas por pantalla
'''

#Lista con elementos al azar entre 1-100
lista = [ randint(1, 100) for valor in range(1, 101)]
print(lista)

#Lista con elementos impares de lista original
listaImpares = [ valor for valor in lista if valor%2!=0]
print(listaImpares)