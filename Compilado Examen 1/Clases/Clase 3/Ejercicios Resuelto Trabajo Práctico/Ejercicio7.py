lista1 = [1, 4, 5] 
lista2 = [3, 8, 9]

#Creamos una lista con la concatenacion de ambas
lista3 = lista1 + lista2
print( "Antes del slicing: ", lista3 )

print("Reemplazamos desde la posición 0 hasta el final en las posiciones 0, 2, 4... con los valores de la lista 1")
lista3[::2] = lista1
print( lista3 )
print("Reemplzamos desde la posición 1 hasta el final en las posiciones 1, 3, 5... con los valores de la lista 2")
lista3[1::2] = lista2 
print( lista3 )
  
print ("La lista intercaladas: " + str(lista3)) 