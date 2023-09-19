"""8-Escribir un programa que pida al usuario una cadena de caracteres y muestre
por pantalla si contiene la letra "a"."""

caracter = input("Ingresa una cadena de caracteres: ")
if "a" in caracter: # si "a" esta en caracter
    print(caracter, "contiene a")
else:
    print(caracter, "no contiene a")