#Versión del juego con menú y selección de dificultad

import random

#Dibujo ahorcado
def dibujo(intentos):
    if intentos == 6:
        print("    +---+")
        print("    |   |")
        print("        |")
        print("        |")
        print("        |")
        print("        |")
        print("   =========")
    elif intentos == 5:
        print("    +---+")
        print("    |   |")
        print("    O   |")
        print("        |")
        print("        |")
        print("        |")
        print("   =========")
    elif intentos == 4:
        print("    +---+")
        print("    |   |")
        print("    O   |")
        print("    |   |")
        print("        |")
        print("        |")
        print("   =========")
    elif intentos == 3:
        print("    +---+")
        print("    |   |")
        print("    O   |")
        print("   /|   |")
        print("        |")
        print("        |")
        print("   =========")
    elif intentos == 2:
        print("    +---+")
        print("    |   |")
        print("    O   |")
        print("   /|\  |")
        print("        |")
        print("        |")
        print("   =========")
    elif intentos == 1:
        print("    +---+")
        print("    |   |")
        print("    O   |")
        print("   /|\  |")
        print("   /    |")
        print("        |")
        print("   =========")
    elif intentos == 0:
        print("    +---+")
        print("    |   |")
        print("    O   |")
        print("   /|\  |")
        print("   / \  |")
        print("        |")
        print("   =========")

# Lista de palabras para adivinar
palabras_faciles = ["ACEITE", "ACUARELA", "ARANDELA", "ARSENAL", "BICICLETA", "BIGOTE", "CAMUFLAJE", "CANDIDATO", "CARPINTERIA", "CEREMONIA", "CLANDESTINO", "CUCARACHA", "DEMOCRACIA", "DETECTIVE", "DOMESTICO", "DUODENO", "ELECTRICIDAD", "ELEGANTE", "EPIDEMIA", "EQUINOCCIO", "ESCARABAJO", "ESCAPARATE", "ESCARLATA", "ESCEPTICO", "ESTIMULO", "FABULOSO", "FLAMENCO", "FRANELA", "GABINETE", "GARRAPATA", "GEOGRAFIA", "HIPOPOTAMO", "INMUNIDAD", "INOCENTE", "INVESTIGAR", "JAQUECA", "KIOSCO", "LABERINTO", "LOTERIA", "MARIONETA", "MALVADO", "MERCADO", "MERENGUE", "MONEDA", "MORETON", "MUCAMA", "NAVIDAD", "NEGOCIO", "NICOTINA","NOVELA", "OBEDECER", "OCTUBRE", "ORANGUTAN", "PALACIO", "PANORAMA", "PANTALON", "PELICULA", "PEREGRINO", "PETROLEO", "PIGMENTO", "PIRAMIDE", "PIROPO", "PLANETA", "POLITICA", "POMADA", "POTASIO", "PROGRAMA", "PROTOCOLO", "PSICOLOGIA", "PUPITRE", "RADAR", "RADIO", "RECLUSO", "RELOJ", "RESERVA", "RESTAURANTE", "ROTISERIA", "RUPESTRE", "SARCASMO", "SEMANA", "SINIESTRO", "SIRENA", "SOFISTICADO", "TATUAJE", "TARJETA", "TESTARUDO", "TITERE", "TOMATE", "VACUNA", "VECINO", "VENENO", "VICTORIA", "VIOLETA", "VIUDA", "VOCACION", "YATE", "YELMO", "YOGA", "ZANAHORIA", "ZURDO"]

