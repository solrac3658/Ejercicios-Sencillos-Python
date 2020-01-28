####Ejercicio Numero 4, Dada una fecha obtener la siguiente fecha habil 

from datetime import datetime, timedelta

fecha_str= input("Ingrese fecha: ")
fecha = datetime.strptime(fecha_str, '%d-%m-%Y')
day = fecha.date().weekday()

if day >=4 :
	fecha = fecha + timedelta(days=7-day)
else:
	fecha = fecha + timedelta(days=1)

fecha = fecha.strftime('%d-%m-%Y')

print(fecha)