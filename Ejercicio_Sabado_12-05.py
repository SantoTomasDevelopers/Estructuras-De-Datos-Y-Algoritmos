Iteracion = 0
TotIteraciones = 0
Ejercicio = 0
SumaPar = 0
try:
	while True:
			
		Ejercicio= int(input('ingrese el Numero del ejercicio 1 - 5:: '))

		if(Ejercicio == 1):
			print('Ejercicio 1')
			while(True):
				Iteracion =0
				TotIteraciones = input('ingrese el valor de iteraciones:: ')
				for Iteracion in range(int(Iteracion),int(TotIteraciones)):
					print('Iteracion:: ',Iteracion+1)
				print('::::::::::::FIN::::::::::::')

		elif(Ejercicio == 2):
			print('Ejerciio 2')
			while(True):
				Iteracion = 0
				
				SumaPar = 0
				TotIteraciones = 0
				while(TotIteraciones <= 1 or TotIteraciones > 20 or TotIteraciones == None ):
					TotIteraciones = int(input('Ingrese un numero para sumar sus pares del 1 - 20:: '))
				
				for Iteracion in range(int(Iteracion),int(TotIteraciones)):
					if(Iteracion%2 == 0):
						SumaPar = SumaPar + Iteracion
						print('Suma Par:: ',SumaPar,'y le sumara:: ',Iteracion+2)
						
		elif(Ejercicio == 3):
			print('Ejercicio 3')
			while(True):
				Iteracion = 0
				while(int(TotIteraciones) <= 0 or int(TotIteraciones) > 100):
					
					TotIteraciones = input('Ingrese un numero para ver los multiplos de 2 y 3  entre 0 y 100:: ')
				
				for Iteracion in range(int(Iteracion),int(TotIteraciones+1)):

					if(Iteracion != 0 and Iteracion %2 == 0):
						print('Multiple de 2 para el valor :: '+str(Iteracion))
					if(Iteracion != 0 and Iteracion %3 == 0):
						print('Multiple de 3 para el valor ::: '+str(Iteracion))

		elif(Ejercicio == 4):
			print('Ejercicio 4')
			Opcion = 0
			valorUno = 0
			valorDos = 0
			Resultado = 0
			while(Opcion != 5):
				Opcion = 0
				print('Menu')
				print('1 .- Sumar')
				print('2 .- Restar')
				print('3 .- Multiplicar')
				print('4 .- Dividir')
				print('5 .- Salir')
				Opcion = input('Ingrese opcion      :: ')
				while(Opcion != 5):
					valorUno = input('Ingrese Primer valor:: ')
					valorDos = input('Ingrese Segundo valor :: ')

					#suma
					while(Opcion == 1):
						Resultado = valorUno + valorDos
						print('el resultado de la suma entre '+str(valorUno)+' con ' +
							str(valorDos)+' es :: '+str(Resultado))
						break
						

					#resta
					while(Opcion == 2):
						Resultado = valorUno - valorDos
						print('el resultado de la resta entre '+str(valorUno)+' con ' +
							str(valorDos)+' es :: '+str(Resultado))
						break

					#multiplicacion
					while(Opcion == 3):
						Resultado = valorUno * valorDos
						print('el resultado de la multiplicacion entre '+str(valorUno)+' con ' +
							str(valorDos)+' es :: '+str(Resultado))
						break
					
					#divicion
					while(Opcion == 4):
						Resultado = float(valorUno) / float(valorDos)
						print('el resultado de la divicion entre '+str(valorUno)+' con ' +
							str(valorDos)+' es :: '+str(Resultado))
						break
					
		elif(Ejercicio == 5):
			print('Ejercicio 5')
			Iteracion = 0
			salir = -1

			while(Iteracion != salir):
				for i in range(1,Iteracion+1):
					if(i%2 == 0):
						print('Numero :: '+str(i)+' es par')
					else:
						print('Numero :: '+str(i)+' no es par')
				Iteracion = int(input(
					'Ingrese un numero para salir ingrese '+str(salir)+' :: ')) 
		
		else: 
			print('Elercicio no encontrado')
except KeyboardInterrupt:
	print(' ')
	print(' ')
	print(' ')
	print('::::::::::::::::::::::::::ADIOS::::::::::::::::::::::::::')
except Exception as e:
	print(str(e))
	
	
def multiple(valor, multiple):
    #TODO: tengo que reparar esta funcion 
    resto = valor % multiple
    if resto == 0:
        return True
    else:
        return False
