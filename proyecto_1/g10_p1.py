# Importamos turtle
import turtle

#El titulo de la ventana principal
turtle.title ("JUEGO EL AHORCADO" + " ( * > * ) ")

#Importamos random para palabras aleatorias
import random

def elegir_palabra():
    return random.choice(palabras)
palabras = ["tomate", "lechuga", "cebolla", "batata", "zapallo","acelga", "zanahoria" ]

#Animación en los intentos
def dibujo_juego (intentos):
    if intentos ==6:
        turtle.reset()
        turtle.hideturtle()
        turtle.speed(5)
        turtle.penup()
        turtle.goto(-50, -150)
        turtle.pendown()
        turtle.forward(100)
        turtle.penup()
        turtle.goto(0, -150)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(200)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(20)
    if intentos ==5:
        turtle.reset()
        turtle.hideturtle()
        turtle.speed(5)
        turtle.penup()
        turtle.goto(-50, -150)
        turtle.pendown()
        turtle.forward(100)
        turtle.penup()
        turtle.goto(0, -150)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(200)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(20)
        turtle.penup()
        turtle.goto( 80, 10)
        turtle.pendown()
        turtle.circle(20)
    if intentos ==4:  
        turtle.reset()
        turtle.hideturtle()
        turtle.speed(5)
        turtle.penup()
        turtle.goto(-50, -150)
        turtle.pendown()
        turtle.forward(100)
        turtle.penup()
        turtle.goto(0, -150)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(200)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(20)
        turtle.penup()
        turtle.goto( 80, 10)
        turtle.pendown()
        turtle.circle(20)        
        turtle.penup()
        turtle.goto(100,-70)
        turtle.pendown()
        turtle.left(-180)
        turtle.forward(60)
    if intentos ==3:
        turtle.reset()
        turtle.hideturtle()
        turtle.speed(5)
        turtle.penup()
        turtle.goto(-50, -150)
        turtle.pendown()
        turtle.forward(100)
        turtle.penup()
        turtle.goto(0, -150)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(200)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(20)
        turtle.penup()
        turtle.goto( 80, 10)
        turtle.pendown()
        turtle.circle(20)  
        turtle.penup()
        turtle.goto(100,-70)
        turtle.pendown()
        turtle.left(-180)
        turtle.forward(60)
        turtle.penup()
        turtle.goto(100,-30)
        turtle.pendown()
        turtle.right(45)
        turtle.forward(40)
    if intentos ==2:
        turtle.reset()
        turtle.hideturtle()
        turtle.speed(5)
        turtle.penup()
        turtle.goto(-50, -150)
        turtle.pendown()
        turtle.forward(100)
        turtle.penup()
        turtle.goto(0, -150)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(200)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(20)       
        turtle.penup()
        turtle.goto( 80, 10)
        turtle.pendown()
        turtle.circle(20)  
        turtle.penup()
        turtle.goto(100,-70)
        turtle.pendown()
        turtle.left(-180)
        turtle.forward(60)
        turtle.penup()
        turtle.goto(100,-30)
        turtle.pendown()
        turtle.right(45)
        turtle.forward(40)
        turtle.penup()
        turtle.goto(100,-30)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(40)
    if intentos ==1:
        turtle.reset()
        turtle.hideturtle()
        turtle.speed(5)
        turtle.penup()
        turtle.goto(-50, -150)
        turtle.pendown()
        turtle.forward(100)
        turtle.penup()
        turtle.goto(0, -150)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(200)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(20)
        turtle.penup()
        turtle.goto( 80, 10)
        turtle.pendown()
        turtle.circle(20)
        turtle.penup()
        turtle.goto(100,-70)
        turtle.pendown()
        turtle.left(-180)
        turtle.forward(60)
        turtle.penup()
        turtle.goto(100,-30)
        turtle.pendown()
        turtle.right(45)
        turtle.forward(40)
        turtle.penup()
        turtle.goto(100,-30)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(40)
        turtle.penup()
        turtle.goto(100,-70)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(30)
        turtle.left(45)
        turtle.forward(30)

# Función para adivinar la letra
def adivinar_letra(palabra_secreta, letras_adivinadas, letras_erroneas):
    while True:
        letra = turtle.textinput("ADIVINA UNA LETRA","Pista: una verdura").lower()
        if len(letra) == 1 and letra.isalpha():
            if letra in letras_adivinadas or letra in letras_erroneas:
                continue
            return letra, True
        elif len(letra) == len(palabra_secreta) and letra.isalpha():
            return letra, False

