#Clase 3 - Listas

#Operacion

from audioop import reverse
import string


list(n) #Devuelve una lista con los elementos de n

in [1,2,3] #Devuelve True si el elemento está en la lista

not in [1,2,3] #Devuelve True si el elemento no está en la lista

len [1,2,3] #Devuelve el número de elementos de la lista

max [1,2,3] #Devuelve el máximo elemento de la lista

min [1,2,3] #Devuelve el mínimo elemento de la lista

sum [1,2,3] #Devuelve la suma de los elementos de la lista

for n in array #Recorre la lista

listaA = listaB + listaC #Concatena las listas

lista[2:6] #Devuelve una sublista de la lista, desde la posición 2 hasta la posición 6

lista[:6] #Devuelve una sublista de la lista, desde la posición 0 hasta la posición 6

lista[2:] #Devuelve una sublista de la lista, desde la posición 2 hasta el final

lista2 = [i**3 for i in lista if i%2!=0] #Devuelve una lista con los cubos de los elementos impares de la lista

#Metodos

lista.reverse() #Invierte el orden de los elementos de la lista

lista.append(x) #Agrega un elemento al final de la lista

lista.insert(pos,valor) #Inserta un elemento en la posición indicada

lista.remove(x) #Elimina el elemento indicado

lista.index(n) #Devuelve la posición del elemento indicado

lista.index(n,n,n) #Devuelve la posición del elemento indicado, desde la posición n hasta la posición n

lista.count(n) #Devuelve la cantidad de veces que aparece el elemento indicado

lista.pop() #Elimina el último elemento de la lista

lista.pop(n) #Elimina el elemento indicado

lista.clear() #Elimina todos los elementos de la lista

lista.sort() #Ordena la lista

lista.sort(reverse = true) #Ordena la lista de forma descendente

########################################################

#Clase 4 - Matrices

#lista replicacion
print(lista*2)  #duplica la lista
print(lista*0)  #devuele la lista vacia

#por comprension
lista = [1,2,3]
listaPares = [x for x in lista if x%2==0] #con condicionales

lista = [1,2,3]
lista2 = [x for x in lista if x%2==0 else x*2 for x in lista] #con condicionales o alternativas dobles

lista =[int(input("Ingrese un numero: ")) for x in range(5)] #que se ingresen los valores por teclado

lista = [random.randint(1,10) for x in range(5)] #con randint

#Matrices forma estatica
matriz = [[1,2],[4,5]] #matriz 2x2
matriz = [[1,2,3],[4,5,6]] #matriz 2x3
matriz = [[1,2,3],[4,5,6],[7,8,9]] #matriz 3x3

print(matriz[0][0]) #acceder a la primera fila y el primer elemento

#matrices forma dinamica
matriz = []
filas = 3
columnas = 3
matriz = []
for x in range(filas):
    matriz.append([0]*columnas) #replicando elementos solo agregamos filas

#matrices con listas de comprension
filas= 3
columnas = 4
matriz = [[0]*columnas for x in range(filas)]

########################################################

#Clase 5 - Strings / Cadena de caracteres

#Los srings son cadenas de texto, por ende se comportan como un array, inclusive pudiendo capturar caracteres a partir de indices.

#+ Concatenar
#* Multiplicar
#+= Añadir
#in Buscar
#== Comparar

for letra in cadena #Recorre la cadena de caracteres de izquierda a derecha

string.count("l") #Devuelve la cantidad de veces que aparece la letra indicada

string.replace("1","2") #Reemplaza la letra indicada por la letra indicada

string.find("H") #Devuelve la posición de la letra indicada

string.split() #Devuelve una lista con los elementos de la cadena de caracteres

string.split(sep="-") #Devuelve una lista con los elementos de la cadena de caracteres, separados por el caracter indicado

string.index("a") #Devuelve la posición de la letra indicada

string.isalpha() #Devuelve True si la cadena de caracteres contiene solo letras

string.isdigit() #Devuelve True si la cadena de caracteres contiene solo números

