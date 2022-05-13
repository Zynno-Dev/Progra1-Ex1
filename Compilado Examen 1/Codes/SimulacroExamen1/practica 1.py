arrayTest = []
palabra = 'margen'

def separarPalabra(palabra):
    for i in range(len(palabra)):
        arrayTest.append(palabra[i])
        arrayTest.append('-')
    return arrayTest

separarPalabra(palabra)
arrayTest.pop(-1)
stringTest = ''.join(arrayTest) # convierte el array en un string
print(stringTest)