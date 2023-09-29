"""8-Escribe un programa que pida al usuario una cadena de texto y luego imprima
el número de palabras que contiene."""

# solucion 1
texto = input("Ingresa una cadena de texto: ")

palabras = texto.split()

print("el numero de palabras es: ", len(palabras))

# solucion 2
contador = 1
cadena = input("Ingresa una cadena de caracteres: ")
for i in cadena:
    if i == " ":
        contador +=1
print("la cantidad de palabras es",contador)

# solucion 3
cadena = input("Ingresa una cadena de caracteres: ")
for i in cadena:
    if i == " ":
        cadena -=1

print("la cantidad de palabras es",len(cadena))