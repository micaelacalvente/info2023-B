# # # ALGUNOS METODOS EN PYTHON # # #

# capitalize() convierte la primera letra de la cadena en mayúscula y el resto en minúsculas.
nombre = input("ingresa tu nombre: ").capitalize()
print(nombre)

# title() hace lo mismo que capitalize()
nombre = input("Ingresa tu nombre: ").title()
print(nombre)

# upper() convierte todas las letras a mayúsculas
nombre = input("Ingresa tu nombre: ").upper()
print(nombre)

# lower() convierte todas las letras a minúsculas
nombre = input("Ingresa tu nombre: ").lower()
print(nombre)

# swapcase() convierte las mayúsculas en minúsculas y viceversa
nombre = input("Ingresa tu nombre: ").swapcase()
print(nombre)

# strip() elimina los espacios en blanco al principio y al final de la cadena
texto = input("Ingresa un texto: ").strip()
print(texto)

# replace() reemplaza una subcadena por otra en la cadena
texto = input("Ingresa un texto: ").replace("2022", "2023")
print(texto)

# center() centra la cadena dentro de un campo de ancho especificado
texto = input("Ingresa un texto: ").center(20, "_")
print(texto)

