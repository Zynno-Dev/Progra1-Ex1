#Cadena de Caracteres: Metodos

texto = input("Ingrese institucion:")
textoPalabras = texto.split()
sigla = ""

for palabra in textoPalabras:
    sigla += palabra[0]
    
print( "La sigla es:", sigla.upper() )