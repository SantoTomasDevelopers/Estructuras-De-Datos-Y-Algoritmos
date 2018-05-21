
def nombre():
	nombre = input("ingrese nombre:: ")
	apellido = (input("ingrese apellido:: "))
	return nombre + ' ' + apellido


def nota_controles_teoricos (cantidad_de_notas):
	nota_control_teorico=0
	suma=0
	for iteracion in range (cantidad_de_notas):
            nota_control_teorico = float (input("ingrese nota de control teorico: "))
            suma=nota_control_teorico+suma
        promedio_teorico=suma / cantidad_de_notas
        ponderacion_teorico=(promedio_teorico*0.20)
	return promedio_teorico

def nota_controles_practicos (cantidad_de_notas):
	nota_control_practicos=0
	suma=0
	for iteracion in range (0,cantidad_de_notas):
            nota_control_practicos = float (input("ingrese nota de control practico: "))
            suma=nota_control_practicos+suma
        promedio_practico=suma / cantidad_de_notas
        ponderacion_practico=(promedio_practico*0.12)
	return promedio_practico

def nota_proyecto ():
	nota_proyecto=float(input("\n\tingrese nota del proyecto: "))
	ponderacion_proyecto=nota_proyecto * 0.48
	return nota_proyecto
	
def eximido_o_reprobado (promedioTotal):
	if (promedioTotal>5.5):
		print("Felicidades ha quedado eximido con un promedio de : ", promedioTotal)
	elif (((promedioTotal+7.0)/2)<4.0):
		print ("Has reprobado")
	elif (((promedioTotal+7.0)/2)>4.0):
		print ("Debe rendir examen")
