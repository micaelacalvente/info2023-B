comision_6 = ["Mica", "Gera", "Eli"]
print(comision_6)

# SIN MANEJO DE ERRORES
 # indice = int(input("Ingrese el indice del elemento a imprimir: "))
 # print(comision_6[indice])

# CON MANEJO DE ERRORES
# ERROR DE INDEXACION / VALORES
try: #intenta
    indice = int(input("Ingrese el indice del elemento a imprimir: "))
    print(comision_6[indice])
except IndexError or ValueError:
    print("El indice ingresado no es valido, ingresar valores del 0 al 2")
else:
    print("Es un profe de la comision 6 !")
finally: #opcional/se ejecuta independiente si hay excepcion o no
    print("Fin del programa :)")


# ERROR DE DIVISION
def division(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        print("No se puede dividir por cero >:(")
    else:
        print(result)

division(0,0)