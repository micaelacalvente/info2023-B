import os
import random
import time


# Función para limpiar consola
def limpiar_pantalla():
    if os.name == "posix":  # En sistemas tipo Unix (macOS y Linux)
        os.system("clear")
    elif os.name == "nt":  # En Windows
        os.system("cls")


def dame_palabra():
    """
    selecciona una palabra random de una lista

    Returns:
        str: la palabra de la lista
    """
    palabras = ["arbol", "casa", "moto", "teclado", "manzana"]
    return random.choice(palabras)


def ocultar_palabra(palabra):
    '''
    Función que oculta la palabra en una lista

    Args:
        palabra (str): la palabra a ocultar

    Returns:
        str: la palabra oculta
    '''
    lista = []
    for _ in palabra:
        lista.append('_')
    return ''.join(lista)


def verificar_una_letra():
    """
    Función que verifica si el usuario ingresó correctamente el tipo y si la letra es de longitud 1

    Returns:
        str: la letra que ingresó
    """
    letra_ingresada = None
    while True:
        letra_ingresada = input("Ingrese una letra: ")
        if len(letra_ingresada) == 1 and not letra_ingresada.isnumeric():
            return letra_ingresada
        else:
            print("Por Favor ingrese correctamente un caracter. Intentelo de nuevo")


def jugar_partida():
    '''
    Esta función maneja una partida individual del juego del ahorcado.
    Ejecuta el juego y sigue pidiendo al jugador que adivine letras
    hasta que el jugador gane, pierda o alcance el límite de intentos (5).
    '''
    palabra_secreta = dame_palabra().upper()
    letras_oculta = list(ocultar_palabra(palabra_secreta))
    letras_adivinadas = []
    letras_incorrectas = []
    contador = 0

    while ''.join(letras_oculta) != palabra_secreta and contador < 6:
        mostrar_ahorcado(contador)  # Muestra el estado actual del ahorcado
        print(" "*31,' '.join(letras_oculta))  # Muestra las letras adivinadas y espacios en blanco para las no adivinadas
        print("")
        print("Letras Incorrectas:",'-'.join(letras_incorrectas))  # Muestra las letras incorrectas ingresadas por el jugador
        print("")
        print("Intentos permitidos:", 6-len(letras_incorrectas))  # Muestra intentos restantes
        print("")
        letra = verificar_una_letra().upper()  # Solicita al jugador que ingrese una letra

        if letra in palabra_secreta:



            for pos, ch in enumerate(palabra_secreta, 0):
            # Verifica si la letra ingresada por el jugador está en la palabra secreta y es igual al carácter en la posición actual
                if letra in palabra_secreta and letra == ch:
                 
                    letras_oculta[pos] = letra  # Actualiza la palabra oculta con la letra adivinada
                
        # Verifica si la letra ingresada por el jugador no está en la palabra secreta
        if letra not in palabra_secreta:
            letras_incorrectas.append(letra)  # Agrega la letra incorrecta a la lista de letras incorrectas
            contador += 1  # Incrementa el contador de intentos fallidos

    palabra_adivinada = ''.join(letras_oculta)  # Convierte las letras adivinadas en una cadena
    estado_juego(contador, palabra_adivinada, palabra_secreta)  # Verifica el estado del juego después del bucle

