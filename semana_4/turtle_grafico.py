import turtle

# Crear una ventana gráfica
ventana = turtle.Screen()
ventana.bgcolor("green")

# Crear una tortuga
tortuga = turtle.Turtle()
tortuga.color("white")
tortuga.shape("circle")
tortuga.pensize(5)

# Dibuja un cuadrado
for t in range(4):
    tortuga.forward(100)
    tortuga.right(90)

# Cierra la ventana haciendo clic
ventana.exitonclick()