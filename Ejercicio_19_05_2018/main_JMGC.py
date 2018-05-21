import Funciones_JMGC as fn
Opcion = 'si'


while(Opcion.upper() == 'SI' ):
    PonderacionControles = 0
    PonderacionPractico  = 0
    PonderacionProyecto  = 0
    PonderacionExamen    = 0
    PonderacionSuma      = 0
    Nombre               = ''
    NotaAprobacion       = 0.0

    Nombre = fn.IngreseNombre()
    PonderacionControles = fn.TomaNotas(5,'Control')
    PonderacionPractico  = fn.TomaNotas(5,'Practico')
    PonderacionProyecto  = fn.TomaNotas(5,'Proyecto')

    ResultadoValidacion = fn.ValidacionNotas(PonderacionControles[1],PonderacionPractico[1],PonderacionProyecto[1])

    if(ResultadoValidacion[0] == 1):#Aprobado sin rendir examen
        NotaAprobacion = ResultadoValidacion[2]
        print('Alumno:: '+str(Nombre)+', '+str(ResultadoValidacion[1])+' con el promedio :: '+str(NotaAprobacion))
        
    if(ResultadoValidacion[0] == 0):#Reprobado sin rendir examen
        print('Alumno:: '+str(Nombre)+', '+ResultadoValidacion[1])
        
    if(ResultadoValidacion[0] == 2):#Rendir examen
        print('Alumno:: '+str(Nombre)+', '+ResultadoValidacion[1])


    while(Opcion.upper() != 'NO'):
        try:
            Opcion = input('Decea ingresar otro alumno? \n\t\t si/no :: ')
            if(Opcion.upper()=='SI'):
                break
        except Exception as e:
            error = format(e)

print('**************SALIENDO**************')