from random import randint

def crear_matriz(filas, columnas):
    matriz = [ [0] * columnas for i in range(filas) ]
    return matriz

def mostrar_butacas(matriz):
    matrizEstado = [ [0] * len(matriz[0]) for i in range(len(matriz)) ]
    
    for i in range(len(matriz)):
        fila = matriz[i]
        matrizEstado[i] = [ "Libre" if valor==0 else "Ocupada" for valor in fila]
    
    for fila in matrizEstado:
        print(fila)
    
#cambia el estado de una butaca de libre a ocupada
#las butacas son numeradas desde 1 a filas*columnas
def reservar( matriz, butaca):
    reserva = True
    nroButaca = 0
    for i in range(len(matriz)):
        for j in range( len(matriz[0])):
            nroButaca +=1
            #print(i,j, nroButaca, butaca)
            if nroButaca == butaca and matriz[i][j] == 1:
                reserva = False

            if nroButaca == butaca and matriz[i][j] == 0:
                matriz[i][j] = 1
                
    
    return reserva
       
def cargar_sala( matriz ):
    matriz = [ [ randint(0,1) for j in range(len(matriz[0]))] for i in range(len(matriz))]
    return matriz
    
def butacas_libres(matriz):
    libres = 0
    for fila in matriz:
        libres += fila.count(0)
        
    return libres

def butacas_contiguas(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    libres = 0
    contiguas = 0
    maxContiguas = 0
    maxContiguasFila = 0
    maxContiguasColumna = 0
    for i in range(filas):
        contiguas = 0
        for j in range(columnas):
            if (matriz[i][j] == 0 and ((j+1)<columnas)  and matriz[i][j] == matriz[i][j+1]): 
                contiguas += 1
            if (matriz[i][j] == 0 and ((j+1)==columnas) and matriz[i][j] == matriz[i][columnas-1]):
                contiguas += 1
                
            if contiguas > maxContiguas :
                maxContiguas = contiguas
                maxContiguasFila = i
                maxContiguasColumna = j
        
    return ( maxContiguas, maxContiguasFila, maxContiguasColumna )
    

def main():
    filas = int( input("Ingrese nro. de filas:"))
    columnas = int( input("Ingrese nro. de butacas por fila:"))
    
    matriz = crear_matriz(filas,columnas)
    #a. creamos una matriz por comprensión con las filas y columnas, cada celda tiene un valor aleatorio entre 0-1 (0:desocupada, 1:ocupada)
    matriz = cargar_sala(matriz)

    mostrar_butacas(matriz)
    
    #b. reservar butaca
    butaca = int(input("Ingrese en nro. de butaca:"))
    reservo = reservar(matriz, butaca)
    
    while reservo == False:
        print("Lo siento, esa butaca ya esta reservada")
        mostrar_butacas(matriz)
        butaca = int(input("Ingrese en nro. de butaca:"))
        reservo = reservar(matriz, butaca)
    
    print("Se ha reservado la butaca ", butaca)
            
        
    mostrar_butacas(matriz)
    
    #c. ver la cantidad de butacas libres
    print("La cantidad de butacas libres es: ", butacas_libres(matriz))
    
    #d. ver la fila con mas butacas libres contiguas
    maxContiguas, maxContiguasFila, maxContiguasColumna = butacas_contiguas(matriz)
    print("Maxima cantidad de filas contiguas: ", maxContiguas, " en la fila ", maxContiguasFila, " en la columna ", maxContiguasColumna)
    
main()