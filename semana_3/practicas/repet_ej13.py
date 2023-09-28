"""13-Escribe un programa que pida al usuario un número y luego imprima un
triángulo de asteriscos con esa cantidad de filas.
*
**
***
****
*****"""

# solucion 1
num_filas = int(input("Ingrese un numero: "))

for i in range(num_filas):
    for j in range(i+1):
        print("*", end="")
    print()

# solucion 2
numero = int(input('ingrese su numero'))

for n in range(numero+1):
    print('*'* n)

# solucion 3
base = int(input("Decime cuanto mide la base de tu triángulo: "))
punta = 0
for i in range(base+1):
    print((punta+i)*"*")