def intro():
   
    img = ["",
           r"                                                                          .-.",
           r"                            || |                   ╔══════════╗            ) )",
           r"                            || |   ,               ║ ╔═══════╗║           '-'",
           r"                            || |  | |              ║ ║       ║║",
           r"                            || '--' |              ║ ║       ",
           r"                      ,,    || .----'              ║ ║       ",
           r"                     || |   || |                   ║ ║       ",
           r"                     |  '---'| |                   ║ ║       ",
           r"                     '------.| |                   ║ ║     ",
           r"                     ((_))  || |                   ║ ║       ",
           r"                     (o o)  || |                 __║ ║__       ",     
           r"                   ___\_/___||_|________________║_______║___________",
           r"                 ",  
           r"     >>===============================================================================<<",
           r"     || $$$$$$\   $$$$$$\         $$$$$$\   $$$$$$\  $$\      $$\ $$$$$$$$\  $$$$$$\  ||",
           r"     ||$$  __$$\ $$  __$$\       $$  __$$\ $$  __$$\ $$$\    $$$ |$$  _____|$$  __$$\ ||",
           r"     ||$$ /  \__|$$ /  $$ |      $$ /  \__|$$ /  $$ |$$$$\  $$$$ |$$ |      $$ /  \__|||",
           r"     ||$$ |$$$$\ \$$$$$$$ |      $$ |$$$$\ $$$$$$$$ |$$\$$\$$ $$ |$$$$$\    \$$$$$$\  ||",
           r"     ||$$ |\_$$ | \____$$ |      $$ |\_$$ |$$  __$$ |$$ \$$$  $$ |$$  __|    \____$$\ ||",
           r"     ||$$ |  $$ |$$\   $$ |      $$ |  $$ |$$ |  $$ |$$ |\$  /$$ |$$ |      $$\   $$ |||",
           r"     ||\$$$$$$  |\$$$$$$  |      \$$$$$$  |$$ |  $$ |$$ | \_/ $$ |$$$$$$$$\ \$$$$$$  |||",
           r"     || \______/  \______/        \______/ \__|  \__|\__|     \__|\________| \______/ ||",
           r"     >>===============================================================================<<",]

    animador_img(img,0.05)
    time.sleep(1)

def jugar_ahorcado():
    '''
    Esta función es la función principal del juego del ahorcado.

    Inicia el juego, selecciona una palabra secreta y llama a la función para jugar una partida.
    También permite al usuario decidir si desea continuar jugando después de una partida.

    La función se ejecuta hasta que el usuario decida no continuar jugando.
    '''
    continuar = None
    opcion_seleccionada = menu()
    while continuar != 'n' and not opcion_seleccionada is None:
        continuar = input("Desea continuar jugando? SI(s)-NO(n): ").lower()
        if continuar == 's':

            jugar_partida()  # Llama a la función para jugar una partida.
           
            continue
        elif continuar == 'n':
            break
        elif continuar != 's' or continuar != 'n':
            print('Ingrese correctamente.') # Mensaje de error si el usuario ingresa una opción inválida.
            continue



def menu():

    '''
    Función que muestra un menu con las opciones de jugar al juego o salir de la aplicación

    returns:
        int o None: la opción seleccionada
    '''
    limpiar_pantalla()
    print('''
    \b\b\b\bJuego del ahorcado Grupo 9

    1. Jugar
    2. Salir
    ''')
    while True:
        opcion = input("Seleccionar opción: ")
        if opcion.isnumeric() and opcion == '1':

            jugar_partida()
            return int(opcion)
        elif opcion.isnumeric() and opcion == '2':
            break   # Se rompe el bucle y devuelve None - Cuando una función no devuelve nada por default es None
        else:
            print('Ingrese correctamente.') # Mensaje de error si el usuario ingresa una opción inválida.
            continue



def estado_juego(intentos, palabra_correcta, palabra_secreta):
    '''
    Imprime en pantalla si el usuario ganó o perdió

    Args:
        intentos (int): número de intentos realizados
        palabra_correcta (str): palabra adivinada por el usuario
        palabra_secreta (str): palabra secreta que el usuario debe adivinar
    '''
    limpiar_pantalla()
    if intentos == 6: 
        img_perdiste()

    elif palabra_correcta == palabra_secreta:
        img_ganaste()



