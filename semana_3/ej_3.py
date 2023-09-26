'''3-Escribe un programa que pida al usuario un número y luego imprima la tabla de
multiplicar correspondiente a ese número del 1 al 10.'''

# soluciones con for

# solución de guille
numero = int(input("Por favor, ingresa tu numero: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

# solución de nico
numero=int(input('Ingrese un numero: '))
lista=[1,2,3,4,5,6,7,8,9,10]

for i in lista:
    print(f'{i}*{numero}={numero*i}')

# -------------------------------------------- #

# solución con while
num = int(input("ingresa un numero: "))

i = 1

while i <= 10:
    print(num, "x", i, "=", num*i)
    i += 1