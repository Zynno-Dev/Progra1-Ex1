'''Utilizar la tecnica de listas por compresion para construir  una lisa con todos los numeros impares comprendidos entre 100 y 200.
'''
listaImpares = [ valor for valor in range(100,201) if valor%2!=0 ]
print(listaImpares)