def mostrar_ahorcado(intentos):
    """
    Muestra una representación gráfica
    del estado actual del ahorcado basado
    en el número de intentos restantes
    """
    limpiar_pantalla()
    if intentos == 0:
        print(
            r"""                                  
                                                                    .-.
                      || |                   ╔══════════╗            ) )
                      || |   ,               ║ ╔═══════╗║           '-'
                      || |  | |              ║ ║       ║║
                      || '--' |              ║ ║       
                ,,    || .----'              ║ ║       
               || |   || |                   ║ ║       
               |  '---'| |                   ║ ║       
               '------.| |                   ║ ║          
               ((_))  || |                   ║ ║
               (o o)  || |                 __║ ║__            
               _\_/___||_|________________║_______║___________
          """
        )
    elif intentos == 1:
        print(
           r"""                                  
                                                                    .-.
                      || |                   ╔══════════╗            ) )
                      || |   ,               ║ ╔═══════╗║           '-'
                      || |  | |              ║ ║       ║║
                      || '--' |              ║ ║       🎩
                ,,    || .----'              ║ ║       
               || |   || |                   ║ ║       
               |  '---'| |                   ║ ║       
               '------.| |                   ║ ║          
               ((_))  || |                   ║ ║
               (o o)  || |                 __║ ║__            
               _\_/___||_|________________║_______║___________
          """
        )
    elif intentos == 2:
        print(
            r"""                                  
                                                                    .-.
                      || |                   ╔══════════╗            ) )
                      || |   ,               ║ ╔═══════╗║           '-'
                      || |  | |              ║ ║       ║║
                      || '--' |              ║ ║       🎩
                ,,    || .----'              ║ ║       😭
               || |   || |                   ║ ║       
               |  '---'| |                   ║ ║       
               '------.| |                   ║ ║          
               ((_))  || |                   ║ ║
               (o o)  || |                 __║ ║__            
               _\_/___||_|________________║_______║___________
          """
        )
    elif intentos == 3:
        print(
            r"""                                  
                                                                    .-.
                      || |                   ╔══════════╗            ) )
                      || |   ,               ║ ╔═══════╗║           '-'
                      || |  | |              ║ ║       ║║
                      || '--' |              ║ ║       🎩
                ,,    || .----'              ║ ║       😭
               || |   || |                   ║ ║       👕
               |  '---'| |                   ║ ║       
               '------.| |                   ║ ║          
               ((_))  || |                   ║ ║
               (o o)  || |                 __║ ║__            
               _\_/___||_|________________║_______║___________
          """
        )
    elif intentos == 4:
        print(
            r"""                                  
                                                                    .-.
                      || |                   ╔══════════╗            ) )
                      || |   ,               ║ ╔═══════╗║           '-'
                      || |  | |              ║ ║       ║║
                      || '--' |              ║ ║       🎩
                ,,    || .----'              ║ ║       😭
               || |   || |                   ║ ║       👕
               |  '---'| |                   ║ ║       👖
               '------.| |                   ║ ║          
               ((_))  || |                   ║ ║
               (o o)  || |                 __║ ║__            
               _\_/___||_|________________║_______║___________
          """
        )
    elif intentos == 5:
        print(
            r"""                                  
                                                                    .-.
                      || |                   ╔══════════╗            ) )
                      || |   ,               ║ ╔═══════╗║           '-'
                      || |  | |              ║ ║       ║║
                      || '--' |              ║ ║       🎩
                ,,    || .----'              ║ ║       😭
               || |   || |                   ║ ║       👕
               |  '---'| |                   ║ ║       👖
               '------.| |                   ║ ║       🧦  
               ((_))  || |                   ║ ║
               (o o)  || |                 __║ ║__            
               _\_/___||_|________________║_______║___________
          """
        )       
        


def img_ganaste():
   
    # se arma una lista con cada liena de la imagen 
    img = [r"",
           r"                        .* *.               `o`o` ",                                
           r"                        *. .*              o`o`o`o      ^,^,^",
           r"                          * \               `o`o`     ^,^,^,^,^",
           r"                             \     ***        |       ^,^,^,^,^",
           r"                              \   *****       |        /^,^,^",
           r"                               \   ***        |       /",
           r"                   ~@~*~@~      \   \         |      /",
           r"                 ~*~@~*~@~*~     \   \        |     /",
           r"                 ~*~@~*~@~*~      \   \       |    /     #$#$#        .`'.;.",
           r"                 ~*~@~*~@~*~       \   \      |   /     #$#$#$#   00  .`,.',",
           r"                   ~@~*~@~ \        \   \     |  /      /#$#$#   /|||  `.,'",
           r"                ____________\________\___\____|_/______/_________|\/\___||______",
           r"               ",
           r"                $$$$$$$$\                                            $$\ ",
           r"                $$  __$$\                                           $$ | ",
           r"                $$ /  \__| $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$$\ $$$$$$\    $$$$$$\  ",
           r"                $$ |$$$$\  \____$$\ $$  __$$\  \____$$\ $$  _____|\_$$  _|  $$  __$$\ ",
           r"                $$ |\_$$ | $$$$$$$ |$$ |  $$ | $$$$$$$ |\$$$$$$\    $$ |    $$$$$$$$ |",
           r"                $$ |  $$ |$$  __$$ |$$ |  $$ |$$  __$$ | \____$$\   $$ |$$\ $$   ____|",
           r"                \$$$$$$  |\$$$$$$$ |$$ |  $$ |\$$$$$$$ |$$$$$$$  |  \$$$$  |\$$$$$$$\ ",
           r"                \______/  \_______|\__|  \__| \_______|\_______/    \____/  \_______| "]
    
    animador_img(img,0.05)
        

    print(r'''       


    ''')

