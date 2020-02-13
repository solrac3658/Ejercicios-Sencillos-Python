##Nota Alguien Sabe si existen números amigos que sean impares??####
def SumaDivisores (n):
    suma =0
    for i in range (1,(n//2)+1):
        if n%i==0:
            suma +=i
    return suma

def NumerosAmigos (x,y):
    if (SumaDivisores(x)==y and SumaDivisores(y)==x):
        return True
    return False

print (NumerosAmigos(220,284))