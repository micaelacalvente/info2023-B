'''6-Crea una función llamada es_par que tome un número como parámetro y
devuelva Es par si el numero cumple con dichas condiciones y en caso contrario
devuelva Es impar o No es par.'''

# solución 1
def es_par(numerito):
    if numerito % 2 ==0:
        print("Es par")
    else:
        print("Es impar")

es_par(5)

# solución 2
def es_par2(numero):
    if numero % 2 ==0:
        return "es par"
    else:
        return "es impar"

print(es_par2(5))

# solución 3
num=int(input("Ingrese un numero: "))

def es_par(numerito):
    if numerito % 2 ==0:
        return "Es par"
    else:
        return "Es impar"

print(es_par(num))
