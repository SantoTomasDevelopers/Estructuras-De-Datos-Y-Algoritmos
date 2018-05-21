import Funciones_JMGC as fn
Opcion = 'si'


while(Opcion.upper() == 'SI' ):
    PonderacionControles = 0
    PonderacionPractico  = 0
    PonderacionProyecto  = 0
    PonderacionExamen    = 0
    PonderacionFinal      = 0
    Nombre               = ''
    NotaAprobacion       = 0.0

    Nombre = fn.IngreseNombre()
    PonderacionControles = fn.TomaNotas(5,'Control')
    PonderacionPractico  = fn.TomaNotas(5,'Practico')
    PonderacionProyecto  = fn.TomaNotas(1,'Proyecto')

    ResultadoValidacion = fn.ValidacionNotas(PonderacionControles[1],PonderacionPractico[1],PonderacionProyecto[1])

    if(ResultadoValidacion[0] == 1):#Aprobado sin rendir examen
        NotaAprobacion = ResultadoValidacion[2]
        print('Alumno:: '+str(Nombre)+', '+str(ResultadoValidacion[1])+' con el promedio ::  {0:.2f}'.format(NotaAprobacion))
        
    if(ResultadoValidacion[0] == 0):#Reprobado sin rendir examen
        print('Alumno:: '+str(Nombre)+', '+ResultadoValidacion[1])
        
    if(ResultadoValidacion[0] == 2):#Rendir examen
        promedio = (PonderacionControles[1] + PonderacionPractico[1] + PonderacionProyecto[1])/3
        print('Alumno:: '+str(Nombre)+', '+ResultadoValidacion[1] + ' con nota presentacion de :: {0:.2f}'.format(promedio))
        PonderacionExamen  = fn.TomaNotas(1,'Examen')
        PonderacionFinal = PonderacionControles[0] + PonderacionPractico[0] + PonderacionProyecto[0] +PonderacionExamen[0]
        if(PonderacionFinal>= 4.0):
            print('Alumno:: '+str(Nombre)+', Usted Aprobo el ramo con ::{0:.2f}'.format(PonderacionFinal))
        else:
            print('Alumno:: '+str(Nombre)+', Usted Reprobo el ramo con :: {0:.2f}'.format(PonderacionFinal))


    while(Opcion.upper() != 'NO'):
        try:
            Opcion = input('Decea ingresar otro alumno? \n\t\t si/no :: ')
            if(Opcion.upper()=='SI'):
                break
        except Exception as e:
            error = format(e)

print('**************SALIENDO**************')