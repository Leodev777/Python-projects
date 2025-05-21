## Concatenacion de string

nombre = "    Leo     "
apellido = "  IGLEsias   "
nombre_completo = f"{nombre} {apellido}"
print(nombre_completo.upper()) ## Letras en mayusculas
print(nombre_completo.lower()) ## Letras en minusculas
print(nombre_completo.capitalize())  ## Primera letra en mayusculas
print(nombre_completo.title())  ## Primera letra de cada string en mayusculas
print(nombre_completo.strip()) ## Elimina los espacios de la decha e izquierda, se puede concatenar con capitalize
print(nombre_completo.lstrip) ## Elimina los espacios de la izquierda
print(nombre_completo.rstrip) ## Elimina los espacios de la derecha
print(nombre_completo.find("GLE")) ## Busca cadena de string dentro de un string
print(nombre_completo.replace("IGLE", "igle")) ## Remplazamos valores
print("Leo" in nombre_completo) ## Busca cadena de caractenes, con diferencia con find, es que find te devuelve un indice y in te revuelve un boolean
print("Leo" not in nombre_completo) ## busca que la cadena no se encuentre dentro del string
