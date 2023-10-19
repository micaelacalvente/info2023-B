frase = "Se la cantidad a iterar"

#dividir la frase en palabras y guardar las palabras en una lista
palabras = frase.split()
print(type(palabras))

#inicializar el contador de palabras
contador_palabras = 0

#recorrer cada palabra y contarla
for palabra in palabras:
    contador_palabras += 1
    print(f"Palabra: {palabra}")

print(f"Total de palabras: {contador_palabras}")