string.islower() #Devuelve True si la cadena de caracteres contiene solo letras minúsculas

string.isupper() #Devuelve True si la cadena de caracteres contiene solo letras mayúsculas

string.join(lista) #Devuelve una cadena de caracteres con los elementos de la lista, separados por el caracter indicado

string.lower() #Devuelve la cadena de caracteres en minúsculas

string.upper() #Devuelve la cadena de caracteres en mayúsculas

string.strip() #Devuelve la cadena de caracteres sin los espacios en blanco

string.strip(sep="-") #Devuelve la cadena de caracteres sin los espacios en blanco y los caracteres indicados

string.lstrip() #Devuelve la cadena de caracteres sin los espacios en blanco a la izquierda

string.lstrip(sep="-") #Devuelve la cadena de caracteres sin los espacios en blanco a la izquierda y los caracteres indicados

string.rstrip() #Devuelve la cadena de caracteres sin los espacios en blanco a la derecha

string.rstrip(sep="-") #Devuelve la cadena de caracteres sin los espacios en blanco a la derecha y los caracteres indicados

string.startswith("H") #Devuelve True si la cadena de caracteres comienza con la letra indicada

string.endswith("H") #Devuelve True si la cadena de caracteres termina con la letra indicada

string.isalnum() #Devuelve True si la cadena de caracteres contiene solo letras y números

string.capitalize() #Devuelve la cadena de caracteres con la primera letra en mayúscula

string.title() #Devuelve la cadena de caracteres con las primeras letras de cada palabra en mayúscula

string.center(10,"+") #Devuelve la cadena de caracteres centrada en una cadena de caracteres de longitud 10

string.ljust("+") #Devuelve la cadena de caracteres a la izquierda

string.rjust("+") #Devuelve la cadena de caracteres a la derecha

string.zfill(6) #Devuelve la cadena de caracteres rellenada con ceros a la izquierda

#Formatear un string
#Se utiliza el prefijo f para indicar que se rellenaran los valores con las variables con el mismo nombre
nombre = "Juan"
edad = 23
print(f"Hola, mi nombre es {nombre} y tengo {edad} años")
#Devuelve = Hola, mi nombre es Juan y tengo 23 años

########################################################

#Clase 6 - Tratamiento de errores

#1. error de sintaxis
SyntaxError: invalid syntax
#2. error de nombre
NameError: name 'x' is not defined
#4. error de semantica
IndexError: list index out of range
TypeError: unsupported operand type(s) for +: 'int' and 'str'
#Tipos de excepciones
#bloque try except
try:
    n = float(input("Ingrese un numero: "))
    m=4
    print("{}/{}={}".format(n,m,n/m))
except:
    print("Ha ocurrido un error, introduce bien el numero")
#bloque else
try:
    n = float(input("Ingrese un numero: "))
    m=4
    print("{}/{}={}".format(n,m,n/m))
except:
    print("Ha ocurrido un error, introduce bien el numero")
else:
    print("No hubo error")
    break #rompe el ciclo
#bloque finally
try:
    n = float(input("Ingrese un numero: "))
    m=4
    print("{}/{}={}".format(n,m,n/m))
except:
    print("Ha ocurrido un error, introduce bien el numero")
else:
    print("No hubo error")
    break #rompe el ciclo
finally:
    print("Se ejecuto el finally") #siempre se ejecuta
#excepciones multiples
try:
    n= input("Ingrese un numero divisor: ") #no transformamos a numero
    5/n
except TypeError: #guardamos la excepcion como una variable e
    print("No se puede divir el numero entre una cadena")
    except ValueError:
    print("Debes introducir una cadena que sea un numero")
    except ZeroDivisionError:
    print("No se puede dividir entre 0")
    except Exception as e:
    print("Ha ocurrido un error", type(e).__name__)
#Crear excepciones
class MiError(Exception):
    pass

def calcularPromedio(lista):
    if len(lista)==0:
        raise MiError("La lista esta vacia")
    else:
        return sum(lista)/len(lista)