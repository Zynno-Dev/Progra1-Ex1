#Ejercicio 11
#Este es un ejemplo de solución al ejercicio 11 de la guia de tp 2021 de programación I


def ingresarPacientes(lista):
    
    nroAfiliado = int(input("Ingrese nro. afiliado:"))
    while nroAfiliado!=-1 :
        tipoConsulta = int (input("Tipo de Consulta (0:Urgencia 1:Turno):"))
        lista.append([nroAfiliado, tipoConsulta])
        
        nroAfiliado = int(input("Ingrese nro. afiliado:"))
                    
    
def buscarPaciente(lista):
    
    nroAfiliado = int(input("Ingrese nro. afiliado:"))
    pacientesUrgencias = [ valor for valor in lista if valor[1]==0 ]
    pacientesTurnos = [ valor for valor in lista if valor[1]==1 ]
    
    while nroAfiliado != -1:
        cantidadUrgencias = 0
        cantidadTurnos = 0
        #buscamos la cantidad de urgencias
        for paciente in pacientesUrgencias:
            if( paciente[0]==nroAfiliado):
                cantidadUrgencias += 1
        #buscamos la cantidad de turnos
        for paciente in pacientesTurnos:
            if( paciente[0]==nroAfiliado):
                cantidadTurnos += 1
        
        print("El paciente tuvo ", cantidadUrgencias, " urgencias y ", cantidadTurnos, " turnos")
        
        nroAfiliado = int(input("Ingrese nro. afiliado:"))
        
        
    
def mostrarPacientes(lista):
    
    cantidadUrgencias = 0
    cantidadTurnos = 0
    
    pacientesUrgencias = [ valor for valor in lista if valor[1]==0 ]
    pacientesTurnos = [ valor for valor in lista if valor[1]==1 ]
    
    print("Pacientes Urgencias:")
    print(pacientesUrgencias)

    print("Pacientes Turnos:")
    print(pacientesTurnos)

    
def menu():
    print("Clinica UADE")
    print("1. Ingresar Pacientes")
    print("2. Mostrar Pacientes")
    print("3. Buscar Paciente")
    print("0.Salir")
    
    print("Ingrese su opción:")
    
    
def main():
    menu()
    opcion = int( input() )
    
    listaPacientes = []

    while opcion != 0:
        if opcion == 1:
            ingresarPacientes(listaPacientes)
        elif opcion == 2:
            mostrarPacientes(listaPacientes)
        elif opcion == 3:
            buscarPaciente(listaPacientes)
        else:
            opcion = 0
        
        menu()
        opcion = int( input() )
        
    
main()