palabras_dificiles = ["ACROSTICO", "AFRODISIACO", "AGNOSTICISMO", "ALABARDA", "ALEGORIA", "AMBROSIA", "ANACRONISMO", "ANFRACTUOSO", "ARTILUGIO", "ASTROLABIO", "BARIATRICO", "BERGANTIN", "BUHARDILLA", "CALIPIGIO", "CARAMBOLA", "CARIATIDE", "CATACRESIS", "CHAMBERGO", "CIRCADIANO", "CONDESTABLE", "CRISELEFANTINO", "DIACRITICO", "DISPEPSIA", "EMPERIFOLLADO", "EPANADIPLOSIS", "ERITROCITO", "ERGASTULA", "ESCAFOIDE", "ESTEGANALISIS", "FAQUIR", "FILATELIA", "GALICURSI", "GAZNAPIRO", "GERBERA", "HIMENEO", "INCONSUTIL", "INCUNABLE", "INEXORABLE", "JITANJAFORA", "KERMES", "LEITMOTIV", "LEMPIRA", "LIBERTINAJE", "MACADAN", "MANGLAR", "MAYOLICA", "MAZMORRA", "MEQUETREFE", "MITRIADISMO", "MORALEJA", "MORGANATICO", "NARCISISMO", "NEGACIONISMO", "NIGROMANCIA", "OBSTETRICIA", "OLEAGINOSO", "OLIBANO", "OMINOSO", "ORONPENDOLA", "PALIMPSESTO", "PANEGIRICO", "PANTAGRUELICO", "PARANGON", "PAROXISMO", "PECUARIO", "PERIPECIA", "PINACOTECA", "PINDARICO", "PINGANILLO", "PLEYADE", "PLUTOCRACIA", "POLIMATIA", "PONTIFICE", "PRESBITERO", "PRIAPISMO", "PROPOLEO", "QUIROPRAXIA", "RECALCITRANTE", "RETALIACION", "RETRUECANO", "SORORIDAD", "TANDEM", "TARTUFO", "TAUTOLOGIA", "TINNITUS", "TIQUISMIQUIS", "TRAPICHE", "TRIFULCA", "TROCANTER", "TROGLODITA", "TROMBOCITO", "UFANAR", "VERONAL", "VITOFILIA", "VITUPERAR", "VODEVIL", "YUGULAR", "ZAFARRANCHO", "ZAHON", "ZALAMERO"]

# Función para seleccionar una palabra al azar
def seleccionar_palabra():
    print("\nDificultad:")
    print("\n1 - Elegir palabra fácil")
    print("2 - Elegir palabra difícil")
    dificultad_seleccionada = input("")
    if dificultad_seleccionada == "1":
        return random.choice(palabras_faciles)
    else:
        return random.choice(palabras_dificiles)

# Función para inicializar la palabra oculta
def inicializar_palabra_oculta(palabra):
    return ["_" for _ in palabra]

# Función para mostrar la palabra oculta
def mostrar_palabra_oculta(palabra_oculta):
    return " ".join(palabra_oculta)

# Función principal del juego
def jugar():
    palabra_a_adivinar = seleccionar_palabra()
    palabra_oculta = inicializar_palabra_oculta(palabra_a_adivinar)
    letras_incorrectas = []

    # Número de intentos permitidos
    intentos = 6
    print(f"\n¡Tienes {intentos} intentos para adivinar la palabra!")

    while intentos > 0 and "_" in palabra_oculta:
        print("\nPalabra a adivinar:", mostrar_palabra_oculta(palabra_oculta))
        letra = input("\nIngresa una letra: ").upper()

        #Si el caracter ingresado no es válido
        if len(letra) != 1 or not letra.isalpha():
            print("Ingresa una letra válida.")
            continue

        #Si la letra ingresada es correcta
        if letra in palabra_a_adivinar:
            print(f"¡La letra \"{letra}\" es correcta!")
            for i in range(len(palabra_a_adivinar)):
                if palabra_a_adivinar[i] == letra:
                    palabra_oculta[i] = letra
        else: #Si la letra ingresada es incorrecta
            intentos -= 1
            print(f"La letra \"{letra}\" es incorrecta. Te quedan {intentos} intentos.")
            letras_incorrectas.append(letra)
            print(f"Letras incorrectas: {letras_incorrectas}")
            dibujo(intentos)

    #Ganar o perder
    if "_" not in palabra_oculta:
        print("\n¡Felicidades! Has adivinado la palabra: {}".format(palabra_a_adivinar))
    else:
        print("\n¡Perdiste! La palabra correcta era: {}".format(palabra_a_adivinar))

#Menú de bienvenida
print("\n¡Bienvenido al juego de ahorcado!")
print("\n1 - Jugar")
print("2 - Salir")
seleccion = input("")
juego = True

while juego:
    if seleccion == "1":
        jugar()
        print("\n1 - Volver a jugar")
        print("2 - Salir")
        seleccion2 = input("")
        if seleccion2 == "1":
            continue
        else:
            break
    elif seleccion == "2":
        break
    else:
        print("Elija una opción válida")
        seleccion = input("")