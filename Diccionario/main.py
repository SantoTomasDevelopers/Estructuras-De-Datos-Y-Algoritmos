#definir una estructura adecuada
ListaUsuarios = {
	"1-9":{
		"rut":"1-9",
		"nombreCompleto":"asd",
		"Direccion":"qwe",
		"Email":"asd@asd.cl",
		"Actividades":{
			"controles":[11,12,13,14,15,16,17,18,19,20],
			"Laboratorio":[1,3,5,7,9],
			"Proyecto":[1]
			}
	},
	"2-7":{
		"rut":"",
		"nombreCompleto":"klñ",
		"Direccion":"iop",
		"Email":"klñ@jkl.cl",
		"Actividades":{
			"controles":[1,2,3,4,5,6,7,8,9,10],
			"Laboratorio":[2,4,6,8,10],
			"Proyecto":[2]
			}
	}
}
#for usr in ListaUsuarios:
#	print(ListaUsuarios[usr]["nombreCompleto"])

Salida = True
while Salida:
	usrConsulta = input("Ingrese usuario a consultar: ")
	if(usrConsulta == "0"):
		Salida = False
	else:
		if(usrConsulta in ListaUsuarios):
			
			salida2 = True
			while salida2:
				actConsulta = input("ingrese actividad a consultar: ") 
				if(actConsulta in ListaUsuarios[usrConsulta]["Actividades"]):
					salida2 = False
					print("Nombre: "+str(ListaUsuarios[usrConsulta]["nombreCompleto"]))
					print("Rut: "+str(ListaUsuarios[usrConsulta]["rut"]))
					print("Email: "+str(ListaUsuarios[usrConsulta]["Email"]))
					print("Direccion: "+str(ListaUsuarios[usrConsulta]["Direccion"]))
					NumeroNota = 1
					for Notas in ListaUsuarios[usrConsulta]["Actividades"][actConsulta]:
					
						print(str(actConsulta)+" N° "+str(NumeroNota)+" es: "+str(+Notas ))
						NumeroNota += 1
				else:
					print("Actividad No existe")
		else:
			print("Usuario no existe")