def mostrar_palabra_oculta(palabra_secreta, letras_adivinadas):
    palabra_oculta = ""
    for letra_palabra in palabra_secreta:
        if letra_palabra in letras_adivinadas:
            palabra_oculta += letra_palabra
        else:
            palabra_oculta += " _ "
    return palabra_oculta

def mostrar_letras_erroneas(letras_erroneas):
    letras_incorrectas = " ".join (letras_erroneas)
    return letras_incorrectas

# Función principal
def juego_ahorcado():
    turtle.clear()
    turtle.bgcolor("white")    
    turtle.pencolor("black")
    palabra_secreta = elegir_palabra()
    letras_adivinadas = []
    letras_erroneas = []
    intentos = 6
    turtle.hideturtle()
    turtle.speed(2)
    turtle.penup()
    turtle.goto(-100, -200)
    turtle.pendown()
    turtle.forward(200)

    while intentos > 0:
        letra, intento_valido = adivinar_letra(palabra_secreta, letras_adivinadas, letras_erroneas)
        if not intento_valido:
            continue
        if len(letra) == 1:
            if letra in palabra_secreta:
                letras_adivinadas.append(letra)
            else:
                intentos -= 1
                letras_erroneas.append(letra)
        else:
            if letra == palabra_secreta:
                letras_adivinadas.extend(palabra_secreta)
            else:
                intentos -= 1
                letras_erroneas.append(letra)
       
        turtle.clear()
        dibujo_juego (intentos)        
        palabra_oculta = mostrar_palabra_oculta(palabra_secreta, letras_adivinadas)
        letras_incorrectas = mostrar_letras_erroneas (letras_erroneas)
        turtle.penup()
        turtle.goto(0, -200)
        turtle.pendown()
        turtle.color("#2E8B57")
        turtle.write("Palabra Secreta: "+ palabra_oculta, move=False, align="center", font=("Arial", 24, "normal"))        
        turtle.penup()
        turtle.goto(0, -250)
        turtle.pendown()
        turtle.color("#FFA500")
        turtle.write("Incorrectas: "+ letras_incorrectas, move=False, align="center", font=("Arial", 18, "normal"))

        if "_" not in palabra_oculta:
            turtle.speed(4)
            turtle.penup()
            turtle.goto(100, 10)
            turtle.pendown()
            turtle.Screen().bgcolor("#008000")  
            turtle.penup()
            turtle.goto(0,150)
            turtle.pendown()
            turtle.color ("#006400")
            turtle.write("¡FELICIDADES GANASTE!", move=False, align="center", font=("Snap ITC", 30, "bold"))
            palabra_oculta = ""            
            break

        if intentos == 0:
            turtle.reset()
            turtle.hideturtle()
            turtle.speed(4)
            turtle.penup()
            turtle.goto(-50, -150)
            turtle.pendown()
            turtle.forward(100)
            turtle.penup()
            turtle.goto(0, -150)
            turtle.pendown()
            turtle.left(90)
            turtle.forward(200)
            turtle.right(90)
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(20)        
            turtle.penup()
            turtle.goto( 80, 10)
            turtle.pendown()
            turtle.circle(20)           
            turtle.penup()
            turtle.goto(100,-70)
            turtle.pendown()
            turtle.left(-180)
            turtle.forward(60)
            turtle.penup()
            turtle.goto(100,-30)
            turtle.pendown()
            turtle.right(45)
            turtle.forward(40)
            turtle.penup()
            turtle.goto(100,-30)
            turtle.pendown()
            turtle.left(90)
            turtle.forward(40)
            turtle.penup()
            turtle.goto(100,-70)
            turtle.pendown()
            turtle.left(90)
            turtle.forward(30)
            turtle.left(45)
            turtle.forward(30)
            turtle.penup()
            turtle.goto(100,-70)
            turtle.pendown()
            turtle.right (-45)
            turtle.forward(30)
            turtle.right(45)
            turtle.forward(30)
            turtle.penup()
            turtle.goto(100, 10)
            turtle.pendown()
            turtle.write("X   X", move=False, align="center", font=("arial", 8, "normal"))
            turtle.Screen().bgcolor("#FF0000")
            turtle.penup()
            turtle.goto(0,150)
            turtle.pendown()
            turtle.color ("#B22222")
            turtle.write("¡AHORCADO! La palabra secreta era: "+ palabra_secreta, move=False, align="center", font=("Snap ITC", 15, "bold"))
            
    jugar_de_nuevo = turtle.textinput ("¿Jugar de nuevo", "Si-(S) o No-(N)").lower()
    if jugar_de_nuevo == "s":
        turtle.reset()
        juego_ahorcado()
    turtle.Terminator()
turtle.reset()
juego_ahorcado()        