#funciones

def nombre():
	nombre = input("ingrese nombre:: ")
	apellido = str(input("ingrese apellido:: "))
	return nombre + ' ' + apellido


def nota_controles_teoricos (cantidad_de_notas):
	nota_control_teorico=0
	suma=0
	for iteracion in range (0,cantidad_de_notas):
            nota_control_teorico = int (input("ingrese nota de control teorico: "))
            suma=nota_control_teorico+suma
        promedio_teorico=suma / cantidad_de_notas
        ponderacion_teorico=(promedio_teorico*0.20)
	return promedio_teorico

def nota_controles_practicos (cantidad_de_notas):
	nota_control_practicos=0
	suma=0
	for iteracion in range (0,cantidad_de_notas):
            nota_control_practicos = int (input("ingrese nota de control practico: "))
            suma=nota_control_practicos+suma
        promedio_practico=suma / cantidad_de_notas
        ponderacion_practico=(promedio_practico*0.12)
	return promedio_practico

def nota_proyecto ():
	nota_proyecto=int(input("\n\tingrese nota del proyecto: "))
	ponderacion_proyecto=nota_proyecto * 0.48
	return nota_proyecto

def eximido_o_reprobado (promedioTotal):
	if (notaPresentacion>55):
		print("Felicidades ha quedado eximido con un promedio de : ", notaPresentacion)
	elif (((notaPresentacion+70)/2)<40):
		print ("Has reprobado")
	elif (((promedioTotal+7.0)/2)>4.0):
		print ("Debe rendir examen")

