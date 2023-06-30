from django.core.exceptions import ValidationError
import re

def nombreValidator(value):
	# value va a tener todo el string que se introdujo en el input
	# voy a separar por cada espacio viendo si cada palabra tiene o no 
	# un caracter numerico, caracter especial o palabras con tildes,
	# si lo tiene tira un mensaje de error 

	if len(value)>=3: #Controla que no se ingresen nombres cortos como ja"

		palabras = value.split(" ")

		for i, palabra in enumerate(palabras): #value.split(" ") me devuelve un array de palabras

			if (i==0) and (not len(palabra)>=2):#Controla la 1er palabra para ingresar Ej: Di o Mc
				raise ValidationError("Debe ingresar más letras")
			if (i>0) and (not len(palabra)>=3): #Controla las siguientes palabras para ingresar Ej: Ana o Sol 
					raise ValidationError("Debe ingresar más de 3 letras por espacio")

			if not palabra.isalpha():
				raise ValidationError("Debe ingresar solo letras")
			# isalpha() me devuelve True si el string contiene los caracteres
			# [a-z] o [A-Z] 
			# me devuelve False si el string contiene los caracteres
			# [0-9] o algun caracter especial como['#','.','-','á','é','í','ó','ú',etc] 
	else:	
		raise ValidationError("Debe ingresar más de 3 letras")
	
def isbnValidator(value):

	if len(value) != 13:
		raise ValidationError("Volver a ingesar. El ISBN esta compuesto por 13 numeros")
	
	if not re.match('^[0-9]{13}$', value):
		raise ValidationError("Debe ingresar solo numeros")
	
	if (value[0:3] != "978") and (value[0:3] != "979"):
		raise ValidationError("El ISBN debe iniciar con 978 o 979")