"""11-Escribir un programa que pida al usuario dos números y muestre por pantalla
la suma de ellos solo si ambos son pares."""

num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))

if num1 % 2 == 0 and num2 % 2 == 0:
    print("la suma de ", num1, "+", num2, "=", num1+num2)
else:
    print("no son pares no hay suma pipipi")