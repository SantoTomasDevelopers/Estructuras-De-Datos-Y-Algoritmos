def EvaluacionCalidad(IndiceCalidad):
    calidad = None
    if(IndiceCalidad <= 30):
        # calidad = 'Buena'
        calidad = True
    elif(30 < IndiceCalidad < 80):
        calidad = False
        # calidad = 'Regular'
    elif(IndiceCalidad >= 80):
        calidad = False
        # calidad = 'Mala'
    return calidad

def ProyeccionCalidad(IndiceCalidad,DiasProyectados):
    IndiceCalidadNuevo = IndiceCalidad -(5*DiasProyectados)
    Eval = EvaluacionCalidad(IndiceCalidadNuevo)
    return Eval

def CalidadDias(IndiceCalidad):
    DiasProyectados = (IndiceCalidad - 30)/5
    return DiasProyectados

def mensajeCalidad(Funcion,BoolCalidad,Dias,Indice):
    if(Funcion == 1):
        mensajeMalo = 'Calidad del Aire no permite realizar ejercicio'
        mensajeBueno ='Calidad del Aire Permite realizar ejercicio'
        if(BoolCalidad):
            print(mensajeBueno)
        else:
            print(mensajeMalo)
    elif(Funcion == 2):
        mensajeMalo = 'Pasados '+str(Dias)+' dìas el Aire no està Bueno'
        mensajeBueno ='Pasados '+str(Dias)+' dìas el Aire Està Bueno'
        if(BoolCalidad):
            print(mensajeBueno)
        else:
            print(mensajeMalo)
    elif(Funcion == 3):
        mensaje = 'Con Ìndice de '+str(Indice)+' el aire estarà bueno en '+str(Dias)+' dìas'
        print(mensaje)