"""6-Escribir un programa que pida al usuario un número entero y muestre por
pantalla si es múltiplo de 2 y de 3 a la vez."""

num = int(input("Ingrese un numero entero: "))
if num % 2 == 0 and num % 3 == 0: # si es multiplo de 2 Y de 3
    print(num, "es multiplo de 2 y de 3 a la vez")
else:
    print(num, "no es multiplo de 2 y de 3 a la vez")