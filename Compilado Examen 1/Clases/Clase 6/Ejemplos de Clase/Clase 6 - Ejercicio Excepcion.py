try:
    #Expresion Inicio
    nroAlumno = int(input("Ingrese nro. alumno:"))
    
    #Condición
    while nroAlumno != -1 :
        try:
            nota1 = int(input("Nota 1:") )
            nota2 = int(input("Nota 2:") )
            promedio = (nota1+nota2) / 2
        except Exception as e:
            print("Lo siento, ha ingresado un valor incorrecto en alguna de las notas del parcial.")
            print(e)
        else:
            print("El promedio del alumno ", nroAlumno, " es: ", promedio)
    #Expresión Fin
        nroAlumno = int(input("Ingrese nro. alumno:"))
except:
    print("Lo siento, ha ocurrido un error.")
finally:
    print("Fin.")
        