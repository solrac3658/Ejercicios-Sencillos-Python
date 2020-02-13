## Dada una cadena de caracteres debe retornar la cantidad de veces que la letra actual se repetie seguidamemnte
## ABBBBCC -> A4B2C

def ComprimirCadena(s):
    s+="\n" ##Agregando Marca de final de Cadena
    repetido = ""
    contador = 0
    cadena_comprimida = ""
    for c in s:
        if c==repetido:
            contador +=1
        else:
            if contador<=1:
                cadena_comprimida+= repetido
            else: 
                cadena_comprimida+= str(contador)+repetido.upper()
            repetido=c
            contador=1
    return cadena_comprimida

print (ComprimirCadena("ABBBBCC"))
