"""
Desarrolle un programa que grafique los largos de las secuencias de Collatz 
de los números enteros positivos menores que el ingresado por el usuario
"""
def  Cantidad_Collatz(n):
	if n == 1:
		return 1
	if n%2==0:
		return 1 + Cantidad_Collatz(n//2)
	else:
		return 1+ Cantidad_Collatz(n*3+1)

n=int(input())

str_cantidad=""
for i in range(1,n+1):
	cantidad= Cantidad_Collatz(i)
	for j in range(cantidad):
		str_cantidad += "*"
	print(str_cantidad)
	str_cantidad=""
