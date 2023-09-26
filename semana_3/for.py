# FOR // PARA

# RANGO (valor_inicial, valor_final, incremento)
# si no aclaras el valor inicial, por defecto es 0
# si no aclaras el valor de incremento por defecto es 1

for valor in range(11): # lo mismo que range(0, 11, 1)
    print(valor, end=" ")

# EJEMPLO DE USO
# mostrar todos los pares del 0 al 100
suma = 0
for numero in range(0, 101, 2):
    suma += numero
print(f"la suma de los numeros pares del 1 al 100 es {suma}")

tope = int(input("Ingrese el tope: "))
for numero in range(1, tope+1, 1):
    print(numero, end=" ")

# tambien se puede iterar sobre strings:
for letra in "Python":
    if letra == "h":
        continue
    print(f"Letra actual: {letra}")

# CUANDO USO UN FOR Y CUANDO UN WHILE
# for solo se puede usar si se conoce la cantidad de veces a iterar
# por ej en la calcu no se puede