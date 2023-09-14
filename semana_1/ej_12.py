#Escribe un programa que solicite al usuario su fecha de nacimiento en formato
# dd/mm/aaaa y luego imprima su edad en años.
# Utiliza la función .split()

fecha = input("Ingrese su fecha de nacimiento en formato dd/mm/aaaa")
dia, mes, anio = fecha.split("/")
edad = 2023 - int(anio)
print("Tenes", edad, "años")
