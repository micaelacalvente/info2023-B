import random
jugar = True

while jugar:

    lista_palabras = ["casa","perro","gato","entrometido","nariz","beso","azucar","esternocleidomastoideo"]

    palabra_aleatoria = random.choice(lista_palabras)
    adivinando_palabra = "_"*len(palabra_aleatoria)

    errores = 0

    print("\nBienvenido al juego del Ahorcado")
    print("-----------------------------------------")





    while adivinando_palabra != palabra_aleatoria:

        if errores == 0:
            print(f"\n\n    +---+|\n         |\n         |\n         |\n         |\n         |\n   =========    {adivinando_palabra} \n ")
        elif errores == 1:
            print(f"\n\n    +---+|\n    |    |\n         |\n         |\n         |\n         |\n   =========    {adivinando_palabra} \n ")
        elif errores == 2:
            print(f"\n\n    +---+|\n    |    |\n    O    |\n         |\n         |\n         |\n   =========    {adivinando_palabra} \n ")
        elif errores == 3:
            print(f"\n\n    +---+|\n    |    |\n    O    |\n    |    |\n         |\n         |\n   =========    {adivinando_palabra} \n ")
        elif errores == 4:
            print(f"\n\n    +---+|\n    |    |\n    O    |\n   /|    |\n         |\n         |\n   =========    {adivinando_palabra} \n ")
        elif errores == 5:
            print(f"\n\n    +---+|\n    |    |\n    O    |\n   /|\   |\n         |\n         |\n   =========    {adivinando_palabra} \n ")
        elif errores == 6:
            print(f"\n\n    +---+|\n    |    |\n    O    |\n   /|\   |\n   /     |\n         |\n   =========    {adivinando_palabra} \n ")
        elif errores == 7:
            print(f"\n\n    +---+|\n    |    |\n    O    |\n   /|\   |\n   / \   |\n         |\n   =========    {adivinando_palabra} \n ")
        else:
            print("      ¡ MORISTE ! \n \n    {}           {}\n      \  _---_  /\n       \/     \/\n        |() ()|\n         \ + /\n        / HHH  \ \n       /  \_/   \ \n     {}          {}\n \n    ¡FIN DEL JUEGO! \n ")
            break

        


        # El usuario elije una letra
        letra = ""
        #print(palabra_aleatoria)

        while len(letra) != 1:
            letra = input("Elija una letra o adivine la palabra: ")

            if letra == palabra_aleatoria:
                break



        if (letra in palabra_aleatoria) and (letra != palabra_aleatoria):
            
            print("-----------------------------------------\n ")
            print(f"La palabra contiene \"{letra.upper()}\"\n ")
            print("-----------------------------------------\n ")

            palabra_aleatoria = list(palabra_aleatoria)
            adivinando_palabra = list(adivinando_palabra)
            

            for i in range(len(palabra_aleatoria)):

                if letra == palabra_aleatoria[i]:
                    adivinando_palabra[i] = palabra_aleatoria[i]


            adivinando_palabra = ''.join(adivinando_palabra)
            palabra_aleatoria = ''.join(palabra_aleatoria)

        elif letra == palabra_aleatoria:
            print("\n GANASTE, fin del juego")
            print(f"\n¨⋱ ⋮ ⋰¨ \n ⋯ ◯ ⋯¨. ︵ . \n ¨︵¸︵( ░░ )︵\n (´░░░░░░ ') ░░░' \n  `´︶´¯`︶´`︶ \n       {palabra_aleatoria.upper()} \n")
            break

        else:
            errores += 1
            print("-----------------------------------------\n ")
            print(f"La palabra no contiene \"{letra.upper()}\"\n ")
            print("-----------------------------------------\n ")
        


    else:
        print("\n GANASTE, fin del juego")

        print(f"\n¨⋱ ⋮ ⋰¨ \n ⋯ ◯ ⋯¨. ︵ . \n ¨︵¸︵( ░░ )︵\n (´░░░░░░ ') ░░░' \n  `´︶´¯`︶´`︶ \n       {palabra_aleatoria.upper()} \n")
    
    jugar_denuevo = input("desea volver a jugar? S/si - N/no").upper()

    while jugar_denuevo != ("S" or "N"):

        if jugar_denuevo == "S":
            break
        elif jugar_denuevo == "N":
            jugar = False
            print("Gracias por jugar")
            break
        else:
            continue










