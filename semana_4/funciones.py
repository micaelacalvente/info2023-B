# crear función
def saludo(comision): #parametro
    """
    esta función imprime un saludo
    args: comisión
    """
    print(f"Hola comision {comision}")

saludo(6) #argumento
saludo(7) #argumento
print(saludo.__doc__)


# PARAMETROS POR POSICIÓN
def suma(num1, num2):
    total = num1 + num2
    return total

suma(6, 2)

# 2 formas de devolver el valor
total_suma = suma(9, 2)
print(f"el total es {total_suma}")

print("el total es: ", suma(2, 3))

# PARAMETROS POR NOMBRE
def saludo(nombre, comision):
    print(f"Hola {nombre} sos de la comision {comision}")

print("Bienvenido al mundo de las funciones!")

# PARAMETROS POR DEFECTO
def saludo2(nombre="Alumno", comision="tarde"):
    print(f"Hola {nombre} sos de la comision {comision}")

print("Bienvenido al mundo de las funciones!")
saludo2(nombre="Ricardo")

# ARGUMENTOS INDETERMINADOS: *ARGS - **KWARGS
def pido_pizza(tamaño, *ingredientes, **detalles):
    print(f"Pediste una pizza tamaño {tamaño} de: ")
    for ingrediente in ingredientes:
        print(f"-{ingrediente}")
    print("-----------------------")
    for clave, valor in detalles.items():
        print(f"-{clave}: {valor}")

pido_pizza("grande", "jamon", "queso", delivery="si", pago="efectivo")

# *ARGS (Argumentos posicionales) Es un parámetro especial que recibe los argumentos como una tupla.
# **KWARGS (Argumentos de Palabras Clave) Es un parámetro especial que recibe los argumentos como un diccionario.

# MODULOS
import math as mt #se puede importar con un alias si se desea
print(mt.sqrt(25))

import datetime
fecha_actual = datetime.datetime.now()
print(fecha_actual)