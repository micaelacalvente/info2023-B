import random
import sys

def elegir_palabra(dificultad=0):
    palabras = [["casa","java","gato","pato"],["perro","pasta","pizza"],["jardin","python","camara"]]
    if dificultad <=3 and dificultad > 0:
        return random.choice(palabras[dificultad-1])
    else :
        return random.choice(random.choice(palabras))
    
    
def mostrar_ahorcado(intentos): 
    
    ahorcado = [
            '''
            +---+
                |   
                |
                |
               ===''',
            '''
            +---+
            O   |
                |
                |
               ===''',
            '''
            +---+
            O   |
            |   |
                |
               ===''',
            '''
            +---+
            O   |
           /|   |
                |
               ===''',
            '''
            +---+
            O   |
           /|\  |
                |
               ===''',
            '''
            +---+
            O   |
           /|\  |
           /    |
               ===''',
            '''
            +---+
            O   |
           /|\  |
           / \  |
               ==='''
    ]
    return ahorcado[6-intentos]



def jugar_ahorcado():
    palabra = elegir_palabra(int(input("¡Bienvenido al Juego! Debes ingresar la dificultad con un numero entre el 1 y el 3:")))
    letras_acertadas = []
    intentos = 6
            
    print("Tendrás que adivinar la siguiente palabra: ", "_ " * len(palabra),".")
    
    while intentos > 0: 
        
        letra = input("Ingresa una letra: ") 
          
        if letra in letras_acertadas: 
            print(f"La letra {letra} ya ha sido adivinada.")
        elif letra in palabra: 
            letras_acertadas.append(letra)
        else:
            intentos -= 1
            print(f"Esa letra no se encuentra, te quedan {intentos} intentos.")
            
        print(mostrar_ahorcado(intentos))
        
        
        mostrar_palabra = " "
        for letra_palabra in palabra:
            if letra_palabra in letras_acertadas:
                mostrar_palabra += letra_palabra + " " 
            else:
                mostrar_palabra += "_ "
        
        print(mostrar_palabra) 
        
        if "_" not in mostrar_palabra:
            print("¡Felicitaciones! Adivinaste la palabra :)")
            volver()
              
    if intentos == 0:
        print(f"Ups, te quedaste sin intentos :(. La palabra era {palabra}")
        volver()
def volver():
        volverr = input("¿Quieres volver a jugar? SI/NO ").upper()
        if volverr == "SI":
           jugar_ahorcado()
        else: 
            print("¡Gracias por jugar!")
            exit()

jugar_ahorcado()
