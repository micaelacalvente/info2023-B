"""9-Escribir un programa que pida al usuario tres números y muestre por pantalla
el mayor de ellos.
"""
numero_1 = int(input("ingresa el primer numero: "))
numero_2 = int(input("ingresa el segundo numero: "))
numero_3 = int(input("ingresa el tercer numero: "))

if numero_1 > numero_2 and numero_1 > numero_3:
    print(f"{numero_1} es el mayor")
elif numero_2 > numero_1 and numero_2 > numero_3:
    print(f"{numero_2} es el mayor")
else:
    print(f"{numero_3} es el mayor")