def img_perdiste():
    img = [r"",
           r"                                                                          .-.",
           r"                            || |                   ╔══════════╗            ) )",
           r"                            || |   ,               ║ ╔═══════╗║           '-'",
           r"                            || |  | |              ║ ║       ║║",
           r"                            || '--' |              ║ ║       💀",
           r"                      ,,    || .----'              ║ ║       F",
           r"                     || |   || |                   ║ ║       I",
           r"                     |  '---'| |                   ║ ║       N",
           r"                     '------.| |                   ║ ║     ",
           r"                     ((_))  || |                   ║ ║       ",
           r"                     (o o)  || |                 __║ ║__       ",     
           r"                   ___\_/___||_|________________║_______║___________",
           r"                 ",  
           r"                   $$$$$$$\                            $$ |$$\             $$\ ",
           r"                   $$  __$$\                           $$ |\__|            $$ |",
           r"                   $$ |  $$ | $$$$$$\   $$$$$$\   $$$$$$$ |$$\  $$$$$$$\ $$$$$$\    $$$$$$\ ",
           r"                   $$$$$$$  |$$  __$$\ $$  __$$\ $$  __$$ |$$ |$$  _____|\_$$  _|  $$  __$$\ ",
           r"                   $$  ____/ $$$$$$$$ |$$ |  \__|$$ /  $$ |$$ |\$$$$$$\    $$ |    $$$$$$$$ |",
           r"                   $$ |      $$   ____|$$ |      $$ |  $$ |$$ | \____$$\   $$ |$$\ $$   ____|",
           r"                   $$ |      \$$$$$$$\ $$ |      \$$$$$$$ |$$ |$$$$$$$  |  \$$$$  |\$$$$$$$\ ",
           r"                   \__|       \_______|\__|       \_______|\__|\_______/    \____/  \_______|"]
      
    animador_img(img,0.05)


def animador_img(img, segundos):
   '''
   crea una animación que muestra una imagen línea por línea,
   donde cada línea se muestra de abajo hacia arriba. 
   La velocidad de la animación se controla mediante la pausa de x segundos entre cada línea.
   '''
 

    #Comienza un bucle while que se ejecutará mientras el valor de cont sea menor o igual a la longitud de la lista img. 
    #Esto significa que la animación se ejecutará para cada línea de la imagen.
   cont = 0
   while cont <= len(img):
       
       #se encarga de limpiar la pantalla de la consola para que la animación se muestre de forma limpia.
       limpiar_pantalla()
        
       
       #aqui se dibuja la secuencia de imagen debido a que si el recorrido es normal la imagen se dibuja en forma inversa 
       #por ello serecorre una secuencia de números en orden inverso, desde la longitud de la lista img hasta 1.
       #Esto significa que i tomará valores desde la longitud de la lista hacia abajo
       for i in range(len(img), 0, -1):
          
           #  se decide qué línea de la imagen imprimir y cuál dejar en blanco.
           #  Si i es menor que cont, se imprime la línea img[i*-1]. 
           # Nota que i*-1 se usa para acceder a las líneas en orden inverso. 
           # Si i es mayor o igual a cont, se imprime una línea en blanco.
           if i<cont:
             print(img[i*-1])
             
           else: 
             print("")

       #Se agrega una pausa de 0.1 segundos antes de continuar con la próxima iteración del bucle while. Esto controla la velocidad de la animación.
       time.sleep(segundos)
       cont +=1          



if __name__ == '__main__':
    intro()
    jugar_ahorcado()


#Comentarios letras_adivinadas.insert(pos, letra)  no funciona

