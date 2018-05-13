Iteracion = 0
TotIteraciones = 0
Ejercicio = 0
SumaPar = 0

try:
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
		
		while(int(TotIteraciones) <= 0 or int(TotIteraciones) >= 100):
			
			TotIteraciones = input('Ingrese un numero para sumar sus pares del 1 - 20:: ')
		
		for Iteracion in range(int(Iteracion),int(TotIteraciones)):
			if(Iteracion%3 == 0):
				SumaPar = SumaPar + Iteracion
				print('Suma Par:: ',SumaPar,'y le sumara:: ',Iteracion+2)




	elif(Ejercicio == 4):
		print('Ejercicio 4')
		

	elif(Ejercicio == 5):
		print('Ejercicio 5')
		
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
   
    resto = valor % multiple
    if resto == 0:
        return True
    else:
        return False