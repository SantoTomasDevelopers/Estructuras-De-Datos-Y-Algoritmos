#main

import funciones
nombre = funciones.nombre()
print"Bienvenido",nombre

cantidad_de_notas=int(input("ingrese cantidad de pruebas: "))
controles_teoricos = funciones.nota_controles_teoricos(cantidad_de_notas)
print "el promedio de controles teoricos es: ", controles_teoricos
controles_practicos= funciones.nota_controles_practicos(cantidad_de_notas)
print "Su promedio de controles practicos es: ", controles_practicos
nota_de_proyecto = funciones.nota_proyecto()
print "Nota del proyecto: ",nota_de_proyecto

sumaPromedios=(controles_teoricos+controles_practicos+nota_de_proyecto)
promedioTotal=sumaPromedios / 3
print ("Su Nota de presentacion es: ",promedioTotal)

presentacion = funciones.eximido_o_reprobado(promedioTotal)