import random
from math import sin,cos


lista = [ random.randint(1,100) for i in range(100) ]
print( lista )
print("---------")
listaPares = [ valor for valor in lista if (valor%2)==0 ]
print(listaPares)
print("---------")
listaImpares = [ valor for valor in lista if (valor%2)!=0 ]
print(listaImpares)
print("---------")
lista2 = [ sin(valor) if valor%2==0 else cos(valor) for valor in lista ]
print( lista2 )

