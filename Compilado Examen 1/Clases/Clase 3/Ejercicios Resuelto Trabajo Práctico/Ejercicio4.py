'''
Eliminar de una lista de palabras las palabras que se encuentran en una segunda lista.
Imprimir la lista original, la lista de palabras a eliminar y la lista resultante.
'''

listaA = [ "pera", "manzana", "frutilla", "mango"]
listaB = [ "pera", "manzana"]

#Creo la lista por comprension
listaC = [ valor for valor in listaA if valor not in listaB ]

'''Forma tradicional recorriendo las listas
listaC = []
for valor in listaA:
    if valor not in listaB:
        listaC.append(valor)
'''

print("Lista Original: ", listaA)
print("Lista Palabras a Eliminar: ", listaB)
print("Lista Resultante: ", listaC)


    