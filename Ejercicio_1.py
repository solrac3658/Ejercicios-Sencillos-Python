####	Ejercicio Numero 1, Transformación Digital a Romano - I
####		IMPORTANTE La conversión llega hasta el número 3999 debido a que a partir del 4000 se necesita un caracter especial para representar el número. 
  

romanos = {
	0:"",1:"I",2:"II", 3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX",
	10:"X",20:"XX", 30:"XXX",40:"XL",50:"L",60:"LX",70:"LXX",80:"LXXX",90:"XC",
	100:"C",200:"CC", 300:"CCC",400:"CD",500:"D",600:"DC",700:"DCC",800:"DCCC",900:"CM",
	1000:"M",2000:"MM", 3000:"MMM",
}

def Romanos(numero):

	numero_romano=""
	potencia = str(numero)
	potencia = len(potencia) - 1
	divisor = 10 ** potencia
	while divisor != 0 :
		clave = numero % divisor
		clave= numero - clave
		numero_romano += romanos[clave]
		numero = numero - clave
		divisor= divisor // 10
	return numero_romano


numero = int(input("Ingrese dato: "))

if numero>3999:
	print("El numero Ingresado debe ser menor estricto a 4000")
else:
	numero_romano = Romanos(numero)
	print (numero_romano)

