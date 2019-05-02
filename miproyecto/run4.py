"""
	file: run.pr
	auto: @reati

	Deseamos obtener el costo de una carrera universitaria. El valor promedio de cada ciclo es de $1200. 
	El valor promedio del seguro educativo es de $100. 
	Si la edad del estudiante es menor e igual 20, caso contrario sera de $150. 
	Si el estudiante tiene una modalidad a distancia, el número de ciclos a seguir es de $10. 
	Caso contrario debera seguir 8 ciclos. 
	Obtener la proyección del costo de la carrera
"""

# Declaracion de variables
edad = input("Ingrese su edad: ")
modalidad = input("Ingrese su modalidad: ")
ciclo = 1200
# Se pasa a enteros
edad = int(edad)
# Estructura condicional y proceso del ejercicio
if (modalidad == "Distancia"):
	cant_ciclo = 10
else:
	cant_ciclo = 8

if (edad <=20):
	seguro = 100
	total = (ciclo * cant_ciclo) + (seguro * cant_ciclo)
else: 
	seguro = 150
	total = (ciclo * cant_ciclo) + (seguro * cant_ciclo)
# Presentación del mensaje
print("%s  %d" % ("Costo de la carrera:", total))






	















