####Ejercicio Numero 3,  Determinar el elemento que más se repite e imprimirlo 


import operator

numero="";
lista=[]

consulta = input("Ingrese Lista: ")

for c in consulta :
	if c == '[' :
		pass
	elif c == "]" :
		lista.append(int(numero))
		numero=""
	elif c == ',' :
		lista.append(int(numero))
		numero=""
	else :
		numero += c

dic_contador = {i:lista.count(i) for i in lista}

sort = sorted(dic_contador.items(), key=operator.itemgetter(1,0), reverse=True)

print( "%s , %s" %(sort[0][0] , sort[0][1]))