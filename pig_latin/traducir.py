def traducir():

	palabra = input("Ingresa una palabra> ")
	palabra = palabra.lower()

	if len(palabra) > 0:
		validacion = True
	else:
		validacion = False

	#Una vez validada la palabra, la funcion convertir traduce la palabra
	def convertir():
		try:
			traduccion = palabra[1:(len(palabra))]+palabra[0]+"ei"
			print(traduccion)
		except IndexError:
			print("Error de Index debido a que no se ha introducido ninguna palabra")


	#Llama a la funcion convertir
	convertir()