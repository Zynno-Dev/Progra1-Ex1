#Cortes de Listas
valores = [ 2, 5,10, 1, 76, 99]
print(valores)
#Con dos indices
corte1 = valores[2:5]

print(corte1)

#Omitimos el primer indice
corte2 = valores[:5]

print(corte2)

#Omitimos el segundo indice
corte3 = valores[2:]
print(corte3)

#Con indice negativo
corte4 = valores[-4:-2]
print(corte4)

#Reemplazamos valores
valores[2:4] = [23,24,56,67]
print(valores)

