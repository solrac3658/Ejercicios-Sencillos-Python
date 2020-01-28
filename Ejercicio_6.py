####Ejercicio Numero 6, 	obtener un código celular 


codigo_telefonico = {
    "a": "2", "b": "22", "c": "222", 
    "d": "3", "e": "33", "f": "333", 
    "g": "4", "h": "44", "i": "444", 
    "j": "5", "k": "55", "l": "555", 
    "m": "6", "n": "66", "o": "666", 
    "p": "7", "q": "77","r": "777", "s": "7777", 
    "t": "8", "u": "88", "v": "888", 
    "w": "9","x": "99", "y": "999", "z": "9999",
    " ": "0"
}

texto_codificado = ""

lineas = int(input("Ingrese la cantidad de Lineas: "))

for x in range(lineas):
	frase = input()
	for c in frase:
		if c.lower() in codigo_telefonico:
			y = codigo_telefonico[c.lower()]
			if len(texto_codificado) > 1 and y [0] == texto_codificado[len(texto_codificado)-1] :
				texto_codificado += " "
				texto_codificado += y
			else :
				texto_codificado += y
		else:
			texto_codificado += c
	print(texto_codificado)
	texto_codificado = ""