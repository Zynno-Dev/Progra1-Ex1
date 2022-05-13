#Pedro tiene almacenados en una variable del tipo lista a sus contactos. 
#Cada elemento de la lista tiene el siguiente formato:
#Nombre: Teléfono: Profesión
#Se pide, mostrar los contactos de Pedro con el siguiente formato:
#    “El numero telefónico de Mariano Martínez es 33433224”

contactos = [ "Juan Perez:33432244:Docente",
              "Mariano Rodriguez:667444:Desempleado",
              "Carla Martino:0948333:Actriz"]


for contacto in contactos:
    infoContacto = contacto.split(sep=":")
    print( "El numero telefónico de ", infoContacto[0], " es ", infoContacto[1] )