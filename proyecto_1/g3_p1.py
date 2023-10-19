import random

# Lista de palabras para adivinar
palabras = ["edgardo", "alan", "franco", "camila", "axel", "fabian", "rodigro", "carla"]

# Función para seleccionar una palabra al azar
def seleccionar_palabra():
    return random.choice(palabras)

# Función para dibujar el muñeco
def dibujar_ahorcado(intentos):
    if intentos == 6:
        print("  _     ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |__")
    elif intentos == 5:
        print("  _     ")
        print(" |       |    ")
        print(" |       O    ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |__")
    elif intentos == 4:
        print("  _     ")
        print(" |       |    ")
        print(" |       O    ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")
        print(" |__")
    elif intentos == 3:
        print("  _     ")
        print(" |       |    ")
        print(" |       O    ")
        print(" |      /|    ")
        print(" |            ")
        print(" |            ")
        print(" |__")
    elif intentos == 2:
        print("  _     ")
        print(" |       |    ")
        print(" |       O    ")
        print(" |      /|\\  ")
        print("              ")
        print(" |            ")
        print(" |__")
    elif intentos == 1:
        print("  _     ")
        print(" |       |    ")
        print(" |       O    ")
        print(" |      /|\\  ")
        print(" |      /     ")
        print(" |            ")
        print(" |__")
    else:
        print("  _     ")
        print(" |       |    ")
        print(" |       O    ")
        print(" |      /|\\  ")
        print(" |      / \\  ")
        print(" |            ")
        print(" |__")

# Función para jugar al ahorcado
def jugar_ahorcado(palabra):
    palabra_adivinada = "_" * len(palabra)
    intentos = 6
    letras_usadas = []

    while True:
        dibujar_ahorcado(intentos)
        print(f"Alumno: {palabra_adivinada}")
        print(f"Letras usadas: {', '.join(letras_usadas)}")
        print(f"Intentos restantes: {intentos}")
        letra = input("Ingresa una letra: ").lower()

        if letra in letras_usadas or letra in "123456789":
            print("Ya has usado esa letra.")
            continue

        letras_usadas.append(letra)

        if letra in palabra:
            nueva_palabra = ""
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    nueva_palabra += letra
                else:
                    nueva_palabra += palabra_adivinada[i]
            palabra_adivinada = nueva_palabra
        else:
            intentos -= 1
            print(f"Letra incorrecta. Te quedan {intentos} intentos.")

        if palabra_adivinada == palabra:
            dibujar_ahorcado(intentos)
            print(f"¡Ganaste! El alumno es: {palabra}")
            break

        if intentos == 0:
            dibujar_ahorcado(intentos)
            print(f"¡Perdiste! El alumno era: {palabra}")
            break

palabra_a_adivinar = seleccionar_palabra()
print("¡Bienvenido al juego del ahorcado!")
print("Adivina el nombre del Estudiante")
jugar_ahorcado(palabra_a_adivinar)
