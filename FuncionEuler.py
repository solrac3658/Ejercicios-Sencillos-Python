"""
Números coprimos, 2 Números son coprimos si el único número que los divide a ambos es 1
"""
def coprimo(x,y):
	for i in range (2,y+1):
		if (x%i==0 and y%i==0):
			return 0
	return 1

"""
La función de Euler cuenta la cantidad de números coprimos que hay entre 1 y un número N
"""
def euler (n):
	suma = 1
	for i in range (2,n):
		suma += coprimo(n,i)
	return suma
