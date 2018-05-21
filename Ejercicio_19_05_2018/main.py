import Funciones as fn

PonderacionControles = 0
PonderacionPractico  = 0
PonderacionProyecto  = 0
PonderacionExamen    = 0
PonderacionSuma      = 0
Nombre = fn.IngreseNombre()

PonderacionControles = fn.TomaNotas(5,'Control')
PonderacionPractico  = fn.TomaNotas(5,'Practico')
PonderacionProyecto  = fn.TomaNotas(5,'Proyecto')
PonderacionExamen    = fn.TomaNotas(5,'Examen')

PonderacionSuma = PonderacionControles + PonderacionPractico + PonderacionProyecto + PonderacionExamen

print(Nombre)
print('Ponderacion Contoles :: '+str(PonderacionControles))
print('Ponderacion Practico :: '+str(PonderacionPractico))
print('Ponderacion Proyecto :: '+str(PonderacionProyecto))
print('Ponderacion Examen   :: '+str(PonderacionExamen))
print('Ponderacion Suma   :: '+str(PonderacionSuma))
