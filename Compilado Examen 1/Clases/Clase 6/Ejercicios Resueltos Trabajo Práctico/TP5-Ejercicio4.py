#Ejercicio 4

try:    
    for i in range ( 1, 100000):
        try:
            print(i)
        except KeyboardInterrupt as e:
            respuesta = input("¿Desea terminar con el programa? (S/N)")
            if respuesta == 'S':
                raise Exception("Se termina la ejecución")
        
except Exception as e:
    print(e)