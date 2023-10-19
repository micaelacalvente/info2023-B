import random
import time

dibujo = ['''

   +---+
   |   |
       |
       |
       |
       |

=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
FINISH HIM
=========''']

######################################## SECCIÓN DE FUNCIONES ###################################################################################

def palabra_aleatoria(lista):
    '''Selecciona una palabra aleatoria de la lista'''
    palabra = random.choice(lista)
    return palabra

def ingresoLetra():
    '''Pide el ingreso de una letra y verifica que sea una letra'''
    x = input("Ingrese una letra: ").upper()
    
    while len(x) != 1 or x.isalpha() == False:
        time.sleep(1)
        x = input("Ingrese una letra! (NO palabra, número o signo): ").upper()
    return x

def letraPorLetra(palabra):
    '''Crea una lista con las letras de la palabra'''
    lista = []
    for i in palabra:
        lista.append(i)
    return lista

def jugarDeNuevo():
    '''Verifica que se ingrese SI o NO'''
    x = input("\nQueres jugar de nuevo? SI - NO:\n").lower()
    while x != "no" and x != "si":
        time.sleep(1)
        x = input("Ingrese una opción valida (SI - NO): ")
    return x

def eliminarLetras(letra, lista):
    '''Elimina la letra de lista tantas veces como aparezca'''
    for i in lista:
        if letra == i:
            lista.remove(i)
    return lista

def letrasUsadas(letra, cadena):
    '''Muestra las letras utilizadas hasta el momento'''
    if len(cadena) == 0:
        cadena += letra
    else:
        cadena += (", " + letra)
    time.sleep(1)
    print(f'\nLetras usadas: {cadena}')
    return cadena

def letraPorGuiones(letra, palabra, lista):
    '''Crea o reemplaza una lista letras y guiones'''
    contador = 0
    if len(lista) == 0: #Para saber si lista es vacia o contiene elementos
        agregar = True
    else:
        agregar = False

    for i in palabra:

        if letra == i and agregar == True: #Verifca si a la lista hay que agregar o editar elementos
            lista.append(i + " ")
        elif agregar == True:
            lista.append("_ ")

        if letra == i and agregar == False:
            lista[contador] = letra + " "
        contador += 1
    return lista

def despedida():
    '''termina el juego y se despide'''
    print("\nHASTA LA PRÓXIMA. GRACIAS POR JUGAR CON EL GRUPO 7")
    print("----------------------------------------------------------------------------------------------------")
    time.sleep(3)
    return False

def seguir():
    '''Verifica si desea seguir o salir'''
    time.sleep(1)
    seguir = input("\nVolver atrás? SI - NO\n").upper()
    while seguir != "SI" and seguir != "NO":
        time.sleep(1)
        seguir= input(f"\n{seguir} no es una opción válida, intente de nuevo.\n").upper()
    if seguir =="NO":
        time.sleep(1)
        jugar = despedida()
        return jugar
    else:
        time.sleep(1)
        print("----------------------------------------------------------------------------------------------------")
        return True

#########################################################################################################################

######################################## INICIO PROGRAMA ###########################################################

lista_palabras = ["heladera", "manzana", "informatorio", "programacion", "tortuga", "ventilador", "python", "mochila", "cocina","celular", "berenjena", "zanahoria", "servilleta", "yerba"]
jugar = True

