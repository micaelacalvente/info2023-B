import random,time

# Listas
palabras = ["yaguarete","carpincho","yacare","yarara","carancho","hornero"]
ayudas = ["Felino chaqueño","Amistoso con otras especies","Reptil de tamaño mediano","Serpiente común chaqueña","Ave rapaz","Su nido es el más resistente"]

# Funcion para mostrar guiones en vez de la palabra
def mostrar_palabra(palabra, letras_correctas):
    resultado = ""
    for letra in palabra:
        if letra in letras_correctas:
            resultado += letra
        else:
            resultado += "_"
    return resultado

#Obtiene la posicion de la palabra secreta en la lista e imprime la pista en la misma posicion de la lustas de pista
def mostrar_pista(palabra):
    indice = palabras.index(palabra)
    pista = ayudas[indice]
    return pista

# Función principal del juego
def ahorcado():
    #selecciona una plabra aleatoria de la lista
    palabra_secreta = random.choice(palabras)
    intentos = 6
    #listas para guardar las letras ingresadas
    letras_correctas = []
    letras_incorrectas = []

    print("¡Juego del Ahorcado!\n")

    print("  ________________     ")
    print("  |              |     ")
    print("  |              |     ")
    print("  |              ┘     ")
    print("  |                    ")
    print("  |                    ")
    print("  |                    ")
    print("  ________")
    print("""""")
    print("Intentos:", intentos)

    while intentos > 0:
        palabra_actual = mostrar_palabra(palabra_secreta, letras_correctas)
        print(f"Palabra actual:", palabra_actual)
        print("Pista:", mostrar_pista(palabra_secreta))
        print("""""")
        print(f"Letras incorrectas:", letras_incorrectas)
        print("""""")
        letra = input("Ingresa una letra: ").lower()
        print("""""")

        #Detecta si se ingreso un caracter y al mismo tiempo si la palabra no se adivino todavia
        if not letra.isalpha() and not palabra_actual == palabra_secreta:
            print('>>>No ingresaste nada<<<')
            print("""""")
            continue
        
        #Muestra un mensaje si las letras se repiten
        if letra in letras_correctas or letra in letras_incorrectas:
            print(">>>Ya intentaste con esa.<<<")
            print("""""")
            continue
        #Muestra un mensaje si las letras son más de una y no resta intentos
        if len(letra)>1:
            print('>>>Intenta solo con una letra.<<<')
            print("""""")
            continue

        #Almacena las letras correctas en la lista y controla si la palabra se adivinó
        if letra in palabra_secreta:
            letras_correctas.append(letra)            
            if set(palabra_actual) == set(palabra_secreta):
                print("¡Felicidades! Has adivinado la palabra")
                print("""""") 
                break
        #Almacena las letras incorrectas, resta vidas y dibuja en código ASCII
        else:
            letras_incorrectas.append(letra)
            intentos -= 1
            print(f">Letra incorrecta. Te quedan", intentos, "intentos.<")
            print("""""")
            # Dibujo del ahorcado en ASCII
            if intentos == 5:
                print("  ________________    ")
                print("  |               |   ")
                print("  |               |   ")
                print("  |               O   ")
                print("  |                   ")
                print("  |                   ")
                print("  |                   ")
                print("  ________")
                print("""""")
            elif intentos == 4:
                print("  ________________    ")
                print("  |               |   ")
                print("  |               |   ")
                print("  |               O   ")
                print("  |               |   ")
                print("  |                   ")
                print("  |                   ")
                print("  ________")
                print("""""")
            elif intentos == 3:
                print("  ________________    ")
                print("  |               |   ")
                print("  |               |   ")
                print("  |               O   ")
                print("  |              /|   ")
                print("  |                   ")
                print("  |                   ")
                print("  ________")
                print("""""")
            elif intentos == 2:
                print("  ________________    ")
                print("  |               |   ")
                print("  |               |   ")
                print("  |               O   ")
                print("  |              /|\  ")
                print("  |                   ")
                print("  |                   ")
                print("  ________")  
                print("""""")              
            elif intentos == 1:
                print("  ________________    ")
                print("  |               |   ")
                print("  |               |   ")
                print("  |               O   ")
                print("  |              /|\  ")
                print("  |              /    ")
                print("  |                   ")
                print("  ________")
                print("""""")
            elif intentos == 0:
                print("  ________________    ")
                print("  |               |   ")
                print("  |               |   ")
                print("  |               O   ")
                print("  |              /|\  ")
                print("  |              / \  ")
                print("  |                   ")
                print("  ________")
                print("""""")
                print(f"¡Perdiste! La palabra era:", palabra_secreta)  
                print("""""") 
    op = input("Queres volver a jugar? (s/n)").lower()
    return op

while True:
    reset = ahorcado()
    if reset == "n":
        print("""""") 
        print("Gracias por jugar!")
        print("""""") 
        time.sleep(2)
        break
  
    