"""7-Escribir un programa que pida al usuario un carácter y muestre por pantalla si
es una letra mayúscula, una letra minúscula, un número o un carácter especial."""

caracter = input("Ingresa un caracter: ")
if caracter.isupper():
    print("es mayuscula")
elif caracter.islower():
    print("es minuscula")
elif caracter.isdigit():
    print("es un numero")
else:
    print("es un caracter especial")

# string.metodo() sintaxis