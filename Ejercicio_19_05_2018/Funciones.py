
#Tipos de Notas
#Control
#Practico
#Proyecto
#Examen
#jprodrigues@rodriges.cl


PonderacionTeorico = 20
ponderacionPractico = 12
PonderacionProyecto = 48
PonderacionExamen = 20
NombreEstudiante = ''

def IngreseNombre():
	return input('Ingrese su nombre ::: ')

def TomaNotas(CantidadNotas,TipoNota):
	if(CantidadNotas != 0):
		Suma = 0
		Promedio = 0
		for i in range(CantidadNotas):
			Nota = float(input('Ingrese '+TipoNota+' N° : '+str(i+1)+' :: '))
			Suma = Nota + Suma 
			#print(Suma)

		print(Suma)
		print(CantidadNotas)
		Promedio = Suma	/ CantidadNotas
		print(Promedio)
		if(TipoNota == 'Control'):
			return (PonderacionTeorico * Promedio)/100

		elif(TipoNota == 'Practico'):
			return (ponderacionPractico * Promedio)/100

		elif(TipoNota == 'Proyecto'):
			return (PonderacionProyecto* Promedio)/100

		elif(TipoNota == 'Examen'):
			return (PonderacionExamen * Promedio)/100

	else:
		return 0





