####Ejercicio Numero 2, Busqueda de un entero en un arreglo 

def Busqueda(lista, numero):

	return numero in lista


lista = []
consulta = input("Ingrese una Lista seguido del Número a Buscar: ")
numero="";
end = False
for c in consulta :
	if end :
		if c == ',' or c == ' ':
			pass
		else :
			numero +=c
	elif c == '[' :
		pass
	elif c == "]" :
		lista.append(numero)
		numero=""
		end=True
	elif c == ',' :
		lista.append(numero)
		numero=""
	else :
		numero += c

print (Busqueda(lista,numero))