### Dado un arreglo de enteros de 7 enteros que representan los dias de una semana se desea saber que combinación de días
### nos da el mayor número, restando el Dia A con un Dia B, el Dia B no puede ser mayor al Dia A 
### [6,2,1,5,1,2,3] -> 4
def MayorDistancia (lista):
    copia_lista=lista
    mayor = 0
    x=max(lista)
    xp=lista.index(x)
    y=min(lista)
    yp=lista.index(y)
    if (xp>yp):
        return x-y
####### Una buena opción es buscar el maximo y restarle el mínimo, pero debemos asegurarnos que 
#### la posición del mínimo sea menor a la posición del máximo para asgurar que el dia B sea Mayor que el A 
##### en dado caso que no sea así procedemos a ejecutar los ciclos. 
    for i in lista:
        copia_lista.pop(0)
        for j in copia_lista:
            numero = j-i
            if numero > mayor:
                mayor = numero
    return mayor 

print (MayorDistancia([6,2,1,5,1,2,3]))
