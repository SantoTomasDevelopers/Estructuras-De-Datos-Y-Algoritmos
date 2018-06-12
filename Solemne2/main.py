import Funciones as fn

InCalidad = 0
InDias = 0
VarDias = 0
ResultEvalCalidad = False
ResulProyecDias = False

InCalidad = int(input('Ingrese Calidad actual del Aire: '))
ResultEvalCalidad = fn.EvaluacionCalidad(InCalidad)
fn.mensajeCalidad(1,ResultEvalCalidad,None,InDias)

InDias = int(input('Ingrese Cantidad de dìas: '))
ResulProyecDias = fn.ProyeccionCalidad(InCalidad,InDias)
fn.mensajeCalidad(2,ResulProyecDias,InDias,None)

VarDias = fn.CalidadDias(InCalidad)
fn.mensajeCalidad(3,None,VarDias,InCalidad)