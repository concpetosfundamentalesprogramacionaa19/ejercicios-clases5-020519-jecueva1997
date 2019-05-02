"""
	file: run.pr
	auto: @reati
"""
# Importación de las varibles
from misvariables import *
# Se pide el ingreso de las notas
nota = input("Ingrese la primera nota: ")
nota2 = input("Ingrese la segunda nota: ")

nota = int(nota)
nota2 = int(nota2)
# Estructura condicional
if nota >=18:
	print("%s - %d" % (mensaje, nota))
else:
	print("%s - %d" % (mensaje2, nota))

if nota2 >=18:
	print("%s - %d" % (mensaje, nota2))
else:
	print("%s - %d" % (mensaje2, nota2))
