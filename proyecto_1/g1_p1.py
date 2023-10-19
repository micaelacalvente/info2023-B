import random
import time

palabras = ["tecnologia", "animales", "estudiar", "aprender", "videojuegos"]

def verificar_letra(letra, palabra_secreta, adivinadas, incorrectas):
    
    if letra in palabra_secreta:
        if letra in adivinadas:
            print("Esa letra ya la has adivinado. Vuelve a intentarlo con otra")
        else:
            adivinadas.append(letra)
    else:
        incorrectas.append(letra)
        
    palabra_actualizada = ""
    for letra_secreta in palabra_secreta:
        if letra_secreta in adivinadas:
            palabra_actualizada += letra_secreta
        else:
            palabra_actualizada += "_"
    
    print("Palabra secreta:", palabra_actualizada)
    
    dibujo_ahorcado = [
    """
     _________  
    |         |    
    |              
    |           
    |           
    |              
    """,
    """
     _________     
    |         |   
    |         0    
    |             
    |             
    |                 
    """,
    """
     _________    
    |         |   
    |         0   
    |         |   
    |             
    |                  
    """,
    """
     _________    
    |         |   
    |         0   
    |         |\  
    |             
    |                  
    """,
    """
     _________   
    |         |   
    |         0   
    |        /|\  
    |             
    |                  
    """,
    """
     _________     
    |         |    
    |         0    
    |        /|\   
    |          \   
    |                
    """,
    """
     _________     
    |         |    
    |         0    
    |        /|\   
    |        / \   
    |                   
    """
    ]
    
    print(dibujo_ahorcado[len(incorrectas)])
        
def jugar():
    intentos = 6
    adivinadas = []
    incorrectas = []
       
    dibujo_ahorcado = [
    """
     _________  
    |         |    
    |              
    |           
    |           
    |              
    """,
    """
     _________     
    |         |   
    |         0    
    |             
    |             
    |                 
    """,
    """
     _________    
    |         |   
    |         0   
    |         |   
    |             
    |                  
    """,
    """
     _________    
    |         |   
    |         0   
    |         |\  
    |             
    |                  
    """,
    """
     _________   
    |         |   
    |         0   
    |        /|\  
    |             
    |                  
    """,
    """
     _________     
    |         |    
    |         0    
    |        /|\   
    |          \   
    |                
    """,
    """
     _________     
    |         |    
    |         0    
    |        /|\   
    |        / \   
    |                   
    """
    ] 
   
    palabra_secreta = random.choice(palabras)
    print(' ')
    print("Bienvenidos al juego del Ahorcado del grupo N° 1  =)")
    print(' ')
    time.sleep(2)

    while intentos > 0 and set(palabra_secreta) != set(adivinadas):
        print("Letras adivinadas:", ", ".join(adivinadas))
        print("Letras incorrectas:", ", ".join(incorrectas))

        letra = input("Ingresa una letra: ").lower()

        while len(letra) != 1 or not letra.isalpha():
            print("La letra que ingresaste no es válida. Ingresa una sola letra.")
            letra = input("Ingresa una letra: ").lower()

        verificar_letra(letra, palabra_secreta, adivinadas, incorrectas)

        if letra not in palabra_secreta:
            intentos -= 1  
            
    if set(palabra_secreta) == set(adivinadas):
        print("¡Felicitaciones, has ganado! La palabra secreta era:", palabra_secreta)
    elif intentos == 0:
        print("¡Lo siento, has perdido! Te quedaste sin intentos. La palabra secreta era:", palabra_secreta)
        
    reiniciar = input("\n   Deseas volver a jugar? \n   1 - Volver a jugar \n   2 - Salir \n")
    
    if reiniciar == "1":  
        jugar()
    else:
        print("Gracias por jugar =)")
jugar()