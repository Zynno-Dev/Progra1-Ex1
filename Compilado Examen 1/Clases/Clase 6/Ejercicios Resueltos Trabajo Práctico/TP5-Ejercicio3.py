def obtenerMes(mes):
    meses = ["Enero", "Febrero", "Marzo", "Abril" , "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    nombreMes = ""
    try:
        nombreMes = meses[mes-1]
    except IndexError as e:
        print("Es un mes invalido")
        raise Exception
     
    return nombreMes

nroMes = 12
try:
    print( "El mes es: ", obtenerMes(nroMes))
except:
    print("Error")
        