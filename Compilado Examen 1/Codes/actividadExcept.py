numB = 0
numA = 0
flag = 0
def declarador():
    global numA, numB, flag
    numA = int(input("Ingrese el primer numero: "))
    if numA==-1:
        print("Fin del programa")
        flag = -1
    else:
        numB = int(input("Ingrese el segundo numero: "))
        if numB==-1:
            print("Fin del programa")
            flag = -1
def promedioException(a,b):
    global flag
    try:
        if flag != -1:
            return (a+b)/2
    except:
        print("No se puede dividir entre cero")
        declarador()
        if flag != -1:
            promedioException(a,b)

while flag!=-1:        
    declarador()
    temp = promedioException(numA,numB)
    if temp != None:
        print(temp)