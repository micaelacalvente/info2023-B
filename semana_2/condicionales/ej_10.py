"""10-Escribir un programa que pida al usuario una letra y muestre por pantalla si es
una vocal o una consonante."""

letra = input("Ingresa una letra: ").lower()
if letra in "aeiou":
    print(letra, "es una vocal")
else:
    print(letra, "es consonante")
