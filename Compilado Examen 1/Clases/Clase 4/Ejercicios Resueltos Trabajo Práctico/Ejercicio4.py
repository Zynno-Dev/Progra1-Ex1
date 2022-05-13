from random import randint

def crearMatriz(filas, columnas):
    matriz = [ [0] * columnas for i in range(filas) ]
    return matriz

def imprimirMatriz(matriz):
    for fila in matriz:
        print(fila)
        

def mostrarDia(dia):
    diaTxt = "Lunes"
    if dia==1:
        diaTxt = "Martes"
    elif dia==2:
        diaTxt = "Miercoles"
    elif dia==3:
        diaTxt = "Jueves"
    elif dia==4:
        diaTxt = "Viernes"
    elif dia==5:
        diaTxt = "Sabado"
        
    return diaTxt
        
def main():
    n = int( input("Ingrese nro. de fabricas:"))
    filas = n
    columnas = 6 #de lunes a sabado
    
    #a. creamos una matriz por comprensión con las filas y columnas, cada celda tiene un valor aleatorio
    matriz = [ [ randint(0,150) for j in range(columnas)] for i in range(filas)]

    imprimirMatriz(matriz)
    
    #b. total de bicletas de cada fabrica
    for i in range(filas):
        total = sum(matriz[i])
        print("Fabrica ", i, ":", total , " bicicletas")
        
    #c. fabrica que tuvo la mayor producción
    maximo = matriz[0][0]
    maxFabrica = 0
    maxDia = 0
    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] > maximo:
                maximo = matriz[i][j]
                maxDia = j
                maxFabrica = i
                
                
    print("La maxima producción fue en la fabrica ", maxFabrica, " el día ", mostrarDia(maxDia), " con un total de ", maximo, " bicicletas.")
    
    #d. dia más productivo, debemo realizar la suma por columna
    sumaDia = [ 0 for j in range(columnas) ]
    for j in range(columnas):
        for i in range(filas):
            sumaDia[j] += matriz[i][j]
            
    #obtengo el indice con el elemento mayor
    diaMaxProduccion = sumaDia.index( max(sumaDia) )
    print( "El día más productivo fue: ", mostrarDia( diaMaxProduccion ) )

    #e. crear una lista por compresión con la menor cantidad de cada fabrica
    matrizMenorProduccion = [ min(fila) for fila in matriz ]
    print( "La menor producción de cada fabrica fue : ", matrizMenorProduccion )
main()