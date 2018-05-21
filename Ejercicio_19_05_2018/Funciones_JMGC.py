
#Tipos de Notas
#Control
#Practico
#Proyecto
#Examen
#jprodrigues@rodriges.cl

PonderacionTeorico  = 20
ponderacionPractico = 12
PonderacionProyecto = 48
PonderacionExamen   = 20
NombreEstudiante    = ''
NotaBaja            = 0

def IngreseNombre():
	# Nombre =  input('Ingrese su Nombre ::: ')
	# Apellido =  input('Ingrese su Apellido ::: ')
	# return Nombre + ' ' + Apellido
	return input('Ingrese su Nombre ::: ')

def TomaNotas(CantidadNotas,TipoNota):
	#VarPonderaciones = __init__()
	#NotaBaja = VarPonderaciones.NotaBaja
	global NotaBaja
	NotaBaja = 0.0
	Nota = 0.0
	if(CantidadNotas != 0):
		Suma = 0.0
		Promedio = 0.0
		for i in range(CantidadNotas):
			Nota = 0.0
			while(Nota<=0 or Nota >7.0):
				try:
					Nota = float(input('Ingrese '+TipoNota+' N° : '+str(i+1)+' :: '))
				except Exception as e:
					error = format(e)

			if(NotaBaja == 0):
				NotaBaja = Nota
			if(Nota<NotaBaja):
				NotaBaja = Nota
			Suma += Nota 
		Suma -= NotaBaja
		Promedio = Suma	/ (CantidadNotas-1)
		if(TipoNota == 'Control'):
			return (PonderacionTeorico * Promedio)/100 , Promedio

		elif(TipoNota == 'Practico'):
			return (ponderacionPractico * Promedio)/100 , Promedio

		elif(TipoNota == 'Proyecto'):
			return (PonderacionProyecto* Promedio)/100 , Promedio

		elif(TipoNota == 'Examen'):
			return (PonderacionExamen * Promedio)/100 , Promedio

	else:
		return 0


def ValidacionNotas(NotaControl,NotaPractico,NotaProyecto):
	Suma = 0
	MensajeAprobado       = 'Usted Esta Aprobado y EXIMIDO del Examen!'
	MensajeRendir         = 'Usted debe RENDIR el Examen!'
	MensajeReprobado      = 'Usted Esta Reprobado! Por tener'
	MensajeReprobadoDos   = 'promedio ROJO!'
	MensajeReprobadoFinal = ''
	MesnsajeError         = 'Error'
	promedio 		      = 0
	Rojos				  = ''

	Suma =NotaControl +  NotaPractico + NotaProyecto
	promedio = Suma / 3
	if(NotaControl < 4.0 or NotaPractico < 4.0 or NotaProyecto < 4.0):
		#Reprobado
		#print(MensajeReprobado)
		if(NotaControl < 4.0 and NotaPractico >= 4.0 and NotaProyecto >= 4.0):#1 promedio rojo
			Rojos = 'Control : '+str(NotaControl)
		elif(NotaControl < 4.0 and NotaPractico < 4.0 and NotaProyecto >= 4.0):#2 promedios rojos
			Rojos = 'Control : '+str(NotaControl) +' y Practico : ' + str(NotaPractico)
		elif(NotaControl < 4.0 and NotaPractico < 4.0 and NotaProyecto < 4.0):#3Promedios rojos
			Rojos = 'Control : '+str(NotaControl) +' y Practico : ' + str(NotaPractico) +' y Proyecto : ' + str(NotaProyecto)
		else:
			Rojos = 'Error 02'
		MensajeReprobadoFinal = MensajeReprobado+' '+Rojos+' '+MensajeReprobadoDos
		return 0,MensajeReprobadoFinal,promedio

	elif( promedio >= 5.5):
		#Aprobado
		#print(MensajeAprobado)	
		
		return 1,MensajeAprobado,promedio
	
	elif( promedio >= 4.0):
		#Rendir Examen
		#print(MensajeRendir)
		Suma =NotaControl +  NotaPractico + NotaProyecto
		
		return 2,MensajeRendir,promedio

	return 0,MesnsajeError

#ValidacionNotas(5.6,5.6)

