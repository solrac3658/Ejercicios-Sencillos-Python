def potencia(x,n):
	if n == 0:
		return 1
	if n == 1 :
		return x
	if n == 2 :
		return x*x
	potencia_actual= potencia(x,n//2)
	potencia_actual=potencia_actual*potencia_actual
	if n % 2 == 0:
		return potencia_actual
	else:
		return potencia_actual*x


for i in range (11):
	print (potencia(2,i))	