while jugar: #MENU
    if len(lista_palabras) == 0:  #Termina si se terminan las palabras de la lista
        print("FIN DEL JUEGO. GRACIAS POR JUGAR CON EL GRUPO 7")
        break

    print("Bienvenido al AHORCADO del Grupo 7")
    print("\nElija una opción:")
    print("1. Iniciar Partida")
    print("2. Reglas del juego")
    print("3. Listado de palabras")
    print("4. Terminar partida")
    
    op = input() #op = opción
    
    time.sleep(1)

    #Opciones Menu
    if op not in ("1234"):
        print(f"\n{op} no es una opción válida, intente de nuevo.\n")
        
    if op == "4":
        jugar = despedida()

    if op == "3":
        print("\nLista de palabras:")
        i = 1
        for palabra in lista_palabras:
            print(f"{i}- {palabra.upper()}")
            i += 1
        time.sleep(1)    
        jugar = seguir()
            
    if op == "2":
        print("\nEl juego consiste en intentar adivinar una palabra.\nEsta es elegida aleatoriamente. Debe adivinar letra por letra.\nVas a tener 6 intentos para adivinar la palabra completa.")
        jugar = seguir()
    
    if op == "1":
        print("\nJUGANDO AL AHORCADO CON EL GRUPO 7") #Inicio del juego
        print(dibujo[0]) #Imprime soporte (horca)
        
        intento = 0 #Para saber cuantos intento quedan
        correctas = 0 #Para saber cuantas correctas faltan
        letras_acertadas = [] #Para armar la palabra con guiones
        letras_usadas = "" #Para mostrar las letras que ya usadas
        contador_letra = 1 #Solo para diferenciar entre un intento y otro

        palabra_actual = palabra_aleatoria(lista_palabras).upper()
        print(f"Palabra a adivinar: {len(palabra_actual)*'_ ' }\n")
        
        letras_palabra = letraPorLetra(palabra_actual) #Para eliminar letras encontradas
        
        
    
        while intento < len(dibujo)-1: #Se ejecuta hasta que el dibujo de ahorcado se complete
            time.sleep(2)
            print(f"Ingresa la {contador_letra}° letra") #Contador de letra
            contador_letra += 1
            letra = ingresoLetra()
            time.sleep(1)


            if letra in letras_palabra: #Verifica que la letra este en la palabra
                
                letras_acertadas = letraPorGuiones(letra, palabra_actual, letras_acertadas) #Para letras acertadas y guiones
                palabra_unida = "".join(letras_acertadas)
                print(f"\nLa letra esta en la palabra: {palabra_unida.upper()}")

                correctas += letras_palabra.count(letra)
                letras_palabra = eliminarLetras(letra,letras_palabra) #Para no volver a contar la misma letra
            

                if correctas == len(palabra_actual): #Corta cuando se completa la palabra
                    break
                
                letras_usadas = letrasUsadas(letra, letras_usadas) #Imprime y añade a la letra actual a la lista
                print("----------------------------------------------------------------------------------------------------")

            elif letra in letras_usadas: #Verifica que no se haya elegido esa letra antes
                print("\nYa probaste con esta letra! Probá de nuevo")
                print("----------------------------------------------------------------------------------------------------")

            else: #Contador de incorrectas
                print("\nLetra Incorrecta!")
                intento +=1
                print(dibujo[intento])
                
                if len(letras_acertadas) == 0: #Muestra la palabra en forma de guiones y con las letras acertadas
                    print(f"Palabra a adivinar: {len(palabra_actual)*'_ ' }\n")
                else:
                    palabra_unida = "".join(letras_acertadas)
                    print(f"\nEstado de la palabra: {palabra_unida.upper()}")
                letras_usadas = letrasUsadas(letra, letras_usadas)
                print("----------------------------------------------------------------------------------------------------")

        if intento >= len(dibujo)-1: #Resultado del juego
            print(f"PERDISTE! La palabra era: {(palabra_actual).upper()}")
        else:
            print("----------------------------------------------------------------------------------------------------")
            print("GANASTE! ADIVINASTE LA PALABRA Y TE SALVASTE DE LA HORCA")
            print(dibujo[intento])
        
        time.sleep(2)
        de_nuevo = jugarDeNuevo() #Pregunta si se desea jugar de nuevo
        if de_nuevo == "no":
            jugar = despedida()
                        
        else:
            lista_palabras.remove(palabra_actual.lower())
            print("----------------------------------------------------------------------------------------------------")
        