
#funciones

def nombre():
	nombre=str(input("ingrese su nombre "))
	return nombre


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
	calpromedio1 = promedioTotal*0.8
	calpromedio2 = 4.0-calpromedio1
	calpromedio3 = calpromedio2 * 0.2

	if (promedioTotal>5.5):
		print "Felicidades ha quedado eximido con un promedio de : ", promedioTotal
	elif ((calpromedio3+promedioTotal)<4.0):
		print "Has reprobado"
	elif ((calpromedio3+promedioTotal)>4.0 and (calpromedio3+promedioTotal)<5.5):
		print "Debe rendir examen"
		nota_examen=int(input("Ingrese nota del examen"))
		pasa_de_curso=(promedioTotal*0.8)+(nota_examen*0.2)
		if (pasa_de_curso>4.0):
			print "Apruebas con: ",pasa_de_curso
		else:
			print "Reprobado "
