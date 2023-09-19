# CONDICIONAL SIMPLE
comision = 6

if comision == 6:
    print("Hola comision 6")

# CONDICIONAL MULTIPLE
usuario = "usuario"
contra = "contra123"

if usuario == "usuario" and contra == "contra123":
    print("Bienvenido")

# CONDICIONAL ALTERNATIVO
n = 10
if n % 2 == 0:
    print(n, "es un número par")
else:
    print(n, "es un numero impar")

# CONDICIONAL ANIDADO
a = 5
b = 10

if a == 5:
    print("a vale", a)
    if b == 10:
        print("y b vale", b) #una condicion dentro de otra
else:
    print("otra cosa")

# CONDICIONAL ALTERNATIVO MULTIPLE
cuestionario = float(input("Ingresa la nota que obtuviste: "))

if cuestionario >= 9: # si saque 9 o mas
    print("Sobresaliente")
elif cuestionario >= 7: # sino 
    print("Muy bueno")
elif cuestionario >= 6: # sino
    print("Bien, aprobaste")
else: 
    print("Desaprobe")