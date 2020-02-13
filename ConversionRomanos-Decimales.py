romanos = {
	"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,
}

def Decimales(s):
	valor = ""
	nummero=0
	for i in range(len(s)):
		if i != len(s)-1 and romanos[s[i]]<romanos[s[i+1]] :
			nummero-=romanos[s[i]]
		else :
			nummero+=romanos[s[i]]
	return nummero

s = input("Ingrese Número a Convertir : ")
print (Decimales(s.upper()))