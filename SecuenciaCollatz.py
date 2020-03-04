def  Collatz(n):
	if n == 4:
		return "4 2 1"
	if n%2==0:
		return str(n) + " "  + Collatz(n//2)
	else:
		return str(n) + " " + Collatz(n*3+1)

print (Collatz(19))
	