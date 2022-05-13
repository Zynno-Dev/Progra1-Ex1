#Concatenación de Listas
listaA = [1,2,3]
listaB = [4,5,6]

listaC = listaA + listaB

print(listaC)

for i in range( len(listaC) ):
    listaC[i] = listaC[i]**2
    
print("Cuadrado de cada valor")
print(listaC)

listaC = listaC + [887]
print(listaC)

    