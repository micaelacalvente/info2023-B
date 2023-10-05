'''3-Crea una función llamada invertir_cadena que tome una cadena de texto como
parámetro y devuelva la cadena invertida.'''

# solucion guille
def invertir_cadena(cadena):
    return (cadena[::-1])

print(invertir_cadena("Hola"))

# solucion mauri
def invertir_cadena(cadena):
    return cadena[::-1]

# Ahora puedes probar la función
print(invertir_cadena("Mauricio Fabian Burgos"))

# solucion gero
def invertir_cadena (texto):
    texto = texto[::-1]
    return texto

texto = input("cadena: ")

print(invertir_cadena(texto))

# solucion agus
def invertir_cadena(cadena):
    cadena_invertida = cadena[::-1]
    return cadena_invertida

cadena_original = "Hola, mundo!"
cadena_invertida = invertir_cadena(cadena_original)
print(cadena_invertida)