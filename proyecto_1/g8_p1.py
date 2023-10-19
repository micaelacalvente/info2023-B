import random

IMAGENES_AHORCADO = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''',

'''

  +---+
  |   |
  O   |
      |
      |
      |
=========''',

'''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',

'''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',

'''

  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''',

'''

  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''',

'''

  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']

# esta funcion muestra el dibujo del ahorcado
def mostrar_ahorcado(intentos):
    print(IMAGENES_AHORCADO[6 - intentos])

# selecciona una palabra aleatoria de la lista
def seleccionar_palabra():
    palabras = ["arbol", "comida", "computadora", "videojuegos", "camioneta", "supercalifragilisticoespialidoso", "ornitorrinco","esqueleto","diccionario","empanada", "profesor","botella","guitarra"]
    return random.choice(palabras)

#  muestra la palabra oculta con letras adivinadas
def mostrar_palabra_oculta(palabra, letras_adivinadas):
    resultado = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            resultado += letra
        else:
            resultado += "_"
    return resultado

def jugar_ahorcado():
    palabra_secreta = seleccionar_palabra()
    letras_adivinadas = []
    intentos_restantes = 6

    print("Empecemos a jugar el juego de El Ahorcado!!!!")

    while True:
        mostrar_ahorcado(intentos_restantes)
        print("\nPalabra a adivinar: " + mostrar_palabra_oculta(palabra_secreta, letras_adivinadas))
        print("Intentos restantes: " + str(intentos_restantes))

        letra = input("Ingresa una letra cualquiera: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print(" ERROR ,Ingresa una sola letra válida.")
            continue

        if letra in letras_adivinadas:
            print("ya has ingresado esta letra antes, intenta con otra")
            continue

        letras_adivinadas.append(letra)

        if letra in palabra_secreta:
            print("¡Letra Correcta!. ")
        else:
            print("Letra Incorrecta. ")
            intentos_restantes -= 1

        if mostrar_palabra_oculta(palabra_secreta, letras_adivinadas) == palabra_secreta:
            print("\n¡Felicidades!!!! has adivinado la palabra, no seras ahorcado, la palabra es:"  + palabra_secreta)
            break
        elif intentos_restantes == 0:
            print("\n¡OHHH NOOOO, no has podido adivinar la palabra PERDISTE!!!!. La palabra secreta era: " + palabra_secreta)
            break

while True:
    jugar_ahorcado()
    reiniciar = input("\n¿Quieres jugar de nuevo? (s/n): ").lower()
    if reiniciar != 's':
        break