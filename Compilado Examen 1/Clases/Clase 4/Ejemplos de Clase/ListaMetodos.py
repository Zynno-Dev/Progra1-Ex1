#Lista Metodos
lista = [1,2,3,4,5]
lista.append(6)

lista.insert(2,3)

print(lista.count(3))

lista.pop(2)

lista.remove(6)


print(lista)

print(lista.index(3))

lista.reverse()
print(lista)


lista = [3,2,1,4,6,5]
lista.sort()
print(lista)

lista = [1,2,34,8,9,16]
lista[2:5] = [3,4,5]
print(lista)


lista = [ 1,2,3,4,5]
listaCubos = [ i**3 for i in lista if i%2!=0 ]
print(listaCubos)



