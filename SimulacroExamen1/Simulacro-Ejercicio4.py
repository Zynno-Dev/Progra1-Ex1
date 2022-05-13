'''
El aula de informática de la Universidad tiene 25 computadoras.
Una computadora puede estar libre (0), ocupada(1) o apagada (-1) por algún desperfecto.
Dado que se tomará examen se asigna una computadora por alumno.
El profesor antes de ingresar a clase, le informa al alumno que computadora esta libre indicando el nro. de computadora (de 1 a 25),
también le informa la fila.
Se pide crear una función que permita al profesor asignar una computadora a l alumnos a medida que vayan llegando.
Dicha función deberá pasar una computadora de libre a ocupada actualizando el mapa en cada asignación.
Los alumnos que darán examen son 18, y actualmente el mapa de computadoras se encuentra en el siguiente estado:
0   0   -1  0   0
0   0   0   -1  0
0   0   -1  0   0
0   0   0   -1  0
0   -1  0   0   0
'''

def crearMatriz(filas, columnas):
    matriz = [ [0] * columnas for i in range(filas) ]
    return matriz

def dibujaMatriz(matriz):
    
    print ('[')
    for fila in matriz:
        print (fila),
    print (']')
 
def actualizarOcupado(matriz, fila, columna):
    matriz[fila][columna] = 1
  
def actualizarInactiva(matriz, fila, columna):
    matriz[fila][columna] = -1  

def computadoraDisponible(matriz):
    i = 0
    j = 0
    #Valor centinela o bandera que nos indica que se ha encontrado un lugar libre
    encontroDisponible = False

    #Recorre la matriz mientras no encuentre un lugar libre.
    #Cuando encuentra un lugar libre actualiza la bande a verdadero
    while i < len(matriz) and encontroDisponible == False:
        j = 0
        while j < len(matriz[0] ) and encontroDisponible == False:
            #print( i, j, matriz[i][j])
            if matriz[i][j] == 0:
                encontroDisponible = True
            j += 1
        i += 1

    #Retornamos un valor anterior porque al salir del bucle incrementa en 1
    return i-1, j-1
    

def asignarComputadoras( matriz, cantidadAlumnos ):
    
    for alumno in range( cantidadAlumnos ):
        fila, columna, nroComputadora = compuDispo(matriz)
        matriz[fila][columna] = 1
        print("Alumno: ", alumno, " utiliza la computadora en la fila: ", fila, " columna: ", columna , " nro de computadora: ", nroComputadora )


def compuDispo(mat):
    
    filas = len(mat)
    columnas = len(mat[0])
    
    fila_encontrada = -1
    colu_encontrada = -1
    maq_encontrada = -1
    numero_maquina = 1
    
    ya_encontre = False
    
    for f in range(filas):
        for c in range(columnas):
            if (mat[f][c] == 0 and ya_encontre == False):
                fila_encontrada = f
                colu_encontrada = c
                maq_encontrada = numero_maquina
                ya_encontre = True
            numero_maquina+=1
                
    return fila_encontrada, colu_encontrada, maq_encontrada    


def main():
    #crear matriz
    matriz = crearMatriz(5,5)
    print("Creamos la Sala del Laboratorio de Informatica:")
    dibujaMatriz( matriz )
    
    #llenar la matriz con el estado inicial
    actualizarInactiva(matriz, 0, 2)
    actualizarInactiva(matriz, 1, 3)
    actualizarInactiva(matriz, 2, 2)
    actualizarInactiva(matriz, 3, 3)
    actualizarInactiva(matriz, 4, 1)    
    print("Configuración Estado Inicial Laboratorio:")
    dibujaMatriz( matriz )

    #asignamos las computadoras a los alumnos
    asignarComputadoras(matriz, 18)
    print("Sala luego de Asignar las Computadoras:")
    dibujaMatriz( matriz )
main()