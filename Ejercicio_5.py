####Ejercicio Numero 5, Determinar si una frase es un panagrama

lista=[]
alfabeto =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]

lineas = int(input("Ingrese la cantidad de Lineas: "))

for i in range(lineas):
	frase = input()
	for c in frase:
		if c.lower() in alfabeto :
			lista.append(c.lower())
	lista=set(lista)
	if len(lista) == 26 :
		print("SI")
	else :
		print("NO")
	lista = []
